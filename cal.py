from tkinter import *
import math  # Import math module for functions like sin, cos, tan, log10

root = Tk()
root.geometry("650x350")
root.title("Yuvanshu Dadhich Calculator")

def click(event):
    global value
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = value.get()
            # If the expression is just digits, convert directly to int
            if expression.isdigit():
                val = int(expression)
            else:
                # Replace function names with their corresponding math module calls
                expression = expression.replace("sin", "math.sin")
                expression = expression.replace("cos", "math.cos")
                expression = expression.replace("tan", "math.tan")
                expression = expression.replace("log", "math.log10")
                expression = expression.replace("sqrt", "math.sqrt")
                expression = expression.replace("^", "")

                # Evaluate the replaced expression
                val = eval(expression)
            value.set(val)
        except Exception as e:
            value.set("Error")
        screen.update()
    
    elif text == "C":
        value.set("")
        screen.update()
    
    elif text == "x":  # Backspace function
        value.set(value.get()[:-1])
        screen.update()
    
    else:
        value.set(value.get() + text)
        screen.update()

# Initialize the string variable with an empty string
value = StringVar()
value.set("")
screen = Entry(root, textvariable=value, font="lucida 32 bold", border=5)
screen.pack(padx=10, pady=10)

# Row 1 Buttons
f = Frame(root, bg="white")
b = Button(f, text="C", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="x", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="sin", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Row 2 Buttons
f = Frame(root, bg="white")
b = Button(f, text="7", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="cos", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Row 3 Buttons
f = Frame(root, bg="white")
b = Button(f, text="4", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="tan", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Row 4 Buttons
f = Frame(root, bg="white")
b = Button(f, text="1", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="log", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

# Row 5 Buttons
f = Frame(root, bg="white")
b = Button(f, text="00", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="sqrt", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f.pack()

# Row 6 Buttons
f = Frame(root, bg="white")
b = Button(f, text="(", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text=")", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="^", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
