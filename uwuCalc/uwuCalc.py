# _   ___      ___   _ / ___|__ _| | ___ 
#| | | \ \ /\ / / | | | |   / _` | |/ __|
#| |_| |\ V  V /| |_| | |__| (_| | | (__ 
# \__,_| \_/\_/  \__,_|\____\__,_|_|\___|

from tkinter import *

expression = ""
 
 
def press(num):
    global expression
 
    expression = expression + str(num)
 
    equation.set(expression)
 
 
def equalpress():
    try:
 
        global expression
 
        total = str(eval(expression))
 
        equation.set(total)
 
        expression = ""
 
    except:
 
        equation.set(" error ")
        expression = ""
 
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
if __name__ == "__main__":
    gui = Tk()
 
    #here you can adjust the color of the window 
    gui.configure(background="gray")
 
    #here you can set the title of the window
    gui.title("uwuCalc")
 
    #here you can make the window bigger
    gui.geometry("340x400")
 
    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)
 
    #grids
    expression_field.grid(columnspan=6, ipadx=70)
 
    #you can modify or make your own buttons here
    button1 = Button(gui, text=' 1 ', fg='white', bg='gray',
                    command=lambda: press(1), height=2, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='white', bg='gray',
                    command=lambda: press(2), height=2, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='white', bg='gray',
                    command=lambda: press(3), height=2, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='white', bg='gray',
                    command=lambda: press(4), height=2, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='white', bg='gray',
                    command=lambda: press(5), height=2, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='white', bg='gray',
                    command=lambda: press(6), height=2, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='white', bg='gray',
                    command=lambda: press(7), height=2, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='white', bg='gray',
                    command=lambda: press(8), height=2, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='white', bg='gray',
                    command=lambda: press(9), height=2, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='white', bg='gray',
                    command=lambda: press(0), height=2, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='white', bg='gray',
                command=lambda: press("+"), height=2, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='white', bg='gray',
                command=lambda: press("-"), height=2, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='white', bg='gray',
                    command=lambda: press("*"), height=2, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='white', bg='gray',
                    command=lambda: press("/"), height=2, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='white', bg='gray',
                command=equalpress, height=2, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='white', bg='gray',
                command=clear, height=2, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='white', bg='gray',
                    command=lambda: press('.'), height=1, width=7)
    uwu = Button(gui, text=' uwu ', fg='black', bg='red',
                command=lambda: press("uwu"), height=2, width=7)
    uwu.grid(row=6, column=6)

    #start
    gui.mainloop()
