# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# Purpose of the class is to handle directly with db, main tasks like LOAD database, SAVE database, return database as a list

import pickle

accounts_list = []


# Data base adapter
class IoAdapter:


    def loadDataFromDatabase(self):
        __FILENAME = 'accountDb.dat'
        global accounts_list
        print("-- Loading accounts from data base --") 
        # Clearing all data in list
        accounts_list.clear()
        eof = False #End of file indicator
        try:
            # Open the binary file
            db_file = open(__FILENAME, 'rb')
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
        return accounts_list



    # Save data to file function
    def saveDataToDatabase(self, accounts_list):
        __FILENAME = 'accountDb.dat'
        print("-- Savings accounts --")     
        # Opening file
        db_file = open(__FILENAME, 'wb')  
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

        # Set data to class field
        self.__Accounts_List = accounts_list

    
    # ---- GETTERS ----

    def getDataBase(self):
        global accounts_list
        # Load fresh data base to list -- ale wyglada ze to jest nie potrzebne , zaciaga z global 
        #accounts_list = self.loadDataFromDatabase()
        # Return list with accounts
        return accounts_list