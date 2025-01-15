from tkinter import *

def calculate(operator):
    """
    Performs the selected arithmetic operation and displays the result.
    """
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
            else:
                result = num1 / num2
        else:
            result_label.config(text="Invalid operator")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers.")

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Create labels and entry fields for numbers
num1_label = Label(root, text="Enter first number:")
num1_label.grid(row=0, column=0)
num1_entry = Entry(root)
num1_entry.grid(row=0, column=1)

num2_label = Label(root, text="Enter second number:")
num2_label.grid(row=1, column=0)
num2_entry = Entry(root)
num2_entry.grid(row=1, column=1)

# Create buttons for each operator
add_button = Button(root, text="+", command=lambda: calculate("+"))
add_button.grid(row=2, column=0)

subtract_button = Button(root, text="-", command=lambda: calculate("-"))
subtract_button.grid(row=2, column=1)

multiply_button = Button(root, text="*", command=lambda: calculate("*"))
multiply_button.grid(row=3, column=0)

divide_button = Button(root, text="/", command=lambda: calculate("/"))
divide_button.grid(row=3, column=1)

# Create a label to display the result
result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()