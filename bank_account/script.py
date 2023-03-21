from account import BankAccount
from account import MinimumBalanceAccount

user1 = BankAccount()
user2 = BankAccount(7000)

print(user1.deposit(5000))

print(user1.try_withdraw(5500))

print(user1.get_balance())

print(user2)

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(400)

print(result)

if (result.is_ok()):
    print(result.message, result.value)

print(accountMin.deposit(300))

print(accountMin)
