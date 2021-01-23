# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

import Io_adapter

import bankaccount
import bankaccount_STANDARD
import bankaccount_COMPANY
import bankaccount_INT

# Data base adapter
class dbAdapter:
    def __init__(self):
        self.__Accounts_List = []
    
    # --- DELETE ACCOUNT ---
    # Delete account function with withdraw all money
    def deleteAccountFromDatabase(self, account_number):
        print("-- Delete account --")
        # get list with bank accounts
        accounts_list = Io_adapter.getDataBase()
        _account_found = False
        _account_deleted = 0
        id = 0
        for account in accounts_list: 
            if account.get_accountNb() == account_number:
                account.close(accounts_list, id)
                _account_found = True
                # Saving updated data
               Io_adapter.IoAdapter.saveDataToDatabase(accounts_list)        
            else:
                id = id +1
        if _account_found == False:
            print("No account number " + str(account_number) + " found.")               



