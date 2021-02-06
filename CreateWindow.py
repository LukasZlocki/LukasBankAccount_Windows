# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter
import db_adapter
import bankaccount
from datetime import date


import messageWindow

class CreateWindowGUI:
    def __init__(self, createWindow, pR, pD):
        # Create the delete window 
        self.createWindow = createWindow
        self.createWindow.geometry("300x150")
        self.createWindow.title("Create")     
        self.__dbAdapter = db_adapter.dbAdapter

        createWindow.geometry("+{}+{}".format(pR, pD))
        createWindow.resizable(0,0)


        # ---- Function definition ----
        def CreateProcedure():      
            # ToDo : Code to add account object to data base 
            accNb = self.db_entry1.get() 
            accType = self.db_entry2.get()  
            accName = self.db_entry3.get()  
            accBal = float(self.db_entry4.get()) 
            
            accountInitdate = date.today()

            self.__dbAdapter.createAccount(self, accType, accNb, accName, accBal, accountInitdate)
            # Logging : account added 
            msg = self.__dbAdapter.getLastLog(self)
            messageWindow.ShowMessage.message(self, msg)
            createWindow.destroy()


        # ---------------- F R A M E S ----------------
        # Creating frames
        self.labelLeft_frame = tkinter.Frame(self.createWindow)
        self.labelRight_frame = tkinter.Frame(self.createWindow)
        self.down_frame = tkinter.Frame(self.createWindow)

        self.labelLeft_frame.grid(row = 1, column = 0)
        self.labelRight_frame.grid(row = 1, column = 1)
        self.down_frame.grid(row = 2, column = 0, pady = 10)

        # ---------------- L A B E L S ----------------
        # Create Labels with descriptions
        self.desc_label1 = tkinter.Label(self.labelLeft_frame, text = 'Account number')
        self.desc_label2 = tkinter.Label(self.labelLeft_frame, text = 'Account type [ST/CO/INT]')
        self.desc_label3 = tkinter.Label(self.labelLeft_frame, text = 'Account owner')
        self.desc_label4 = tkinter.Label(self.labelLeft_frame, text = 'Account balancer')
        # Create Labels with database data
        self.db_entry1 = tkinter.Entry(self.labelRight_frame)
        self.db_entry2 = tkinter.Entry(self.labelRight_frame)
        self.db_entry3 = tkinter.Entry(self.labelRight_frame)
        self.db_entry4 = tkinter.Entry(self.labelRight_frame)

        # ---------------- B U T T O N S ----------------
        # Add to database button
        self.add_button = tkinter.Button(self.down_frame, text = "Create", width = 8, command = CreateProcedure)

        # Pack objects
        self.desc_label1.pack(side = 'top')
        self.desc_label2.pack(side = 'top')
        self.desc_label3.pack(side = 'top')
        self.desc_label4.pack(side = 'top')
        self.db_entry1.pack(side = 'top')
        self.db_entry2.pack(side = 'top')
        self.db_entry3.pack(side = 'top')
        self.db_entry4.pack(side = 'top')
        self.add_button.pack(side = 'top')