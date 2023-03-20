"""
The bank account will have following functionalities:
1. Checking balance.
2. Deposit money.
3. Withdraw money.

"""
from result import Ok, Error


class BankAccount:
    """Creates the bank account object.
    You can check balance and deposit/withdraw money.
    """

    def __init__(self, balance: int = 0):
        self.balance = balance

    def get_balance(self) -> str:
        return "Your current balance is: " + str(self.balance)

    def deposit(self, amountOfMoney) -> str:
        self.balance += amountOfMoney
        return "Your current balance is: " + str(self.balance)

    def try_withdraw(self, amountOfMoney) -> str:
        if self.balance >= amountOfMoney:
            self.balance -= amountOfMoney
            return Ok("The following amount of cash has been paid out", amountOfMoney)

        return Error("Too little cash", amountOfMoney)

    def __str__(self):
        return "Account balance: " + str(self.balance) + "\n"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def deposit(self, amountOfMoney) -> str:
        self.balance += amountOfMoney
        return "Your current balance is: " + str(self.balance)

    def try_withdraw(self, amountOfMoney) -> str:
        if self.balance - amountOfMoney >= self.minimumBalance:
            return super().try_withdraw(amountOfMoney)
        else:
            return Error("Failed, attempt to cross the threshold", amountOfMoney)

    def __str__(self):
        return "Account balance: " + str(self.balance) + "\n"
