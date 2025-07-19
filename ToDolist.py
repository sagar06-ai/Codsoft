import tkinter as tk
from tkinter import messagebox
import json
import os


TASK_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")

        self.tasks = load_tasks()

      
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.load_task_listbox()

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def load_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task["done"] else "❌"
            self.task_listbox.insert(tk.END, f"{task['title']} [{status}]")

    def add_task(self):
        title = self.task_entry.get().strip()
        if title:
            self.tasks.append({"title": title, "done": False})
            self.task_entry.delete(0, tk.END)
            self.load_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["done"] = True
            self.load_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task first.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.load_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task first.")

    def on_closing(self):
        save_tasks(self.tasks)
        self.root.destroy()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
