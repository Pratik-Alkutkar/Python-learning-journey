import tkinter 
import sys 

m1_entry_str_var = None 
m2_entry_str_var = None
r_entry_str_var = None
opL_str_var = None

def on_compute(): 
    try: 
        m1 = float(m1_entry_str_var.get())
        m2 = float(m2_entry_str_var.get())
        r = float(r_entry_str_var.get())
    except: 
        opL_str_var.set("Bad values:Error in format conversion")
        return None 
    
    if m1 <= 0.0: 
        opL_str_var.set("Mass of object one cannot be negative")
        return None 
    if m2 <= 0.0: 
        opL_str_var.set("Mass of object two cannot be negative")
        return None 
    if r <= 0.0: 
        opL_str_var.set("Distance between two objects cannot be negative")
        return None 
    
    G = 6.67 * (10 ** -11)
    F = (G * m1 * m2) / (r**2)

    msg = "The force between two objects:%.12f" % F 
    opL_str_var.set(msg)

def on_clear():
    m1_entry_str_var.set("")
    m2_entry_str_var.set("")
    r_entry_str_var.set("")
    opL_str_var.set("")

def on_exit(): 
    sys.exit(0) 

def main(): 
    global m1_entry_str_var
    global m2_entry_str_var 
    global r_entry_str_var 
    global opL_str_var 

    root_window = tkinter.Tk()
    root_window.title("Compute Gravitational")

    m1_L = tkinter.Label(root_window)
    m1_L.configure(text="Enter mass of object one:")

    m1_entry_str_var = tkinter.StringVar()
    m1_E = tkinter.Entry(root_window)
    m1_E.configure(textvariable=m1_entry_str_var)

    m2_entry_str_var = tkinter.StringVar()
    m2_L = tkinter.Label(root_window)
    m2_L.configure(text="Enter mass of object two:")

    m2_E = tkinter.Entry(root_window)
    m2_E.configure(textvariable=m2_entry_str_var)

    r_L = tkinter.Label(root_window)
    r_L.configure(text="Enter distance between objects:")

    r_entry_str_var = tkinter.StringVar()
    r_E = tkinter.Entry(root_window)
    r_E.configure(textvariable=r_entry_str_var)

    compute_button = tkinter.Button(root_window)
    compute_button.configure(text='Compute', command=on_compute)

    clear_button = tkinter.Button(root_window)
    clear_button.configure(text='Clear', command=on_clear)

    exit_button = tkinter.Button(root_window)
    exit_button.configure(text='Exit', command=on_exit)

    opL_str_var = tkinter.StringVar()
    opL = tkinter.Label(root_window)
    opL.configure(textvariable=opL_str_var)

    m1_L.grid(row=0, column=0)
    m1_E.grid(row=0, column=2)
    m2_L.grid(row=1, column=0)
    m2_E.grid(row=1, column=2)
    r_L.grid(row=2, column=0)
    r_E.grid(row=2, column=2)
    compute_button.grid(row=3, column=0)
    clear_button.grid(row=3, column=1)
    exit_button.grid(row=3, column=2)
    opL.grid(row=4, column=1)

    root_window.mainloop() 

main() 