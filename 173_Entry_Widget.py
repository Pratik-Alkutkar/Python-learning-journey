import tkinter 
import sys 

str_var_entry = None 
str_var_op = None

def on_submit(): 
    msg = str_var_entry.get() 
    str_var_op.set(msg)

def main(): 
    global str_var_entry
    global str_var_op 

    root_window = tkinter.Tk() 
    root_window.title("Entry Widget Demo")

    L1 = tkinter.Label(root_window)
    L1.configure(text="Enter your text:")
    
    str_var_entry = tkinter.StringVar() 
    E1 = tkinter.Entry(root_window)
    E1.configure(textvariable=str_var_entry)

    B1 = tkinter.Button(root_window)
    B1.configure(text="Submit", command=on_submit)

    str_var_op = tkinter.StringVar()
    opL = tkinter.Label(root_window)
    opL.configure(textvariable=str_var_op)

    L1.grid(row=0, column=0)
    E1.grid(row=0, column=1)
    B1.grid(row=0, column=2)
    opL.grid(row=1, column=0)

    root_window.mainloop() 

main()