# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl


# Poprawic licznik - zle zlicza przelaczne recordy

import tkinter
import db_adapter
import bankaccount

import db_adapter

dbPosition = 0
dbRecords = 0 

class ListWindowGUI():
    def __init__(self, listWindow, pR, pD):
        # Create the list window 
        self.listWindow = listWindow
        self.listWindow.geometry("300x200")
        self.listWindow.title("List")

        listWindow.geometry("+{}+{}".format(pR, pD))
        listWindow.resizable(0,0)
        
        # Initialize global adapter
        self.AdapterDb = db_adapter.dbAdapter()

        global dbRecords
        # Get records quantity in db
        dbRecords = self.AdapterDb.getRecordsNumber()

        # position in list 
        global dbPosition
        dbPosition = 0
        # position seen by user 
        global userPossition
        userPossition = 1

        # ---- Function definition ----
        def forward_clicked(): 
            global dbPosition
            global dbRecords
            global userPossition
    
            _beforeDbPos = dbPosition
            _beforeUserPossition = userPossition

            dbPosition = _beforeDbPos + 1 
            userPossition = _beforeUserPossition + 1
            if dbPosition >= dbRecords:
                dbPosition = _beforeDbPos
                userPossition = _beforeUserPossition
            # Get record by position index in db
            account = self.AdapterDb.getRecordByPossitionInList(dbPosition)
            # Refresh labels with account data
            refreshLabels(account, userPossition, dbRecords)

        def backward_clicked():
            global dbPosition
            global dbRecords
            global userPossition

            _beforeDbPos = dbPosition
            _beforeUserPossition = userPossition

            dbPosition = _beforeDbPos - 1
            userPossition = _beforeUserPossition - 1
            if dbPosition <= -1:
                dbPosition = 0
                userPossition = 1
            # Get record by position index in db
            account = self.AdapterDb.getRecordByPossitionInList(dbPosition)
            # Refresh labels with account data
            refreshLabels(account, userPossition, dbRecords)

        def refreshLabels(account, position, records):
            self.db_label1.config(text = account.get_accountNb())
            self.db_label2.config(text = account.get_acctype())
            self.db_label3.config(text = account.get_name())
            self.db_label4.config(text = account.get_balance())
            self.counter_label.config(text = 'Records in database ' + str(position) + ' / ' + str(records))


        # ---------------- F R A M E S ----------------
        self.buttonLeft_frame = tkinter.Frame(self.listWindow)
        self.buttonRight_frame = tkinter.Frame(self.listWindow)
        self.labelLeft_frame = tkinter.Frame(self.listWindow)
        self.labelRight_frame = tkinter.Frame(self.listWindow)
        self.down_frame = tkinter.Frame(self.listWindow)

        self.buttonLeft_frame.grid(row = 0, column = 0)
        self.buttonRight_frame.grid(row = 0, column = 1)
        self.labelLeft_frame.grid(row = 1, column = 0)
        self.labelRight_frame.grid(row = 1, column = 1)
        self.down_frame.grid(row = 2, column = 0, pady = 10)
        
        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription
        self.forward_button = tkinter.Button(self.buttonRight_frame, text = "-->", width = 8, command = forward_clicked)
        self.backward_button = tkinter.Button(self.buttonLeft_frame, text = "<--", width = 8, command = backward_clicked)
        # Create exit_button and label with buttons' description
        self.exit_button = tkinter.Button(self.down_frame, text = "Exit", width = 8, command = self.listWindow.destroy)

        # ---------------- L A B E L S ----------------
        # Create Labels with descriptions
        self.desc_label1 = tkinter.Label(self.labelLeft_frame, text = 'Account number   :')
        self.desc_label2 = tkinter.Label(self.labelLeft_frame, text = 'Account type     :')
        self.desc_label3 = tkinter.Label(self.labelLeft_frame, text = 'Account owner    :')
        self.desc_label4 = tkinter.Label(self.labelLeft_frame, text = 'Account balancer :')
        # Create Labels with database data
        self.db_label1 = tkinter.Label(self.labelRight_frame, text = 'xxxxxxxx')
        self.db_label2 = tkinter.Label(self.labelRight_frame, text = 'xxxxxxxx')
        self.db_label3 = tkinter.Label(self.labelRight_frame, text = 'xxxxxxxx')
        self.db_label4 = tkinter.Label(self.labelRight_frame, text = 'xxxxxxxx')
        # Create label with records counter
        self.counter_label = tkinter.Label(self.down_frame, text = 'Records in database ' + str(dbPosition-1) + ' / ' + str(dbRecords))

        # Pack objects
        self.forward_button.pack(side = 'left')
        self.backward_button.pack(side = 'right')
        self.desc_label1.pack(side = 'top')
        self.desc_label2.pack(side = 'top')
        self.desc_label3.pack(side = 'top')
        self.desc_label4.pack(side = 'top')
        self.db_label1.pack(side = 'top')
        self.db_label2.pack(side = 'top')
        self.db_label3.pack(side = 'top')
        self.db_label4.pack(side = 'top')
        self.counter_label.pack(side = 'top')
        self.exit_button.pack(side = 'top')

        startingAccount = self.AdapterDb.getRecordByPossitionInList(0)
        refreshLabels(startingAccount, userPossition, dbRecords)

        # Enter the tkinter main loop.
        tkinter.mainloop()