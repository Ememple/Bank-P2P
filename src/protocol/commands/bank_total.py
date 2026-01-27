from src.protocol.commands.base import Command

class BankTotal(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 0:
            return "ERROR NO_ARGUMENTS_EXPECTED"

        total = self.bank.get_total_balance()

        if not total and total != 0:
            return "ERROR TOTAL BALANCE"

        return str(total)
