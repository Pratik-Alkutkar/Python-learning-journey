import sys 
import tkinter 

def ok_handler(): 
    print("Ok Button Has been clicked")
    return True 

def cancel_handler(): 
    print("Cancel Button has been clicked")
    return False 

def main(): 
    root_window = tkinter.Tk() 
    root_window.title("Three Button Demo")

    btn1 = tkinter.Button(root_window) 
    btn1.configure(text='Ok', command=ok_handler)
    btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)

    btn2 = tkinter.Button(root_window) 
    btn2.configure(text="Cancel", command=cancel_handler)
    btn2.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)

    btn3 = tkinter.Button(root_window)
    btn3.configure(text="Exit", command=sys.exit)
    btn3.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)

    root_window.mainloop() 


main() 