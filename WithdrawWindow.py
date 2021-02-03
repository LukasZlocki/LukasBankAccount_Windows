# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter
import db_adapter
import bankaccount

class WithdrawWindowGUI:
    def __init__(self, withdrawWindow):
        # Create the delete window 
        self.withdrawWindow = withdrawWindow
        self.withdrawWindow.geometry("300x200")
        self.withdrawWindow.title("Lucas Bank Account - Withdraw")

        self.adapterDb = db_adapter.dbAdapter()

        global adapter
        global account
        adapter = self.adapterDb


        # DEF to code
        def searchAccount_clicked():
            global adapter
            global account
            accNb = self.user_entry.get()
            account = adapter.getAccountDataByAccountNumber(accNb)
            self.label_presentBalance.config(text = 'Balance : ' + str(account.get_balance()))

        def withdrawSend_clicked():
            global account
            userWithdraw = float(self.userBal_entry.get())
            account.withdraw(userWithdraw)
            adapter.updateDatabase(account)


        # ---------------- F R A M E S ----------------
        # Creating frames
        self.description_frame = tkinter.Frame(self.withdrawWindow)
        self.label_frame = tkinter.Frame(self.withdrawWindow)
        self.button_frame = tkinter.Frame(self.withdrawWindow)
        self.wdrlabel1_frame = tkinter.Frame(self.withdrawWindow)
        self.wdrLabel2_frame = tkinter.Frame(self.withdrawWindow)
        self.wdrButton_frame = tkinter.Frame(self.withdrawWindow)

        self.description_frame.grid(row = 0, column = 0)
        self.label_frame.grid(row = 1, column = 0)
        self.button_frame.grid(row = 1, column = 1)
        self.wdrlabel1_frame.grid(row = 2, column = 0)
        self.wdrLabel2_frame.grid(row = 3, column = 0)
        self.wdrButton_frame.grid(row = 3, column = 1)

        # ---------------- L A B E L S ----------------
        # Create Labels with description
        self.description_label = tkinter.Label(self.description_frame, text = 'Account number to WITHDRAW:')
        self.user_entry = tkinter.Entry(self.label_frame)

        self.label_presentBalance = tkinter.Label(self.wdrlabel1_frame, text = 'Balance : ')
        self.userBal_entry = tkinter.Entry(self.wdrLabel2_frame)


        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription      
        self.search_button = tkinter.Button(self.button_frame, text = "Search", width = 8, command = searchAccount_clicked)
        self.depo_button = tkinter.Button(self.wdrButton_frame, text = "Withdraw", width = 8, command = withdrawSend_clicked)

        # Pack objects
        self.description_label.pack(side = 'top')
        self.user_entry.pack(side = 'top')
        self.search_button.pack(side = 'top')
        
        self.label_presentBalance.pack(side = 'top')
        self.userBal_entry.pack(side = 'top')
        self.depo_button.pack(side = 'top')


        # Enter the tkinter main loop.
        tkinter.mainloop()