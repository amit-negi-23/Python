# Practice Question

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, debit_amt):
        self.balance-=debit_amt
        print("Rs.", debit_amt, "was debited")
        print("total balance =", self.get_balance())

    def credit(self, credit_amt):
        self.balance+=credit_amt
        print("Rs.", credit_amt, "was credited")
        print("total balance =", self.get_balance())
    
    def get_balance(self):
        return self.balance


acc1 = Account(5000, 59085591419)
acc1.debit(500)
acc1.credit(1000)

print(acc1.get_balance())