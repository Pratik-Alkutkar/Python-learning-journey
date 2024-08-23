import tkinter 
import sys 

def ok_handler(): 
    print("Ok is clicked")

def cancel_handler(): 
    print("Cancel is clicked ")

def main(): 
    root_window = tkinter.Tk() 
    root_window.title("Grid Demo")

    L1 = tkinter.Label(root_window) 
    L1.configure(text="Click Ok to continue")

    btn1 = tkinter.Button(root_window)
    btn1.configure(text="Ok", command=ok_handler)

    L2 = tkinter.Label(root_window)
    L2.configure(text="Click Cancel to go to previous Menu")

    btn2 = tkinter.Button(root_window)
    btn2.configure(text='Cancel', command=cancel_handler)

    L1.grid(row=0, column=0)
    btn1.grid(row=0, column=1)

    L2.grid(row=1, column=0)
    btn2.grid(row=1, column=1)
    
    root_window.mainloop() 

main() 