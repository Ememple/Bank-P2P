from src.protocol.commands.base import Command

class BankTotal(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 0:
            return "ER NO ARGUMENTS EXPECTED"

        total = self.bank.get_total_balance()

        if not total and total != 0:
            return "ER TOTAL BALANCE"

        return f"BA {total}\r"
