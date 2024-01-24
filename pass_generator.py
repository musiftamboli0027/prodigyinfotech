import tkinter as tk
from tkinter import ttk, Entry, Label, Button, StringVar
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.password_var = StringVar()
        
        self.length_label = Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = Label(master, text="Generated Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)

        self.password_entry = Entry(master, textvariable=self.password_var, state='readonly')
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Configure the style for a colorful appearance
        self.style = ttk.Style()
        self.style.configure('TButton', foreground='#ffffff', background='#4CAF50')
        self.style.configure('TLabel', foreground='#333333', background='#BDBDBD')
        self.style.configure('TEntry', foreground='#000000', background='#E0E0E0')

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                raise ValueError("Password length should be a positive integer.")

            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_var.set(generated_password)
        except ValueError as e:
            self.password_var.set("Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
