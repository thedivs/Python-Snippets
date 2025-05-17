import numpy as np
import pandas as pd
import ast
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# reading/importing both the csv file (movies,credits) creating dataset
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merging both dataset on the basis on Title and ingesting into movies dataset itself
movies = movies.merge(credits, on='title')  # movies dataset will have now column of credits dataset as well
# print(movies.shape)
# required column -  genres,id,keywords,title,overview,cast,crew

# keeping only required columns and ingesting into movies dataset itself
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# ---------------------------------------- Performing few Data Cleaning

movies.dropna(inplace=True)
movies.drop_duplicates(inplace=True)


# ---------------------------------------- Performing few Data Preprocessing

# Function to convert obj into List
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


# Function to convert obj into List with top 3 cast
def convert_cast(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L


# Function to Fetch Director name from the dictionary
def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break;
    return L


ps = PorterStemmer()


# creating function for stemming the words into tags column

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)


# function for recommendation

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    # sorting the similarity on the basis on similarity number and keeping top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)


# converting all the column values into List to contact all of them together
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# replacing the spaces in the string like 'Science Fiction'  = 'ScienceFiction' to make it one entity
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# creating new column as tags which will be concatenation of all the other list columns
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# creating new dataframe as no required other column we have all details in tags itself
new_df = movies[['movie_id', 'title', 'tags']]

# converting the tags column value from list to string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# converting all of them in lower case
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# applying stem
new_df['tags'] = new_df['tags'].apply(stem)

# we need to convert this tag text into vectors so that every movie will be as a vector and while suggestions,
# we will use the nearest vector to recommend - will do vectorisation with 'Bag of words' method
# while doing this we will exclude the stop words from the sentences ie- are,is,the,to,and,an,a,in etc.

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()
# print(vectors.shape)
# features having similar words like [actor,actors]. will apply stemming to make them one form like [actor,actor]

# creating similarity using cosine method of angle
similarity = cosine_similarity(vectors)

pickle.dump(new_df,open('movies.pkl','wb'))

# sendind as dictionary
pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))

pickle.dump(similarity,open('similarity.pkl','wb'))