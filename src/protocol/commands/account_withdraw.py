from src.protocol.commands.base import Command

class AccountWithdraw(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 2:
            return "ER MISSING ARGUMENTS"

        try:
            account_id = int(args[0])
        except ValueError:
            return "ER INVALID ACCOUNT ID"

        try:
            amount = int(args[1])
        except ValueError:
            return "ER INVALID AMOUNT"

        if amount <= 0:
            return "ER AMOUNT MUST BE POSITIVE"

        self.bank.withdraw(account_id, amount)
        return "AW\r"
