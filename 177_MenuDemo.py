import tkinter 
import sys 

def onNew(): 
    print("Clicked on new command from file menu")

def main(): 
    root_window = tkinter.Tk() 
    root_window.title("Menu Demo")
    w_menubar = tkinter.Menu(root_window)
    
    file_menu = tkinter.Menu(w_menubar, tearoff=0)
    w_menubar.add_cascade(label='File', menu = file_menu)
    file_menu.add_command(label='New', command=onNew)
    file_menu.add_separator() 
    file_menu.add_command(label='Save', command=None)
    file_menu.add_command(label='Exit', command=sys.exit)

    edit_menu = tkinter.Menu(w_menubar, tearoff=0)
    w_menubar.add_cascade(label='Edit', menu = edit_menu)

    format_menu = tkinter.Menu(w_menubar, tearoff=0)
    w_menubar.add_cascade(label='Format', menu=format_menu)

    view_menu = tkinter.Menu(w_menubar, tearoff=0)
    w_menubar.add_cascade(label='View', menu = view_menu)

    help_menu = tkinter.Menu(w_menubar, tearoff=0)
    w_menubar.add_cascade(label='Help', menu = help_menu)

    root_window.configure(menu=w_menubar)
    root_window.mainloop()

main() 