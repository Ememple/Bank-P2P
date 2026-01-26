from src.protocol.commands.base import Command

class RobberyPlan(Command):
    def __init__(self, bank):
        self.bank = bank

    def execute(self, args: list[str]):
        if len(args) != 1:
            return "ERROR MISSING_ARGUMENT"

        try:
            number = int(args[0])
        except ValueError:
            return "ERROR INVALID_NUMBER"

        if number <= 0:
            return "ERROR NUMBER_MUST_BE_POSITIVE"

        targets_count = self.bank.get_accounts_count()
        plan_summary = ", ".join(f"{acc.id}:{acc.balance}" for acc in targets_count)

        return f"RP PLAN {plan_summary}"
