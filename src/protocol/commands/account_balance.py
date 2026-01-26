from src.protocol.commands.base import Command

class AccountBalance(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 1:
            return "ERROR MISSING_ACCOUNT_ID"
        try:
            account_id = int(args[0])
        except ValueError:
            return "ERROR INVALID_ACCOUNT_ID"

        balance = self.bank.get_balance(account_id)
        if not balance:
            return "ERROR BALANCE"

        return str(balance)
