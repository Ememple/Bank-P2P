from src.protocol.commands.base import Command

class AccountRemove(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 1:
            return "ER MISSING_ACCOUNT_ID"

        try:
            account_id = int(args[0])
        except ValueError:
            return "ER INVALID_ACCOUNT_ID"

        self.bank.remove_account(account_id)
        return "AR\r"
