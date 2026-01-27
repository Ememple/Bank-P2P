from src.protocol.commands.base import Command

class AccountBalance(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 1:
            return "ER MISSING ACCOUNT ID"
        try:
            account_id = int(args[0])
        except ValueError:
            return "ER INVALID ACCOUNT ID"

        balance = self.bank.get_balance(account_id)
        if not balance and balance != 0:
            return "ER INVALID BALANCE"

        return f"AB {balance}\r"
