# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import mainWindow_gui as win
import tkinter as tk


def main():

    root = tk.Tk()
    app = win.MainWindowGUI(root)
    root.mainloop() 





# Call main function
if __name__ == "__main__":
    main()  