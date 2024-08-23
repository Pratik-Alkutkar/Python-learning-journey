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
    root_window.title("Message & Buttons!")

    msg_var = tkinter.StringVar() 
    msg_var.set("See for the count here")
    msg = tkinter.Label(root_window)
    msg.configure(textvariable=msg_var)

    ok_btn = tkinter.Button(root_window)
    ok_btn.configure(text='OK', command=ok_handler)

    exit_btn = tkinter.Button(root_window)
    exit_btn.configure(text='Exit', command=sys.exit)

    msg.grid(row=0, column=0)
    ok_btn.grid(row=1, column=0)
    exit_btn.grid(row=2, column=0)

    root_window.mainloop()

main() 