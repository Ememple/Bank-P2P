from src.protocol.commands.base import Command

class BankCode(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 0:
            return "ER NO ARGUMENTS EXPECTED"
        return f"BC {self.bank.bank_code()}\r"
