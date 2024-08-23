import sys 
import tkinter 

def main(): 
    
    N = int(input("Enter the side for button:1:Left 2:Right 3:Top 4:Bottom-->"))
    btn_side = None 
    if N == 1: 
        btn_side = tkinter.LEFT 
    elif N == 2: 
        btn_side = tkinter.RIGHT 
    elif N == 3: 
        btn_side = tkinter.TOP 
    elif N == 4: 
        btn_side = tkinter.BOTTOM
    else: 
        print("Bad choice")
        sys.exit(0) 

    N = int(input("Do you want to expand widget?1: YES, 2:NO-->"))
    btn_expand = None 
    if N == 1: 
        btn_expand = tkinter.YES 
    elif N == 2: 
        btn_expand = tkinter.NO 
    else: 
        print("Bad choice")
        sys.exit(-1)

    if btn_expand == tkinter.YES: 
        N = int(input("Enter side for filling: 1: X only 2: Y only 3:Both-->"))
        if N == 1: 
            btn_fill = tkinter.X 
        elif N == 2: 
            btn_fill = tkinter.Y 
        elif N == 3: 
            btn_fill = tkinter.BOTH 
        else: 
            print("Bad choice")
            sys.exit(-1)

    root_window = tkinter.Tk() 
    root_window.title("Customized Button")

    btn = tkinter.Button(root_window)
    btn.configure(text='Exit', command=sys.exit)
    if btn_expand == tkinter.YES: 
        btn.pack(side=btn_side, expand=btn_expand, fill=btn_fill)
    elif btn_expand == tkinter.NO:
        btn.pack(side=btn_side)

    root_window.mainloop()  

main() 