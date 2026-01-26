from src.protocol.commands.base import Command

class BankClients(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]) -> str:
        if len(args) != 0:
            return "ERROR NO_ARGUMENTS_EXPECTED"

        count = self.bank.get_accounts_count()
        return str(count)
