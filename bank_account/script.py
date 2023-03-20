"""

"""

from account import MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(400)

if (result.is_ok()):
    print(result.message)
