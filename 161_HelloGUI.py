import tkinter 

def main(): 

    root_window = tkinter.Tk() 
    root_window.title("HelloWin!")

    msg = tkinter.Label(root_window)
    msg.configure(text='Hello, GUI World!')
    msg.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH) 

    root_window.mainloop() 

main() 

# Window GADGET = WIDGET 