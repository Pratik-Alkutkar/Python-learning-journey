import tkinter 
import sys 

cnt = 0 

def ok_handler(): 
    global cnt 
    cnt += 1 
    msg_var.set("Ok Button clicked %d times" % cnt)

def main(): 
    global msg_var 

    root_window = tkinter.Tk() 
    root_window.title("Label & Buttons!")

    msg_var = tkinter.StringVar() 
    msg_var.set("Look for the count here")
    msg = tkinter.Label(root_window)
    msg.configure(textvariable=msg_var)

    ok_button = tkinter.Button(root_window)
    ok_button.configure(text='Ok', command=ok_handler) 

    exit_button = tkinter.Button(root_window)
    exit_button.configure(text='Exit', command=sys.exit)

    msg.grid(row=1, column=0)
    ok_button.grid(row=2, column=0)
    exit_button.grid(row=3, column=0)

    root_window.mainloop() 

main() 