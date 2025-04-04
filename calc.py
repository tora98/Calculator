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

        self.columnconfigure((1, 2, 3, 4), weight=1, uniform='x')
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

        self.value1 = 0
        self.value2 = 0
        self.operation = ''

        self.entry = ttk.Entry(
            self,
            font=("Arial", 30),
            state='normal'
            )
        self.entry.grid(
            column=1,
            row=1,
            columnspan=4,
            sticky='nsew',
            padx=5,
            pady=5
            )

        self.btnclear = ttk.Button(
            self,
            text='C',
            command=self.clear
            )
        self.btnclear.grid(
            column=1,
            row=2,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btnnegate = ttk.Button(
            self,
            text='-/+',
            command=self.negate
            )
        self.btnnegate.grid(
            column=2,
            row=2,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btnback = ttk.Button(
            self,
            text='<-',
            command=self.back
            )
        self.btnback.grid(
            column=3,
            row=2,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btnmultiply = ttk.Button(
            self,
            text='*',
            command=self.multiply
            )
        self.btnmultiply.grid(
            column=4,
            row=2,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn1 = ttk.Button(
            self,
            text='1',
            command=self.insert1
            )
        self.btn1.grid(
            column=1,
            row=3,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn2 = ttk.Button(
            self,
            text='2',
            command=self.insert2
            )
        self.btn2.grid(
            column=2,
            row=3,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn3 = ttk.Button(
            self,
            text='3',
            command=self.insert3
            )
        self.btn3.grid(
            column=3,
            row=3,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btndivide = ttk.Button(
            self,
            text='/',
            command=self.divide
            )
        self.btndivide.grid(
            column=4,
            row=3,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn4 = ttk.Button(
            self,
            text='4',
            command=self.insert4
            )
        self.btn4.grid(
            column=1,
            row=4,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn5 = ttk.Button(
            self,
            text='5',
            command=self.insert5
            )
        self.btn5.grid(
            column=2,
            row=4,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn6 = ttk.Button(
            self,
            text='6',
            command=self.insert6
            )
        self.btn6.grid(
            column=3,
            row=4,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btnsubtract = ttk.Button(
            self,
            text='-',
            command=self.subtract
            )
        self.btnsubtract.grid(
            column=4,
            row=4,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn7 = ttk.Button(
            self,
            text='7',
            command=self.insert7
            )
        self.btn7.grid(
            column=1,
            row=5,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn8 = ttk.Button(
            self,
            text='8',
            command=self.insert8
            )
        self.btn8.grid(
            column=2,
            row=5,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn9 = ttk.Button(
            self,
            text='9',
            command=self.insert9
            )
        self.btn9.grid(
            column=3,
            row=5,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btnadd = ttk.Button(
            self,
            text='+',
            command=self.add
            )
        self.btnadd.grid(
            column=4,
            row=5,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn0 = ttk.Button(
            self,
            text='0',
            command=self.insert0
            )
        self.btn0.grid(
            column=1,
            row=6,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btn00 = ttk.Button(
            self,
            text='00',
            command=self.insert00
            )
        self.btn00.grid(
            column=2,
            row=6,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btndecimal = ttk.Button(
            self,
            text='.',
            command=self.insert_decimal
            )
        self.btndecimal.grid(
            column=3,
            row=6,
            padx=5,
            pady=5,
            sticky='nsew'
            )

        self.btnecompute = ttk.Button(
            self,
            text='=',
            command=self.compute
            )
        self.btnecompute.grid(
            column=4,
            row=6,
            padx=5,
            pady=5,
            sticky='nsew'
            )
        self.entry.insert(tk.END, '0')

        self.mainloop()

    def delete(self):
        self.entry.delete(0, 'end')

    def clear(self):
        self.entry.delete(0, 'end')
        self.is_number()

    def is_number(self):
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

    def is_zero(self):
        value_get = self.entry.get()
        if value_get == '0':
            return True
        else:
            return False

    def has_decimal(self):
        get_value = self.entry.get()
        for letter in get_value:
            if letter == '.':
                return True
        return False

    def err(self):
        self.delete()
        self.entry.insert(0, 'ERROR!')

    def insert1(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            return
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '1')

    def insert2(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '2')

    def insert3(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '3')

    def insert4(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '4')

    def insert5(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '5')

    def insert6(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '6')

    def insert7(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '7')

    def insert8(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '8')

    def insert9(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            self.delete()
        self.entry.insert(tk.END, '9')

    def insert0(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            return
        self.entry.insert(tk.END, '0')

    def insert00(self):
        valid = self.is_number()
        iszero = self.is_zero()
        if not valid:
            pass
        if iszero:
            return
        self.entry.insert(tk.END, '00')

# Awaiting Logic From isnumber Function
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

    def insert_decimal(self):
        has_decimal = self.has_decimal()
        if has_decimal:
            return
        self.entry.insert(tk.END, '.')

    def back(self):
        value_get = self.entry.get()
        length = len(value_get)
        self.entry.delete(length-1, 'end')

    def multiply(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'multiplication'
        self.clear()

    def divide(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'division'
        self.clear()

    def subtract(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'subtraction'
        self.clear()

    def add(self):
        valid = self.is_number()
        if not valid:
            return
        self.value1 = float(self.entry.get())
        self.operation = 'addition'
        self.clear()

    def var_type(self, number):
        if number % 1 == 0:
            return int(number)
        return number

    def compute(self):
        result = 0
        valid = self.is_number()
        iszero = self.is_zero()
        value_get = self.entry.get()
        self.value2 = float(value_get)
        if not valid:
            self.delete()
            self.entry.insert(tk.END, 'Err')
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
