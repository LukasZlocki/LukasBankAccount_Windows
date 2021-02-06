# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter
import db_adapter
import bankaccount

import messageWindow

class DeleteWindowGUI:
    def __init__(self, deleteWindow):
        # Create the delete window 
        self.deleteWindow = deleteWindow
        self.deleteWindow.geometry("230x80")
        self.deleteWindow.title("Delete")
        self.accounts_lists = []

        deleteWindow.resizable(0,0)

        # Initialize global adapter
        self.AdapterDb = db_adapter.dbAdapter()

        # ---- Function definition ----
        def deleteProcedure():      
            accNb = self.user_entry.get()
            # Deleting account form data base
            self.AdapterDb.deleteAccountFromDatabase(accNb)
             # Logging : Covid19 restriction logs
            msg = self.AdapterDb.getLastLog()
            messageWindow.ShowMessage.message(self, msg)
            
            deleteWindow.destroy()

        # ---------------- F R A M E S ----------------
        # Creating frames
        self.description_frame = tkinter.Frame(self.deleteWindow)
        self.label_frame = tkinter.Frame(self.deleteWindow)
        self.button_frame = tkinter.Frame(self.deleteWindow)

        self.description_frame.grid(row = 0, column = 0)
        self.label_frame.grid(row = 1, column = 0)
        self.button_frame.grid(row = 1, column = 1)

        # ---------------- L A B E L S ----------------
        # Create Labels with description
        self.description_label = tkinter.Label(self.description_frame, text = 'Account number to DELETE:')
        self.user_entry = tkinter.Entry(self.label_frame)

        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription      
        self.delete_button = tkinter.Button(self.button_frame, text = "Delete", width = 8, command = deleteProcedure)

        # Pack objects
        self.description_label.pack(side = 'top')
        self.user_entry.pack(side = 'top')
        self.delete_button.pack(side = 'top')

        # Enter the tkinter main loop.
        tkinter.mainloop()

       

        


