from src.protocol.commands.base import Command

class BankCode(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 0:
            return "ERROR NO_ARGUMENTS_EXPECTED"

        return NotImplemented
