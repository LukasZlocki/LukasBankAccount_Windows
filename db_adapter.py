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
        self.__Accounts_List = Io_adapter.IoAdapter.loadDataFromDatabase(self)

        global Acc_List
        Acc_List = Io_adapter.IoAdapter.loadDataFromDatabase(self) 


    # --- CREATE ACCOUNT ---   
    def createAccount(self, accType, accNb, accName, accBal, accInit):       
        if accType == 'CO':
            # Create an COMPANY account object
            newAccount = bankaccount_COMPANY.BankAccount_COMPANY(accBal, accName, accNb, accInit) 
        if accType  == 'INT':
            # Create an INTERNATIONAL account object
            newAccount = bankaccount_INT.BankAccount_INT(accBal, accName, accNb, accInit) 
        if accType  == 'ST':
            # Create an STANDARD account object
            newAccount = bankaccount_STANDARD.BankAccount_STANDARD(accBal, accName, accNb, accInit) 

        # Add object to list of accounts
        #self.__Accounts_List.append(newAccount)
        Acc_List.append(newAccount)
        print("... Account added to list.")

        # Save accounts list to file
        Io_adapter.IoAdapter.saveDataToDatabase(self, Acc_List)



    # --- DELETE ACCOUNT ---
    # Delete account function with withdraw all money
    def deleteAccountFromDatabase(self, account_number):
        print("-- Delete account --")
        # get list with bank accounts
        accounts_list = Io_adapter.IoAdapter.getDataBase(self)
        _account_found = False
        _account_deleted = 0
        id = 0
        for account in accounts_list: 
            if account.get_accountNb() == int(account_number):
                account.close(accounts_list, id)
                _account_found = True
                # Saving updated data
                Io_adapter.IoAdapter.saveDataToDatabase(self, accounts_list)        
            else:
                id = id +1
        if _account_found == False:
            print("No account number " + str(account_number) + " found.")               

    # Update account database by account object
    def updateDatabase(self, account):
        _acc_list = self.__Accounts_List
        for acc in _acc_list:
            if acc.get_accountNb() == account.get_accountNb():
                # updating account list
                acc.set_balance(account.get_balance())
        # updating database
        Io_adapter.IoAdapter.saveDataToDatabase(self, _acc_list)

    # ---- GETTERS ---

    # returns bankaccount object by account number
    def getAccountDataByAccountNumber(self, accNumber):
        for account in self.__Accounts_List:
            if account.get_accountNb() == accNumber:
                return account


    # Returns bankaccount object object by position in list
    def getRecordByPossitionInList(self,possitionInList):
        accountData = self.__Accounts_List[possitionInList]
        return accountData

    # Returns records quantity
    def getRecordsNumber(self):
        recordsNumber = len(self.__Accounts_List)
        return recordsNumber
