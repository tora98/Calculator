'''
CALCULATOR CODE REVIEW SUGGESTIONS by CLAUDE

STRENGTHS:
- Good use of grid layout for UI organization
- Proper error handling for edge cases like division by zero
- Comprehensive validation for number inputs
- Clean separation of arithmetic operations

AREAS FOR IMPROVEMENT:
 
4. IMPROVE GUI ORGANIZATION
   - Create separate methods for UI setup to make __init__ less crowded:
   
   def setup_ui(self):
       self.setup_display()
       self.setup_operation_buttons()
       self.setup_number_buttons()

5. ENHANCE MEMORY MANAGEMENT
   - Current design only supports one operation at a time
   - Consider adding support for expression evaluation or operation chaining

6. IMPROVE ERROR DISPLAY
   - "ERROR!" message doesn't explain what went wrong
   - Add more informative error messages for different error types

7. ADD KEYBOARD SUPPORT
   - Add keyboard bindings for digits and operations:

   # Bind operation keys
   self.bind('+', lambda event: self.add())
   self.bind('-', lambda event: self.subtract())
   # etc.

8. ADD DOCUMENTATION
   - Add docstrings to explain what each method does
   - Example:
   
   def is_number(self):
       """
       Validates if the current entry is a valid number.
       Returns True if valid, False otherwise.
       Also inserts '0' if the entry is empty.
       """
'''
# Pressing a number after a result should clear entry
# Try to output 2 decimal places only
import tkinter as tk
from tkinter import ttk


class Main(tk.Tk):

    def __init__(self):
        super().__init__()
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

        # Bind Button presses for number keys
        for digit in '0123456789':
            self.bind(digit, lambda event, d=digit: self.insert_digit(d))

        # Insert initial value of 0
        self.is_number()

        # Run the mainloop
        self.mainloop()

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
    def call_func(self, command):
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
    def delete(self):
        self.entry.delete(0, 'end')

    # Delete Entry Value and inserts 0 as initial value
    def clear(self):
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
    def negate(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            return
        if iszero:
            return
        value_get = self.entry.get()
        result = '-'
        if value_get[0] == '-':
            absolute = abs(float(value_get))
            result = str(absolute)
        else:
            for letter in value_get:
                result += letter

        self.delete()
        self.entry.insert(0, result)

    # Inserts a decimal point if there is none yet returns if already present
    def insert_decimal(self):
        has_decimal = self.has_decimal()
        if has_decimal:
            return
        self.entry.insert(tk.END, '.')

    # Deletes the last character on the entry
    def back(self):
        value_get = self.entry.get()
        length = len(value_get)
        self.entry.delete(length-1, 'end')

    # Sets value 1 and operation then preceeds to wait for the second value
    def multiply(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'multiplication'
        self.clear()

    # Sets value 1 and operation then preceeds to wait for the second value
    def divide(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'division'
        self.clear()

    # Sets value 1 and operation then preceeds to wait for the second value
    def subtract(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'subtraction'
        self.clear()

    # Sets value 1 and operation then preceeds to wait for the second value
    def add(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'addition'
        self.clear()

    # Computes for the resulting value after accepting the second value for the operation
    def compute(self):
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
        self.entry.insert(0, str(self.value1))


if __name__ == "__main__":
    show = Main()
