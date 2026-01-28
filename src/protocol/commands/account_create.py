from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class AccountCreate(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        logger.info(f"service AC started")
        if len(args) != 0:
            logger.error('Account creation command requires exactly no arguments')
            return "ER NO ARGUMENTS EXPECTED"

        account_id = self.bank.create_account()
        logger.info(f"service AC ended successfully")
        return f"AC {account_id}/{self.bank.bank_code()}\r"
