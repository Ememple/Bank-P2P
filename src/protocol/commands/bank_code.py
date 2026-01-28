from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class BankCode(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        logger.info(f"BC service started")
        if len(args) != 0:
            logger.error(f"BN service takes exactly zero arguments")
            return "ER NO ARGUMENTS EXPECTED"
        logger.info(f"BC service ended successfully")
        return f"BC {self.bank.bank_code()}\r"
