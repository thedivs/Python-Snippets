import streamlit as st
import pickle
import pandas as pd
import requests


# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=86fe603d3be8a081a2e647bd9404114c&language=en-US".format(
#         movie_id)
#     data = requests.get(url, timeout=None)
#     data = data.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # sorting the similarity on the basis on similarity number and keeping top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        # recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)


