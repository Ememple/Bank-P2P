from src.protocol.commands.account_balance import AccountBalance
from src.protocol.commands.account_create import AccountCreate
from src.protocol.commands.account_deposit import AccountDeposit
from src.protocol.commands.account_remove import AccountRemove
from src.protocol.commands.account_withdraw import AccountWithdraw
from src.protocol.commands.bank_clients import BankClients
from src.protocol.commands.bank_code import BankCode
from src.protocol.commands.bank_total import BankTotal
from src.protocol.commands.robbery_plan import RobberyPlan
import logging

logger = logging.getLogger(__name__)

class Dispatcher:
    def __init__(self, bank):
        self.bank = bank
        self.commands = {
            "AC": AccountCreate(bank),
            "AD": AccountDeposit(bank),
            "AW": AccountWithdraw(bank),
            "AB": AccountBalance(bank),
            "AR": AccountRemove(bank),
            "BC": BankCode(bank),
            "BA": BankTotal(bank),
            "BN": BankClients(bank),
            "RP": RobberyPlan(bank)
        }

    def dispatch(self, code: str, args: list[str]):
        if code not in self.commands:
            logger.warning(f"unknown command: {code} launched by client")
            raise KeyError(code)
        return self.commands[code].execute(args)
