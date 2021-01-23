# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter

class DeleteWindowGUI:
    def __init__(self, deleteWindow):
        # Create the delete window 
        self.deleteWindow = deleteWindow
        self.deleteWindow.geometry("200x70")
        self.deleteWindow.title("Lucas Bank Account - Delete")
        #self.accounts_lists = accounts_list

        # Creating frames
        self.description_frame = tkinter.Frame(self.deleteWindow)
        self.label_frame = tkinter.Frame(self.deleteWindow)
        


        # ---------------- L A B E L S ----------------
        # Create Labels with description
        self.description_label = tkinter.Label(self.description_frame, text = 'Account number to DELETE:')
        self.make_entry = tkinter.Entry(self.label_frame, width=10)
        self.make_entry.grid(row = 0, column = 0)


        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription
        self.delete_button = tkinter.Button(self.label_frame, text = "Delete", width = 8)
        self.delete_button.grid(row = 0, column = 1, padx = 10)

        # Pack objects
        self.description_label.pack(side = 'top')
       # self.make_entry.pack(side = 'top')
       # self.delete_button.pack(side = 'top')

        # Pack all frames
        self.description_frame.pack()
        self.label_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()