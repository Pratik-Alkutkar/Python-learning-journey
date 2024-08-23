import tkinter 
import sys 
import time 

L, B, E, D, lst = None, None, None, None, None

i = -1

def onDestroy(): 
    global i 
    i = i + 1 
    if i < len(lst): 
        lst[i].destroy()     

def onTest(): 
    print("Test button clicked")

def main(): 
    global L, B, E, D, lst
    
    root_window = tkinter.Tk() 
    root_window.title("Experimenting with widgets!")

    L = tkinter.Label(root_window)
    L.configure(text="Enter some text:")

    str_var = tkinter.StringVar() 
    E = tkinter.Entry(root_window)
    E.configure(textvariable=str_var)

    B = tkinter.Button(root_window)
    B.configure(text="Test", command=onTest)

    D = tkinter.Button(root_window)
    D.configure(text='Destroy', command=onDestroy) 

    lst = [L, E, B, D]

    L.grid(row=0, column=0)
    E.grid(row=0, column=1)
    B.grid(row=0, column=2)
    D.grid(row=1, column=1)

    root_window.mainloop() 

main() 