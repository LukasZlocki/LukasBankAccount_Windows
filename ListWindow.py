# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import tkinter
import db_adapter
import bankaccount

class ListWindowGUI:
    def __init__(self, listWindow):
        # Create the delete window 
        self.listWindow = listWindow
        self.listWindow.geometry("200x350")
        self.listWindow.title("Lucas Bank Account - List")
       
        # Creating frames
        self.buttonLeft_frame = tkinter.Frame(self.listWindow)
        self.buttonRight_frame = tkinter.Frame(self.listWindow)
        self.labelLeft_frame = tkinter.Frame(self.listWindow)
        self.labelRight_frame = tkinter.Frame(self.listWindow)
        self.buttonLeft_frame.grid(row = 0, column = 0)
        self.buttonRight_frame.grid(row = 0, column = 1)
        self.labelLeft_frame.grid(row = 1, column = 0)
        self.labelRight_frame.grid(row = 1, column = 1)
        
        # ---------------- B U T T O N S ----------------
        # Create create_button and lebel with buttons' decription
        self.forward_button = tkinter.Button(self.buttonRight_frame, text = "-->", width = 8)
        self.backward_button = tkinter.Button(self.buttonLeft_frame, text = "<--", width = 8)

        # ---------------- L A B E L S ----------------
        # Create Labels with descriptions
        self.desc_label1 = tkinter.Label(self.labelLeft_frame, text = 'Account number   :')
        self.desc_label2 = tkinter.Label(self.labelLeft_frame, text = 'Account type     :')
        self.desc_label3 = tkinter.Label(self.labelLeft_frame, text = 'Account owner    :')
        self.desc_label4 = tkinter.Label(self.labelLeft_frame, text = 'Account balancer :')
        # Create Labels with database data
        self.db_label1 = tkinter.Label(self.labelRight_frame, text = '1234')
        self.db_label2 = tkinter.Label(self.labelRight_frame, text = 'Standard')
        self.db_label3 = tkinter.Label(self.labelRight_frame, text = 'Lukasek')
        self.db_label4 = tkinter.Label(self.labelRight_frame, text = '54')

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