'''
Code Structure and Logic Improvements

Issue with is_number() function

The function is called in __init__ but doesn't return a value there, which is confusing
It's used inconsistently - sometimes for validation, sometimes to initialize the display


Handle numbers after result calculation

As your own comment suggests, pressing a number after a result should clear entry, but this isn't implemented


Decimal handling

Your own comment mentions "Try to output 2 decimal places only!" but this isn't implemented
The has_decimal method is being checked conditionally in operation methods but not properly used


Type checking inconsistency

In operation methods (add, subtract, etc.), you check self.has_decimal but this is a method, not a property
This condition likely never evaluates properly, causing inconsistent numeric type handling


Zero division error handling

In compute(), you check for zero division after setting self.value2, but you should check before the operation


Unexpected state after computation

After computation, you set self.operation = 'addition' which could lead to unexpected behavior if the user continues with more operations



Performance and Best Practices

Use string formatting for cleaner code

Replace string concatenation with f-strings for better readability


Avoid unnecessary operations

In negate(), you're creating a result string character by character when you could use simpler logic


Use constants for repeated values

Define constants for repeated strings like operation names


State management

After computation, maintain a "result mode" flag to know when to clear the display for new input


Input validation

Implement more robust input validation, especially for decimal points and negative numbers
'''
# Pressing a number after a result should clear entry
# Try to output 2 decimal places only!
# Learn more about storing values as integers
# floats sometimes shoots itself
import tkinter as tk
from tkinter import ttk


