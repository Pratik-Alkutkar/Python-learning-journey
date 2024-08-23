import sys, time, tkinter 

def time_button_real_handler(time_as_float:float)->None: 
    print(time.ctime(time_as_float))

def time_handler(): 
    time_button_real_handler(time.time())

def main(): 
    root_window = tkinter.Tk()
    root_window.title("Time Button Demo")

    time_btn = tkinter.Button(root_window)
    time_btn.configure(text='Time', command=time_handler)
    time_btn.pack(side=tkinter.TOP, expand=tkinter.YES, fill = tkinter.X)

    root_window.mainloop() 

main() 

