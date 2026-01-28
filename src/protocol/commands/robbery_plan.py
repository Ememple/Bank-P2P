from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class RobberyPlan(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        logger.info(f"RP service started")
        if len(args) != 1:
            logger.error(f"RobberyPlan takes exactly 1 argument")
            return "ERROR MISSING_ARGUMENT"

        try:
            number = int(args[0])
        except ValueError:
            logger.error(f"RobberyPlan takes exactly 1 argument")
            return "ERROR INVALID_NUMBER"

        if number <= 0:
            logger.error(f"RobberyPlan service targets number is invalid")
            return "ERROR NUMBER_MUST_BE_POSITIVE"

        targets_count = self.bank.get_accounts_count()
        plan_summary = ", ".join(f"{acc.id}:{acc.balance}" for acc in targets_count)
        logger.info(f"RP ended successfully")
        return f"RP PLAN {plan_summary}"
