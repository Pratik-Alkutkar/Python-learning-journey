import tkinter 
import sys 
import math 

root_window = None 
curr_msg_1, curr_msg_2, curr_msg_3 = None, None, None 
curr_entry_1, curr_entry_2, curr_entry_3 = None, None, None
str_var_entry_1, str_var_entry_2, str_var_entry_3 = None, None, None 
compute_btn, clear_btn, exit_btn = None, None, None 
op_msg = None 
str_var_op_msg = None 

def onComputeGravitational():
    print("Compute Gravitational Here")

def onComputeColomb(): 
    try: 
        q1 = float(str_var_entry_1.get())
        q2 = float(str_var_entry_2.get())
        r = float(str_var_entry_3.get())
    except: 
        str_var_op_msg.set("Invalid input, error in format conversion")
        return None 

    if q1 == 0.0 or q2 == 0.0: 
        str_var_op_msg.set("Magnitude of charge cannot be zero")
        return None 

    if r <= 0.0: 
        str_var_op_msg.set("Invalid distance, distance must be positive")
        return None 

    K = 9 * (10**9)
    mod_q1 = abs(q1)
    mod_q2 = abs(q2)

    mod_F = (K * mod_q1 * mod_q2) / (r**2)  
    if (q1 < 0.0 and q2 < 0.0) or (q1 > 0.0 and q2 > 0.0): 
        msg = "Force of Repulsion between the charges = %.3f" % mod_F
    else: 
        msg = "Force of Attraction between the charges = %.3f" % mod_F
    str_var_op_msg.set(msg)

def onComputeQuadratic(): 
    print("Compute Quadratic Here")

def onClear(): 
    global str_var_entry_1, str_var_entry_2, str_var_entry_3 
    global str_var_op_msg 

    if str_var_entry_1 != None: 
        str_var_entry_1.set("")
    if str_var_entry_2 != None: 
        str_var_entry_2.set("")
    if str_var_entry_3 != None: 
        str_var_entry_3.set("")
    if str_var_op_msg != None: 
        str_var_op_msg.set("")
    
def destroy_current_widgets(): 
    global curr_msg_1, curr_msg_2, curr_msg_3
    global curr_entry_1, curr_entry_2, curr_entry_3 
    global compute_btn, clear_btn, exit_btn
    global op_msg

    if curr_msg_1 != None and type(curr_msg_1) == tkinter.Label:
        curr_msg_1.destroy()
    if curr_msg_2 != None and type(curr_msg_2) == tkinter.Label: 
        curr_msg_2.destroy() 
    if curr_msg_3 != None and type(curr_msg_3) == tkinter.Label: 
        curr_msg_3.destroy() 
    
    if curr_entry_1 != None and type(curr_entry_1) == tkinter.Entry: 
        curr_entry_1.destroy() 
    if curr_entry_2 != None and type(curr_entry_2) == tkinter.Entry: 
        curr_entry_2.destroy() 
    if curr_entry_3 != None and type(curr_entry_3) == tkinter.Entry: 
        curr_entry_3.destroy() 

    if compute_btn != None and type(compute_btn) == tkinter.Button: 
        compute_btn.destroy() 
    if clear_btn != None and type(clear_btn) == tkinter.Button: 
        clear_btn.destroy()
    if exit_btn != None and type(exit_btn) == tkinter.Button: 
        exit_btn.destroy() 

    if op_msg != None and type(op_msg) == tkinter.Label: 
        op_msg.destroy()

def arrange(): 
    curr_msg_1.grid(row=0, column=0)
    curr_msg_2.grid(row=1, column=0)
    curr_msg_3.grid(row=2, column=0)

    curr_entry_1.grid(row=0, column=1)
    curr_entry_2.grid(row=1, column=1)
    curr_entry_3.grid(row=2, column=1)

    compute_btn.grid(row=3, column=0)
    clear_btn.grid(row=3, column=1)
    exit_btn.grid(row=3, column=2)

    op_msg.grid(row=4, column=0)

def onGravitationalSolver(): 
    global root_window 
    global curr_msg_1, curr_msg_2, curr_msg_3 
    global curr_entry_1, curr_entry_2, curr_entry_3 
    global str_var_entry_1, str_var_entry_2, str_var_entry_3 
    global compute_btn, clear_btn, exit_btn 
    global op_msg 
    global str_var_op_msg 

    destroy_current_widgets()
    root_window.title("Gravitational Solver")

    curr_msg_1 = tkinter.Label(root_window)
    curr_msg_1.configure(text="Enter mass of object 1:")

    curr_msg_2 = tkinter.Label(root_window)
    curr_msg_2.configure(text="Enter mass of object 2:")

    curr_msg_3 = tkinter.Label(root_window)
    curr_msg_3.configure(text="Enter distance between the objects:")

    str_var_entry_1 = tkinter.StringVar()
    curr_entry_1 = tkinter.Entry(root_window)
    curr_entry_1.configure(text=str_var_entry_1)

    str_var_entry_2 = tkinter.StringVar()
    curr_entry_2 = tkinter.Entry(root_window)
    curr_entry_2.configure(text=str_var_entry_2)

    str_var_entry_3 = tkinter.StringVar()
    curr_entry_3 = tkinter.Entry(root_window)
    curr_entry_3.configure(text=str_var_entry_3)

    compute_btn = tkinter.Button(root_window)
    compute_btn.configure(text='Compute', command=onComputeGravitational)

    clear_btn = tkinter.Button(root_window)
    clear_btn.configure(text='Clear', command=onClear)

    exit_btn = tkinter.Button(root_window)
    exit_btn.configure(text='Exit', command=sys.exit)

    str_var_op_msg = tkinter.StringVar() 
    op_msg = tkinter.Label(root_window)
    op_msg.configure(textvariable=str_var_op_msg)

    arrange()

