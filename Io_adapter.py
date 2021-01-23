# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

import pickle




class IoAdapter:
    def __init__(self):
        self.__FILENAME = "accountDb.dat"
        self.__Accounts_List = []
    

    
    def LoadDb(self):
        accounts_list = []
        print("-- Loading accounts from data base --") 
        # Clearing all data in list
        accounts_list.clear()
        eof = False #End of file indicator
        try:
            # Open the binary file
            db_file = open(self.__FILENAME, 'rb')
            # Reat up to the end of file
            while not eof:
                try:
                    #Unpickle the next object
                    account = pickle.load(db_file)
                    accounts_list.append(account)
                except EOFError:
                    # Set the flag of and of file
                    eof = True
            # Close the file
            db_file.close()
            print("... Accounts loaded to list.")
        except:
            print("No file found. Create account first.")
        
        # Set data to class field
        self.__Accounts_List = accounts_list


    # Save data to file function
    def saveData(self, accounts_list):
        print("-- Savings accounts --")     
        # Opening file
        db_file = open(self.__FILENAME, 'wb')  
        # Logic data for while loop
        loop = len(accounts_list)
        i = 0
        while not i == loop :   
            # Write i object to file
            pickle.dump(accounts_list[i], db_file)
            i = i + 1          
        # Close file
        db_file.close()
        print("... Accounts list updated to file.")


    # ---- GETTERS ----
    
    def getDataBase(self):
        return self.__Accounts_List
