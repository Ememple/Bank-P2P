from src.protocol.commands.base import Command
import socket

class AccountCreate(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 0:
            return "ER NO ARGUMENTS EXPECTED"


        account_id = self.bank.create_account()
        return f"AC {account_id}/{self.bank.bank_code()}\r"
