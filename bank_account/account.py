"""
The package is a quasi bank account application.
You can create objects based on defined classes,
which represents two types of accounts.
Each account type has features
that allow you to perform the following operations:
1. Checking balance.
2. Deposit money.
3. Withdraw money.
The try_withdraw function returns objects
created based on classes defined in result.py module.
The objects contain attributes with boolean values regards to
whatever there was success when trying to withdraw funds or not.
The subclass MinimumBalanceAccount inherits from the superclass BankAccount.
It's a special kind of BankAccount class
where the minimum balance needs to be maintained.

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
            return Ok("The following amount of cash\
 has been paid out:", amountOfMoney)

        return Error("Account balance is too low to withdraw:", amountOfMoney)

    def __str__(self):
        return "Account balance: " + str(self.balance)


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
            return Error("Failed, the minimum account balance will be exceeded\
 when attempting to withdraw:", amountOfMoney)

    def __str__(self):
        return "Account balance: " + str(self.balance)
