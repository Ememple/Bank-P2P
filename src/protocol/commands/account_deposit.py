from src.protocol.commands.base import Command

class AccountDeposit(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]) -> str:
        if len(args) != 2:
            return "ER MISSING_ARGUMENTS"

        try:
            account_id = int(args[0])
        except ValueError:
            return "ER INVALID_ACCOUNT_ID"

        try:
            amount = int(args[1])
        except ValueError:
            return "ER INVALID_AMOUNT"

        if amount <= 0:
            return "ER AMOUNT MUST BE POSITIVE"

        self.bank.deposit(account_id, amount)

        return "AD\r"
