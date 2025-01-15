import random
import string
from tkinter import *

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Password length must be at least 4!")
            return
        # Display the complexity requirements
        complexity_message.set("Your password will contain:\n• Uppercase letters\n• Lowercase letters\n• Numbers\n• Special characters")
        
        # Ensure at least one of each required character type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        # Fill the rest of the password with a random mix of all character types
        characters = string.ascii_letters + string.digits + string.punctuation
        password += [random.choice(characters) for _ in range(length - 4)]
        random.shuffle(password)  # Shuffle to mix the characters
        final_password = ''.join(password)
        result_label.config(text=f"Generated Password: {final_password}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Create the main window
root = Tk()
root.title("Password Generator")

# Input field for password length
Label(root, text="Enter Password Length:").grid(row=0, column=0, pady=10)
length_entry = Entry(root)
length_entry.grid(row=0, column=1, pady=10)

# Complexity information label (initially empty)
complexity_message = StringVar()
complexity_label = Label(root, textvariable=complexity_message, justify=LEFT)
complexity_label.grid(row=1, column=0, columnspan=2, pady=5)

# Button to generate password
Button(root, text="Generate Password", command=generate_password).grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = Label(root, text="Generated Password will appear here.")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
