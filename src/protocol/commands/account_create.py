from src.protocol.commands.base import Command

class AccountCreate(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 0:
            return "ERROR NO_ARGUMENTS_EXPECTED"

        account_id = self.bank.create_account()
        return f"OK ACCOUNT_CREATED {account_id}"
