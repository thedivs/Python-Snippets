import random

words = ["apple", "programming", "hacking", "smartest", "artificial", "robotics"]
word = random.choice(words)
#scramble the random choice word
scrambled = ''.join(random.sample(word,len(word)))

name = input("What is your name ?")
print(f"Hey {name}! Welcome to the Word Scramble game.")
print(f"{name}, I am scrambling a word, can you guess in 3 attempts ? Word is : {scrambled}")

attempts = 3
while attempts  > 0:
    guess = input("What is your guess :").lower()
    if guess == word:
        print(f"Correct ! You win {name}")
    else:
        attempts = attempts - 1
        print(f"Opps ! Attempts left : {attempts}")

if attempts == 0:
    print(f"Sorry {name} ! You are out of tries, Word was - {word}")


    