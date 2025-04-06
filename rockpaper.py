import tkinter as tk
import random

# All possible choices
choices = ["rock", "paper", "scissors", "lizard", "spock"]
 
# Rules dictionary (what beats what)
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

# Score tracking
user_score = 0
comp_score = 0

# Function to play a round
def play(choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    result_text.set(f"You chose {choice}\nComputer chose {comp_choice}")

    if choice == comp_choice:
        outcome_text.set("It's a tie!")
    elif comp_choice in rules[choice]:
        user_score += 1
        outcome_text.set("You win this round!")
    else:
        comp_score += 1
        outcome_text.set("Computer wins this round!")

    score_text.set(f"Score — You: {user_score} | Computer: {comp_score}")

# Setup the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors, Lizard, Spock")
root.geometry("400x450")
root.resizable(False, False)

# UI Labels
title = tk.Label(root, text="Rock, Paper, Scissors, Lizard, Spock", font=("Helvetica", 14, "bold"))
title.pack(pady=10)

result_text = tk.StringVar()
outcome_text = tk.StringVar()
score_text = tk.StringVar(value="Score — You: 0 | Computer: 0")

result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12), justify="center")
result_label.pack(pady=10)

outcome_label = tk.Label(root, textvariable=outcome_text, font=("Helvetica", 12, "italic"), fg="blue")
outcome_label.pack()

score_label = tk.Label(root, textvariable=score_text, font=("Helvetica", 12))
score_label.pack(pady=10)

# Buttons for choices
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

for item in choices:
    btn = tk.Button(btn_frame, text=item.capitalize(), width=10, command=lambda c=item: play(c))
    btn.pack(side="left", padx=5)

# Run the app
root.mainloop()
