# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter
import db_adapter
import bankaccount

import messageWindow

import mainWindow_gui as mainWindow

class DepositWindowGUI:
    def __init__(self, depositWindow, pR, pD):
        # Create the delete window 
        self.depositWindow = depositWindow
        self.depositWindow.geometry("260x150")
        self.depositWindow.title("Deposit")
        self.accounts_lists = []

        depositWindow.geometry("+{}+{}".format(pR, pD))
        depositWindow.resizable(0,0)

        self.adapterDb = db_adapter.dbAdapter()

        global adapter
        global account
        adapter = self.adapterDb

        # DEF to code
        def searchAccount_clicked():
            # Step I - get account object by account number (from db adapter) / done
            # Step II - deposit money on local object here in depositWindow /
            # step III - sent modified bankaccount object to db adapter
            global adapter
            global account
            accNb = self.user_entry.get()
            account = adapter.getAccountDataByAccountNumber(accNb)
            # Logging : account found or not
            msg = adapter.getLastLog()
            messageWindow.ShowMessage.message(self, msg)
            self.label_presentBalance.config(text = 'Balance : ' + str(account.get_balance()))


        def depositSend_clicked():
            global account
            userBalance = float(self.userBal_entry.get())
            presentBalance = float(account.get_balance())
            newBalance = presentBalance + userBalance
            account.set_balance(newBalance)
            adapter.updateDatabase(account)
            # Logging : account found or not
            msg = adapter.getLastLog()
            messageWindow.ShowMessage.message(self, msg)

            self.depositWindow.destroy
            
            #self.newWindow = tkinter.Tk()
            #self.app = mainWindow.MainWindowGUI(self.newWindow)




        # ---------------- F R A M E S ----------------
        # Creating frames
        self.description_frame = tkinter.Frame(self.depositWindow)
        self.label_frame = tkinter.Frame(self.depositWindow)
        self.button_frame = tkinter.Frame(self.depositWindow)
        self.depolabel1_frame = tkinter.Frame(self.depositWindow)
        self.depoLabel2_frame = tkinter.Frame(self.depositWindow)
        self.depoButton_frame = tkinter.Frame(self.depositWindow)

        self.description_frame.grid(row = 0, column = 0)
        self.label_frame.grid(row = 1, column = 0)
        self.button_frame.grid(row = 1, column = 1)
        self.depolabel1_frame.grid(row = 2, column = 0)
        self.depoLabel2_frame.grid(row = 3, column = 0)
        self.depoButton_frame.grid(row = 3, column = 1)

        # ---------------- L A B E L S ----------------
        # Create Labels with description
        self.description_label = tkinter.Label(self.description_frame, text = 'Account number to DEPOSIT:')
        self.user_entry = tkinter.Entry(self.label_frame)

        self.label_presentBalance = tkinter.Label(self.depolabel1_frame, text = 'Balance : ')
        self.userBal_entry = tkinter.Entry(self.depoLabel2_frame)


        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription      
        self.search_button = tkinter.Button(self.button_frame, text = "Search", width = 8, command = searchAccount_clicked)
        self.depo_button = tkinter.Button(self.depoButton_frame, text = "Deposit", width = 8, command = depositSend_clicked)

        # Pack objects
        self.description_label.pack(side = 'top')
        self.user_entry.pack(side = 'top')
        self.search_button.pack(side = 'top')
       
        self.label_presentBalance.pack(side = 'top')
        self.userBal_entry.pack(side = 'top')
        self.depo_button.pack(side = 'top')


        # Enter the tkinter main loop.
        tkinter.mainloop()