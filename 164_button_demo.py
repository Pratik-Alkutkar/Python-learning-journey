import tkinter 
import sys 

def exit_btn_handler(): 
    print("Exit button clicked")
    sys.exit(0)

def main(): 
    root_window = tkinter.Tk()
    root_window.title("Button Demo")

    btn_1 = tkinter.Button(root_window)
    btn_1.configure(text='Exit', command=exit_btn_handler) 
    btn_1.pack(side=tkinter.TOP, expand=tkinter.YES)
    
    root_window.mainloop() 

main() 

"""
Experiment: 
    1) expand, fill deu naka. side TOP BOTTOM RIGHT LEFT 
    2) expand == YES, fill X, Y, BOTH 

Program: 
    1) Console End user ask: 
        side?? left, right, top, bottom 
    2) expand, yes, no? 
        if yes? 
            X 
            Y 
            BOTH 

Program: 
    Three Buttons: 
        Ok, Cancel, exit 

        Ok clicked 
        Cancel clicked 
        exit : App terminate             

"""