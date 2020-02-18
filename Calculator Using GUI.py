import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry(root) 
entry2 = tk.Entry(root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot():  
    x1 = entry1.get()
    
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)

def Plus():  
    x1 = entry1.get()
    x2 = entry2.get()
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)
    
Plus = tk.Button(text='+', command=Addition)
Minus = tk.Button(text='-', command=Subtraction)
Multiplication = tk.Button(text='*', command=Multiply)
Division = tk.Button(text='/', command=Division)


canvas1.create_window(200, 180, window=button1)


root.mainloop()