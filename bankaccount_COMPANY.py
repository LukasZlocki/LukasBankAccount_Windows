# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

import bankaccount
from datetime import date

class BankAccount_COMPANY(bankaccount.BankAccount):
    # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):

        # init date attribute
        self.__initdate = initdate
        self.__acctype = "Company bank account"
        self.__Log = " "

        # Covid19 Rule : from 01.04.2019 +1 k PLN init loan for all COMPANY accounts.
        covid19_loan_date = date(2019, 4, 1)
        if initdate >= covid19_loan_date:
            bal = bal + 5000
            self.__Log = "Government support : 5 k pln."

        # init superclass
        bankaccount.BankAccount.__init__(self, bal, na, acctnb)
   

    # -- Overrided methods --

    # Get account type
    def get_acctype(self):
        return self.__acctype

    # The withdraw method withdraws an amount from the account.
    # (Overrided) Covid19 rule : withdraw not more than 1 k pln
    def withdraw(self, amount):
        if amount > 1000 :
            print("Too large amount of money. Withdraw max 1000 pln")
            self.__Log = "Too large amount of money. Withdraw max 1000 pln"
        else :
            if self.get_balance() >= amount:
                new_balans = self.get_balance() - amount
                self.set_balance(new_balans)
                print("... Amount withdrawn.")
                self.__Log = "... Amount withdrawn."

            else:
                print('Error: Insufficient funds')
                self.__Log = "Error: Insufficient funds"

    # The close method is closing account 
    # (Overrided) Covid19 rule : company account not allowed to close
    def close(self, accounts_list, id):
        print('Deleting company account not allowed')
        self.__Log = "Deleting company account not allowed"

    # The classLog method is returning class log. 
    # (Overrided) due to different Covid19 rules
    def get_classLog(self):
        return self.__Log
       
