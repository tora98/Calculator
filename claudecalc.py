'''
Key Improvements Made

Better structure and naming

Renamed the class to Calculator for clarity
Added more descriptive method names and docstrings
Grouped related functionality together


Implemented result mode

Added a result_mode flag to track when a calculation has just completed
This allows clearing the display when entering a new number after seeing a result


Better number formatting

Added a format_number method to handle decimal place formatting
Properly strips trailing zeros from decimal values


Improved operation handling

Created constants for operation types
Centralized operation preparation in a single method
Added proper error handling for division by zero


Better display management

Added get_display and set_display helper methods
More consistent handling of the calculator's display state


Simplified button command handling

Used a function map for cleaner command dispatch



These improvements make the calculator more reliable, maintainable, and user-friendly. The code is now better organized with clearer separation of concerns and more consistent behavior.
Would you like me to explain any specific part of these changes in more 
'''
import tkinter as tk
from tkinter import ttk

# Constants for operation types
MULTIPLY = 'multiply'
DIVIDE = 'divide'
ADD = 'add'
SUBTRACT = 'subtract'


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.setup_display()
        self.setup_buttons()
        
        # Initialize the calculator state
        self.initialize_state()

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

    def initialize_state(self):
        """Initialize or reset the calculator state"""
        self.value1 = 0
        self.value2 = 0
        self.operation = ''
        self.result_mode = False  # Flag to indicate if we just calculated a result
        self.set_display('0')

    def setup_display(self):
        """Set up the calculator display and window properties"""
        self.geometry("500x600")
        self.minsize(width=500, height=600)
        self.title("Calculator")

        # Configure grid layout for the window
        self.columnconfigure((1, 2, 3, 4), weight=1, uniform='x')
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

    def setup_buttons(self):
        """Set up the calculator buttons"""
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

    def set_display(self, value):
        """Update the display with the given value"""
        self.entry.delete(0, 'end')
        self.entry.insert(0, value)

    def get_display(self):
        """Get the current value from the display"""
        value = self.entry.get()
        if not value:
            return '0'
        return value

    def insert_digit(self, digit, event=None):
        """Insert a digit into the display"""
        # If we just calculated a result, clear the display first
        if self.result_mode:
            self.set_display('')
            self.result_mode = False
            
        current = self.get_display()
        
        # Replace initial zero with the digit
        if current == '0':
            self.set_display(digit)
        else:
            self.entry.insert(tk.END, digit)

    def call_func(self, command, event=None):
        """Call the appropriate function based on the button pressed"""
        function_map = {
            'C': self.clear,
            '<-': self.back,
            '+/-': self.negate,
            '*': self.multiply,
            '/': self.divide,
            '-': self.subtract,
            '+': self.add,
            '.': self.insert_decimal,
            '=': self.compute
        }
        
        if command in function_map:
            function_map[command]()

    def clear(self, event=None):
        """Clear the display and reset calculator state"""
        self.initialize_state()

    def format_number(self, number):
        """Format the number to display with appropriate decimal places"""
        # Convert to float first to handle potential decimal values
        num = float(number)
        
        # If it's a whole number, return as integer
        if num.is_integer():
            return str(int(num))
        
        # Format with 2 decimal places if it has decimals
        return f"{num:.2f}".rstrip('0').rstrip('.') if '.' in str(num) else str(int(num))

    def is_valid_number(self, value=None):
        """Check if the current display value is a valid number"""
        value = value if value is not None else self.get_display()
        if value == '':
            return False
            
        try:
            float(value)
            return True
        except ValueError:
            return False

    def has_decimal(self, value=None):
        """Check if the current display value has a decimal point"""
        value = value if value is not None else self.get_display()
        return '.' in value

    def negate(self, event=None):
        """Negate the current display value"""
        current = self.get_display()
        
        if current == '0':
            return
            
        if current.startswith('-'):
            self.set_display(current[1:])
        else:
            self.set_display(f"-{current}")

    def insert_decimal(self, event=None):
        """Insert a decimal point if there isn't one already"""
        if self.result_mode:
            self.set_display('0')
            self.result_mode = False
            
        current = self.get_display()
        
        if not self.has_decimal():
            self.entry.insert(tk.END, '.')

    def back(self, event=None):
        """Delete the last character from the display"""
        current = self.get_display()
        
        if len(current) <= 1 or (len(current) == 2 and current.startswith('-')):
            self.set_display('0')
        else:
            self.entry.delete(len(current) - 1, 'end')

    def prepare_operation(self, operation_type):
        """Prepare for an operation by storing the current value and operation"""
        if not self.is_valid_number():
            return
            
        self.value1 = float(self.get_display())
        self.operation = operation_type
        self.set_display('0')
        self.result_mode = False

    def multiply(self, event=None):
        """Prepare for multiplication operation"""
        self.prepare_operation(MULTIPLY)

    def divide(self, event=None):
        """Prepare for division operation"""
        self.prepare_operation(DIVIDE)

    def subtract(self, event=None):
        """Prepare for subtraction operation"""
        self.prepare_operation(SUBTRACT)

    def add(self, event=None):
        """Prepare for addition operation"""
        self.prepare_operation(ADD)

    def compute(self, event=None):
        """Compute the result of the operation"""
        if not self.is_valid_number() or not self.operation:
            return
            
        self.value2 = float(self.get_display())
        
        try:
            if self.operation == MULTIPLY:
                result = self.value1 * self.value2
            elif self.operation == DIVIDE:
                if self.value2 == 0:
                    self.set_display('ERROR: DIVISION BY ZERO')
                    return
                result = self.value1 / self.value2
            elif self.operation == SUBTRACT:
                result = self.value1 - self.value2
            elif self.operation == ADD:
                result = self.value1 + self.value2
            else:
                return
                
            # Format and display the result
            formatted_result = self.format_number(result)
            self.set_display(formatted_result)
            
            # Update calculator state
            self.value1 = float(formatted_result)
            self.value2 = 0
            self.operation = ''
            self.result_mode = True
            
        except Exception as e:
            self.set_display(f"ERROR: {str(e)}")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()