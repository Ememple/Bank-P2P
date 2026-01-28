from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class BankTotal(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        logger.info(f"BA service started")
        if len(args) != 0:
            logger.error(f"BA service takes no arguments")
            return "ER NO ARGUMENTS EXPECTED"

        total = self.bank.get_total_balance()

        if not total and total != 0:
            logger.error(f"BA service total balance error")
            return "ER TOTAL BALANCE"

        logger.info(f"BA service ended successfully")
        return f"BA {total}\r"
