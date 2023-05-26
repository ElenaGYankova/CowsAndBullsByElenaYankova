import random
import tkinter as tk
from tkinter import messagebox
import webbrowser


class CowsAndBullsGame:
    def __init__(self):
        self.secret_number = self.generate_secret_number()
        self.attempts = 0
        self.guesses = []

        self.window = tk.Tk()
        self.window.title("Cows and Bulls Game")
        self.window.configure(bg="white")

        self.label = tk.Label(self.window, text="Enter your guess (4-digit number):", bg="pink", fg="black")
        self.label.pack()

        self.entry = tk.Entry(self.window, width=30, bg='white', fg='blue')
        self.entry.pack()
        self.entry.focus()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess, bg='blue', fg='white')
        self.button.pack()

        self.progress_label = tk.Label(self.window, text="Progress: 0 attempt(s)", bg='white', fg='black')
        self.progress_label.pack()

        self.guesses_label = tk.Label(self.window, text="Numbers tried: ", bg='white', fg='black')
        self.guesses_label.pack()

        self.xoxo_button = tk.Button(self.window, text="Ellie's GitHub", command=self.open_link, bg='pink', fg='blue')
        self.xoxo_button.pack()

        self.entry.bind('<Return>', lambda event: self.check_guess())

    def generate_secret_number(self):
        digits = random.sample(range(0, 10), 4)
        return ''.join(map(str, digits))

    def evaluate_guess(self, guess):
        cows = 0
        bulls = 0

        for i in range(len(self.secret_number)):
            if self.secret_number[i] == guess[i]:
                bulls += 1
            elif self.secret_number[i] in guess:
                cows += 1

        return cows, bulls

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit() or len(guess) != 4:
            messagebox.showwarning("Invalid Guess", "Please enter a 4-digit number.")
        else:
            self.attempts += 1
            cows, bulls = self.evaluate_guess(guess)

            if bulls == 4:
                messagebox.showinfo("Congratulations",
                                    "You guessed the number {} correctly in {} attempts.".format(guess, self.attempts))
                self.window.destroy()
            else:
                messagebox.showinfo("Guess Result", "Cows: {}, Bulls: {}".format(cows, bulls))

            self.guesses.append(guess)
            self.update_progress()

        self.entry.delete(0, tk.END)

    def update_progress(self):
        try:
            if self.window.winfo_exists():
                progress_text = "Progress: {} attempt(s)".format(self.attempts)
                self.progress_label.config(text=progress_text)

                guesses_text = "Numbers tried: " + ', '.join(self.guesses)
                self.guesses_label.config(text=guesses_text)
        except tk.TclError:
            pass

    def open_link(self):
        webbrowser.open('https://github.com/ElenaGYankova')

    def run(self):
        self.window.mainloop()


game = CowsAndBullsGame()
game.run()
