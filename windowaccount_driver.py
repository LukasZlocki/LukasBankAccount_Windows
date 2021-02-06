# Banking task by Lukasz Zlocki / 76103
# tkinter base Windows version
# zlocki_76103@cloud.wsb.wroclaw.pl

import mainWindow_gui as win
import tkinter as tk


def main():

    root = tk.Tk()

    # ---------------- CALCULATE SCREEN RESOLUTION ----------------
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)  
    # Gets both half the screen width/height and window width/height
    posR = int(root.winfo_screenwidth()/2 - windowWidth/2)
    posD = int(root.winfo_screenheight()/2 - windowHeight/2)

    app = win.MainWindowGUI(root, posR, posD)
    root.mainloop() 





# Call main function
if __name__ == "__main__":
    main()  