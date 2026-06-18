import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except:
            return []
    return []

# Save tasks
def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = task_entry.get().strip()

    if task:
        tasks.append({"task": task, "completed": False})
        update_listbox()
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Delete task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Mark complete
def mark_complete():
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected]["completed"] = True
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Refresh list
def update_listbox():
    task_listbox.delete(0, tk.END)

    for task in tasks:
        if task["completed"]:
            task_listbox.insert(
                tk.END,
                f"✔ {task['task']}"
            )
        else:
            task_listbox.insert(
                tk.END,
                task["task"]
            )

# GUI
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="To-Do List Manager",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
task_entry.pack(pady=10)

add_btn = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_btn.pack(pady=5)

task_listbox = tk.Listbox(
    root,
    width=50,
    height=15,
    font=("Arial", 11)
)
task_listbox.pack(pady=10)

complete_btn = tk.Button(
    root,
    text="Mark Complete",
    width=20,
    command=mark_complete
)
complete_btn.pack(pady=5)

delete_btn = tk.Button(
    root,
    text="Delete Task",
    width=20,
    command=delete_task
)
delete_btn.pack(pady=5)

tasks = load_tasks()
update_listbox()

root.mainloop()