# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter

import DeleteWindow_gui as deleteWindow
import ListWindow as listWindow
import CreateWindow as createWindow
import DepositWindow as depositWindow
import WithdrawWindow as withdrawWindow

import db_adapter

dbRecords = 0 


class MainWindowGUI:
    def __init__(self, mainWindow):
        # Create the main window 
        self.mainWindow = mainWindow 
        self.mainWindow.geometry("150x220")
        self.mainWindow.title("Lucas Bank Account - MENU")

        mainWindow.resizable(0,0)

        # Initialize global adapter
        self.AdapterDb = db_adapter.dbAdapter()
        # Get records quantity in db
        global dbRecords      
        dbRecords = self.AdapterDb.getRecordsNumber()


        # Creating frames
        self.menu_frame = tkinter.Frame()


        # ---------------- L A B E L S ----------------
        # Create Label with description
        self.records_label = tkinter.Label(self.menu_frame, text = 'Records in database : ' + str(dbRecords))
        # Create Label with description
        self.desc_label = tkinter.Label(self.menu_frame, text = 'Choose your function :')
        

        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription
        self.create_button = tkinter.Button(self.menu_frame, text = "Create", width = 8, command = self.Create_command)
        # Create delete_button and lebel with buttons' decription
        self.delete_button = tkinter.Button(self.menu_frame, text = "Delete", width = 8, command = self.Delete_command)
        # Create deposit_button and lebel with buttons' decription
        self.deposit_button = tkinter.Button(self.menu_frame, text = "Deposit", width = 8, command = self.Deposit_command)
        # Create withdraw_button and lebel with buttons' decription
        self.withdraw_button = tkinter.Button(self.menu_frame, text = "Withdraw", width = 8, command = self.Withdraw_command)
        # Create withdraw_button and lebel with buttons' decription
        self.list_button = tkinter.Button(self.menu_frame, text = "List", width = 8, command = self.List_command)
        # Create exit_button and label with buttons' description
        self.exit_button = tkinter.Button(self.menu_frame, text = "Exit", width = 8, command = self.mainWindow.destroy)


        # Pack objects
        self.records_label.pack(side = 'bottom')
        self.desc_label.pack(side = 'top')
        self.create_button.pack(side = 'top')
        self.delete_button.pack(side = 'top')
        self.deposit_button.pack(side = 'top')
        self.withdraw_button.pack(side = 'top')
        self.list_button.pack(side = 'top')
        self.exit_button.pack(side = 'top')
        
        # Pack all frames
        self.menu_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def Delete_command(self):
        self.newWindow = tkinter.Tk()
        self.app = deleteWindow.DeleteWindowGUI(self.newWindow)           

    def List_command(self):
        self.newWindow = tkinter.Tk()
        self.app = listWindow.ListWindowGUI(self.newWindow)

    def Create_command(self):
        self.newWindow = tkinter.Tk()
        self.app = createWindow.CreateWindowGUI(self.newWindow)

    def Deposit_command(self):
        self.mainWindow.destroy
        self.newWindow = tkinter.Tk()
        self.app = depositWindow.DepositWindowGUI(self.newWindow)


    def Withdraw_command(self):
        self.newWindow = tkinter.Tk()
        self.app = withdrawWindow.WithdrawWindowGUI(self.newWindow)