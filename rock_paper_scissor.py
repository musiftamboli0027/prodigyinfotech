import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

class RPSGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.choices = ['rock', 'paper', 'scissors']

        self.user_choice_var = tk.StringVar()
        self.computer_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select your choice:").pack()

        for choice in self.choices:
            tk.Radiobutton(self.master, text=choice.capitalize(), variable=self.user_choice_var,
                           value=choice).pack()

        tk.Button(self.master, text="Play", command=self.play_game).pack()

        tk.Label(self.master, text="Computer's choice:").pack()
        tk.Label(self.master, textvariable=self.computer_choice_var).pack()

        tk.Label(self.master, text="Result:").pack()
        tk.Label(self.master, textvariable=self.result_var).pack()

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(self.choices)
        
        self.computer_choice_var.set(computer_choice.capitalize())

        result = determine_winner(user_choice, computer_choice)
        self.result_var.set(result)

        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGameApp(root)
    root.mainloop()
