import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        messagebox.showerror("Ошибка", "Ошибка! Деление на ноль не допускается.")
        return None
    else:
        return x / y

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operation = operation_var.get()

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)

    if result is not None:
        result_label.config(text="Результат: " + str(result))

root = tk.Tk()
root.title("Калькулятор")

num1_entry = tk.Entry(root)
num1_entry.pack()

num2_entry = tk.Entry(root)
num2_entry.pack()

operation_var = tk.StringVar(root)
operation_var.set('add')  # default value

add_button = tk.Radiobutton(root, text='Сложение', variable=operation_var, value='add')
add_button.pack()

subtract_button = tk.Radiobutton(root, text='Вычитание', variable=operation_var, value='subtract')
subtract_button.pack()

multiply_button = tk.Radiobutton(root, text='Умножение', variable=operation_var, value='multiply')
multiply_button.pack()

divide_button = tk.Radiobutton(root, text='Деление', variable=operation_var, value='divide')
divide_button.pack()

calculate_button = tk.Button(root, text='Вычислить', command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Результат: ")
result_label.pack()

root.mainloop()
