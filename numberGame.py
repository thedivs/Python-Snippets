import random

secret_number = random.randint(1,100)

name = input("What is your name ?")
print(f"Hey {name}! Welcome to the Number guessing game.")
print(f"{name}, I am thinking of a number between 1 to 100. can you make a guess ?")

attempts = 0
while True:
    guess_num = input("Enter your digit :")
    if not guess_num.isdigit():
        print(f"{name}, Please enter a valid number :")
        continue

    guess = int(guess_num)
    attempts +=1

    if guess< secret_number:
        print("Too Low! Try Again")
    elif guess > secret_number:
        print("Too high! Try Again")
    else:
        print(f"Congrats ! {name}, you have guessed it in {attempts} attempts.")
        break