def onColombSolver(): 
    global root_window 
    global curr_msg_1, curr_msg_2, curr_msg_3 
    global curr_entry_1, curr_entry_2, curr_entry_3 
    global str_var_entry_1, str_var_entry_2, str_var_entry_3 
    global compute_btn, clear_btn, exit_btn 
    global op_msg 
    global str_var_op_msg

    destroy_current_widgets()
    root_window.title("Colomb Solver")
    curr_msg_1 = tkinter.Label(root_window)
    curr_msg_1.configure(text="Enter charge on particle 1:")

    curr_msg_2 = tkinter.Label(root_window)
    curr_msg_2.configure(text="Enter charge on particle 2:")

    curr_msg_3 = tkinter.Label(root_window)
    curr_msg_3.configure(text="Enter distance between the charges:")

    str_var_entry_1 = tkinter.StringVar()
    curr_entry_1 = tkinter.Entry(root_window)
    curr_entry_1.configure(text=str_var_entry_1)

    str_var_entry_2 = tkinter.StringVar()
    curr_entry_2 = tkinter.Entry(root_window)
    curr_entry_2.configure(text=str_var_entry_2)

    str_var_entry_3 = tkinter.StringVar()
    curr_entry_3 = tkinter.Entry(root_window)
    curr_entry_3.configure(text=str_var_entry_3)

    compute_btn = tkinter.Button(root_window)
    compute_btn.configure(text='Compute', command=onComputeColomb)

    clear_btn = tkinter.Button(root_window)
    clear_btn.configure(text='Clear', command=onClear)

    exit_btn = tkinter.Button(root_window)
    exit_btn.configure(text='Exit', command=sys.exit)

    str_var_op_msg = tkinter.StringVar() 
    op_msg = tkinter.Label(root_window)
    op_msg.configure(textvariable=str_var_op_msg)

    arrange()

def onQuadraticSolver(): 
    global root_window 
    global curr_msg_1, curr_msg_2, curr_msg_3 
    global curr_entry_1, curr_entry_2, curr_entry_3 
    global str_var_entry_1, str_var_entry_2, str_var_entry_3 
    global compute_btn, clear_btn, exit_btn 
    global op_msg 
    global str_var_op_msg

    destroy_current_widgets()
    root_window.title("Quadratic Solver")
    curr_msg_1 = tkinter.Label(root_window)
    curr_msg_1.configure(text="Enter C.F. of x^2:")

    curr_msg_2 = tkinter.Label(root_window)
    curr_msg_2.configure(text="Enter C.F. of x:")

    curr_msg_3 = tkinter.Label(root_window)
    curr_msg_3.configure(text="Enter constant:")

    str_var_entry_1 = tkinter.StringVar()
    curr_entry_1 = tkinter.Entry(root_window)
    curr_entry_1.configure(text=str_var_entry_1)

    str_var_entry_2 = tkinter.StringVar()
    curr_entry_2 = tkinter.Entry(root_window)
    curr_entry_2.configure(text=str_var_entry_2)

    str_var_entry_3 = tkinter.StringVar()
    curr_entry_3 = tkinter.Entry(root_window)
    curr_entry_3.configure(text=str_var_entry_3)

    compute_btn = tkinter.Button(root_window)
    compute_btn.configure(text='Compute', command=onComputeQuadratic)

    clear_btn = tkinter.Button(root_window)
    clear_btn.configure(text='Clear', command=onClear)

    exit_btn = tkinter.Button(root_window)
    exit_btn.configure(text='Exit', command=sys.exit)

    str_var_op_msg = tkinter.StringVar() 
    op_msg = tkinter.Label(root_window)
    op_msg.configure(textvariable=str_var_op_msg)

    arrange()

def main(): 
    global root_window
    root_window = tkinter.Tk() 
    root_window.title("Solvers")

    menu_bar = tkinter.Menu(root_window, tearoff=0)
    menu_solver = tkinter.Menu(menu_bar, tearoff=0)
    menu_help = tkinter.Menu(menu_bar, tearoff=0)
    
    menu_bar.add_cascade(label='File', menu=menu_solver)
    menu_bar.add_cascade(label='About', menu=menu_help)

    menu_solver.add_command(label='Compute Gravitational', command=onGravitationalSolver)
    menu_solver.add_command(label='Compute Colomb', command=onColombSolver)
    menu_solver.add_command(label='Quadratic Solver', command=onQuadraticSolver)
    menu_solver.add_separator() 
    menu_solver.add_command(label='Exit', command=sys.exit)

    menu_help.add_cascade(label='About', command=None)

    root_window.configure(menu = menu_bar)
    root_window.mainloop()

main()