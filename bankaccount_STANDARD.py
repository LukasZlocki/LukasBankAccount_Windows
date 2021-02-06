# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

import bankaccount

class BankAccount_STANDARD(bankaccount.BankAccount):
     # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):
        # init superclass
        bankaccount.BankAccount.__init__(self, bal, na, acctnb)

        # init date attribute
        self.__initdate = initdate
        self.__acctype = "Standard bank account"
        self.__Log = " "


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

    # The classLog method is returning class log. 
    # (Overrided) due to different Covid19 rules
    def get_classLog(self):
        return self.__Log
            
            

    