class Main(tk.Tk):

    def __init__(self):
        super().__init__()

        self.setup_display()
        self.setup_buttons()

        self.is_number()

        # Bind Button presses for number keys
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '00']
        for digit in self.nums:
            self.bind(digit, lambda event, d=digit: self.insert_digit(d))

        # Binds for other buttons
        self.bind('.', self.insert_decimal)
        self.bind('+', self.add)
        self.bind('-', self.subtract)
        self.bind('/', self.divide)
        self.bind('*', self.multiply)
        self.bind('n', self.negate)
        self.bind('<Delete>', self.clear)
        self.bind('<BackSpace>', self.back)
        self.bind('<Return>', self.compute)

    def setup_display(self):
        self.geometry("500x600")
        self.minsize(width=500, height=600)
        self.title("Calculator")

        # Configure grid layout for the window
        self.columnconfigure((1, 2, 3, 4), weight=1, uniform='x')
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        # Create global variables for storing values
        self.value1 = 0
        self.value2 = 0
        self.operation = ''

    def setup_buttons(self):
        # Create list of key/value pairs to be used in creating number buttons
        self.digits = {
            '1': (3, 1), '2': (3, 2), '3': (3, 3),
            '4': (4, 1), '5': (4, 2), '6': (4, 3),
            '7': (5, 1), '8': (5, 2), '9': (5, 3),
            '0': (6, 1), '00': (6, 2)
        }

        # Create a list of key/value pairs for creating operation and compute buttons
        self.buttons = {
            'C': (2, 1), '+/-': (2, 2), '<-': (2, 3), '*': (2, 4),
                                                      '/': (3, 4),
                                                      '-': (4, 4),
                                                      '+': (5, 4),
                                        '.': (6, 3), '=': (6, 4)
        }

        # Create an Entry Widget for Display
        self.entry = ttk.Entry(
            self,
            font=("Arial", 30),
            state='normal'
            )
        # Grid the Entry Widget
        self.entry.grid(
            column=1,
            row=1,
            columnspan=4,
            sticky='nsew',
            padx=5,
            pady=5
            )

        # Create number buttons and grid them on the window
        for digit, (row, col) in self.digits.items():
            ttk.Button(
                self,
                text=digit,
                command=lambda d=digit: self.insert_digit(d)
                ).grid(column=col, row=row, padx=5, pady=5, sticky='nsew')

        # Create the other buttons and grid them on the window
        for button, (row, col) in self.buttons.items():
            ttk.Button(
                self,
                text=button,
                command=lambda c=button: self.call_func(c)
                ).grid(column=col, row=row, padx=5, pady=5, sticky='nsew')

    # Function for inserting the digits on the Entry Widget
    def insert_digit(self, digit, event=None):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            return
        if iszero:
            self.delete()
        self.entry.insert(tk.END, str(digit))

    # Function that validates the button press and calls associated function
    def call_func(self, command, event=None):
        if command == 'C':
            self.clear()
        elif command == '<-':
            self.back()
        elif command == '+/-':
            self.negate()
        elif command == '*':
            self.multiply()
        elif command == '/':
            self.divide()
        elif command == '-':
            self.subtract()
        elif command == '+':
            self.add()
        elif command == '.':
            self.insert_decimal()
        elif command == '=':
            self.compute()

    # Deletes Entry Widget value
    def delete(self, event=None):
        self.entry.delete(0, 'end')

    # Delete Entry Value and inserts 0 as initial value
    def clear(self, event=None):
        self.delete()
        self.is_number()

    # Checks then returns a value as a float or an int
    def var_type(self, number):
        if number % 1 == 0:
            return int(number)
        return number

    # Validates Entry Value if viable number,
    # sets initial value to 0 if blank
    def is_number(self) -> bool:
        value_get = self.entry.get()
        if value_get == '':
            self.entry.insert(0, '0')
            return False
        else:
            try:
                float(value_get)
                return True
            except ValueError:
                return False

    # Checks if the current entry value is 0
    def is_zero(self):
        value_get = self.entry.get()
        if value_get == '0':
            return True
        else:
            return False

    # Checks for a decimal point in the entry values
    def has_decimal(self):
        get_value = self.entry.get()
        for letter in get_value:
            if letter == '.':
                return True
        return False

    # Transforms entry value into a negative and back if pressed again
    def negate(self, event=None):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            return
        if iszero:
            return
        value_get = self.entry.get()
        result = '-'
        if value_get[0] == '-':
            val = self.var_type(abs(float(value_get)))
            result = str(val)
        else:
            for letter in value_get:
                result += letter

        self.delete()
        self.entry.insert(0, result)

    # Inserts a decimal point if there is none yet returns if already present
    def insert_decimal(self, event=None):
        has_decimal = self.has_decimal()
        if has_decimal:
            return
        self.entry.insert(tk.END, '.')

    # Deletes the last character on the entry
    def back(self, event=None):
        value_get = self.entry.get()
        length = len(value_get)
        self.entry.delete(length-1, 'end')

    # Sets value 1 and operation then preceeds to wait for the second value
    def multiply(self, event=None):
        valid = self.is_number()
        if not valid:
            return
        if self.has_decimal:
            self.value1 = float(self.entry.get())
        else:
            self.value1 = int(self.entry.get())
        self.operation = 'multiplication'
        self.clear()

    # Sets value 1 and operation then preceeds to wait for the second value
    def divide(self, event=None):
        valid = self.is_number()
        if not valid:
            return
        if self.has_decimal:
            self.value1 = float(self.entry.get())
        else:
            self.value1 = int(self.entry.get())
        self.operation = 'division'
        self.clear()

    # Sets value 1 and operation then preceeds to wait for the second value
    def subtract(self, event=None):
        valid = self.is_number()
        if not valid:
            return
        if self.has_decimal:
            self.value1 = float(self.entry.get())
        else:
            self.value1 = int(self.entry.get())
        self.operation = 'subtraction'
        self.clear()

    # Sets value 1 and operation then preceeds to wait for the second value
    def add(self, event=None):
        valid = self.is_number()
        if not valid:
            return
        if self.has_decimal:
            self.value1 = float(self.entry.get())
        else:
            self.value1 = int(self.entry.get())
        self.operation = 'addition'
        self.clear()

    # Computes for the resulting value after accepting the second value for the operation
    def compute(self, event=None):
        result = 0
        valid = self.is_number()
        iszero = self.is_zero()
        value_get = self.entry.get()
        self.value2 = float(value_get)
        if not valid:
            self.delete()
            self.entry.insert(tk.END, 'Invalid Character')
            return
        if self.operation == 'multiplication':
            result = self.value1 * self.value2
        elif self.operation == 'division':
            if iszero:
                self.entry.insert(0, 'ERROR:ZERO DIVISION')
            else:
                result = self.value1 / self.value2
        elif self.operation == 'subtraction':
            result = self.value1 - self.value2
        elif self.operation == 'addition':
            result = self.value1 + self.value2
        self.value1 = self.var_type(result)
        self.delete()
        self.value2 = 0
        self.operation = 'addition'
        self.entry.insert(0, str(self.value1))


if __name__ == "__main__":
    show = Main()
    show.mainloop()
