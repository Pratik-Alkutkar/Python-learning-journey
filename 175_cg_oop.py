import tkinter 

class ComputeGravitational: 
    def onSubmit(): 
        print("Submit clicked!")

    def __init__(self): 
        self.root_window = tkinter.Tk()
        self.msgL = tkinter.Label(self.root_window)
        self.str_var = tkinter.StringVar() 
        self.input_entry = tkinter.Entry(self.root_window)
        self.submit_btn = tkinter.Button(self.root_window)

    def configure(self): 
        self.msgL.configure(text='Enter something:')
        self.input_entry.configure(textvariable=self.str_var)
        self.submit_btn.configure(text='Submit', command=ComputeGravitational.onSubmit)

    def arrange(self): 
        self.msgL.grid(row=0, column=0)
        self.input_entry.grid(row=0, column=1)
        self.submit_btn.grid(row=0, column=2)

    def loop(self): 
        self.root_window.mainloop()
        print("HERE")

def main(): 
    CG = ComputeGravitational() 
    CG.configure() 
    CG.arrange()
    CG.loop() 

main()
