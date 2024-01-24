import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.listbox = tk.Listbox(master, width=50, height=10)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            removed_task = self.tasks.pop(task_index)
            self.listbox.delete(task_index)
            messagebox.showinfo("Task Removed", f"Task '{removed_task}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
