from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class BankClients(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]) -> str:
        logger.info(f"BN service started")
        if len(args) != 0:
            logger.error(f"BN service takes exactly zero arguments")
            return "ER NO ARGUMENTS EXPECTED"

        count = self.bank.get_accounts_count()
        logger.info(f"BN service ended successfully")
        return f"BN {count}\r"
