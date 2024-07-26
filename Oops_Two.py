class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private attribute

    def show_pass(self):
        print(self.__acc_pass)


acc1 = Account(2181, "abcd@123")

print(acc1.acc_no)
# print(acc1.acc_pass)          # cannot access acc_pass directly
acc1.show_pass()