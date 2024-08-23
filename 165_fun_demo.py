import sys 
import tkinter 

string_var = None
s = "ABCDEFGHIJKLMNOPQRTSTUVWXYZ"
i = -1 

def next_handler(): 
    global i 
    global string_var
    i = (i + 1) % len(s) 
    dsp_str = s[i]
    string_var.set(dsp_str)

def main(): 
    global msg 
    global string_var
    
    root_window = tkinter.Tk() 
    root_window.title("Characters in Loop")

    string_var = tkinter.StringVar() 
    string_var.set("Look for next alphabet here")
    msg = tkinter.Label(root_window)
    msg.configure(textvariable=string_var)
    msg.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

    next_button = tkinter.Button(root_window)
    next_button.configure(text='Next', command=next_handler)
    next_button.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

    exit_button = tkinter.Button(root_window)
    exit_button.configure(text='Exit', command=sys.exit)
    exit_button.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

    root_window.mainloop() 

main()