class Bank:
    bank_name = "ICICI Bank"

    def __init__(self, name, balance, ifsc, acno):
        self._account_no = acno
        self.account_name = name
        self.__ifsc_code = ifsc
        self.acc_balance = balance

    def get_details(self):
        print(f"account_no: {self._account_no}")
        print(f"account_name: {self.account_name}")
        print(f"ifsc_code: {self.__ifsc_code}")
        print(f"account_balance: {self.acc_balance}")

    def balance(self):
        print(f"Current balance: {self.acc_balance}")

    def withdraw(self, amt):
        if amt > self.acc_balance:
            print("Insufficient balance")
        else:
            self.acc_balance -= amt
            print(f"Balance after withdrawal: {self.acc_balance}")

    def deposit(self, amt):
        self.acc_balance += amt
        print(f"New balance: {self.acc_balance}")

shony_ac = Bank("shony", 1010, "icici0001", 5000)

shony_ac.get_details()

shony_ac.withdraw(200)

shony_ac.deposit(500)

shony_ac.balance()

