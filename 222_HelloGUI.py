import tkinter

def main():
    root_window = tkinter.Tk()
    root_window.title("HelloWin")
    L = tkinter.Label(root_window)
    L.configure(text="Hello Tkinter")
    L.grid(row=0, column=0)
    root_window.mainloop()

main()
