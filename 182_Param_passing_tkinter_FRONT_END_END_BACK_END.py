#-----------------------------------------------------------------------

import tkinter

root_win = tkinter.Tk()
root_win.title("Test")

B = tkinter.Button(root_win)

# Client side / front end 
B.configure(text="Exit", command=sys.exit, fg='', bg='')

root_win.mainloop()
#----------------------------------------------------------------------
# Server side / Backend 

tkinter.py ---> tkinter package

class Button:

    def configure(self, **kwargs):
      

        valid_keys = ['text', 'command', 'fg', 'bg']

        for key in kwargs.keys():
            if key not in valid_keys:
                raise ValueError
        kwargs['text']
        kwargs['command']
        kwargs['fg']
