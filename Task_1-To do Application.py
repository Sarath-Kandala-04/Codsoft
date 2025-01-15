from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task_title = task_title_entry.get()
    task_description = task_description_text.get("1.0", END)
    due_date = due_date_entry.get()
    priority = priority_combobox.get()

    if task_title.strip():
        task_listbox.insert(END, f"{task_title} - {priority}")  # Display basic info in listbox
        # Store full task details (you'd use a more robust storage method)
        tasks.append({
            "title": task_title,
            "description": task_description,
            "due_date": due_date,
            "priority": priority
        })
        task_title_entry.delete(0, END)
        task_description_text.delete("1.0", END)
        due_date_entry.delete(0, END)
        priority_combobox.set("")  # Reset priority selection
    else:
        messagebox.showwarning("Warning", "Task title cannot be empty!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        del tasks[selected_index]  # Remove task from storage
    except IndexError:
        messagebox.showwarning("Warning", "No task selected to delete!")

def clear_tasks():
    task_listbox.delete(0, END)
    tasks.clear()  # Clear task storage

def view_task_details():
    try:
        selected_index = task_listbox.curselection()[0]
        task = tasks[selected_index]
        details_window = Toplevel(root)
        details_window.title(f"Task Details: {task['title']}")

        Label(details_window, text="Title:").grid(row=0, column=0)
        Label(details_window, text=task['title']).grid(row=0, column=1)
        Label(details_window, text="Description:").grid(row=1, column=0)
        Label(details_window, text=task['description']).grid(row=1, column=1)
        Label(details_window, text="Due Date:").grid(row=2, column=0)
        Label(details_window, text=task['due_date']).grid(row=2, column=1)
        Label(details_window, text="Priority:").grid(row=3, column=0)
        Label(details_window, text=task['priority']).grid(row=3, column=1)

    except IndexError:
        messagebox.showwarning("Warning", "No task selected to view!")

# Initialize task storage (replace with a more robust solution)
tasks = []

# Create the main window
root = Tk()
root.title("To-Do List Application")

# Task title input
Label(root, text="Task Title:").grid(row=0, column=0, padx=5, pady=5)
task_title_entry = Entry(root, width=35)
task_title_entry.grid(row=0, column=1, padx=5, pady=5)

# Task description input
Label(root, text="Description:").grid(row=1, column=0, padx=5, pady=5)
task_description_text = Text(root, width=35, height=5)
task_description_text.grid(row=1, column=1, padx=5, pady=5)

# Due date input
Label(root, text="Due Date:").grid(row=2, column=0, padx=5, pady=5)
due_date_entry = Entry(root, width=12)
due_date_entry.grid(row=2, column=1, padx=5, pady=5)

# Priority selection
Label(root, text="Priority:").grid(row=3, column=0, padx=5, pady=5)
priority_combobox = ttk.Combobox(root, values=["High", "Medium", "Low"])
priority_combobox.grid(row=3, column=1, padx=5, pady=5)

# Add task button
Button(root, text="Add Task", command=add_task).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Task list display
task_listbox = Listbox(root, width=50, height=10)
task_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Buttons for managing tasks
Button(root, text="Delete Selected Task", command=delete_task).grid(row=6, column=0, padx=5, pady=5)
Button(root, text="Clear All Tasks", command=clear_tasks).grid(row=6, column=1, padx=5, pady=5)
Button(root, text="View Task Details", command=view_task_details).grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()