from src.protocol.commands.base import Command

class AccountWithdraw(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 2:
            return "ERROR MISSING_ARGUMENTS"

        try:
            account_id = int(args[0])
        except ValueError:
            return "ERROR INVALID_ACCOUNT_ID"

        try:
            amount = int(args[1])
        except ValueError:
            return "ERROR INVALID_AMOUNT"

        if amount <= 0:
            return "ERROR AMOUNT_MUST_BE_POSITIVE"

        self.bank.withdraw(account_id, amount)
        return f"OK WITHDREW {amount} FROM ACCOUNT {account_id}"
