from src.services.ReadConfig import ReadConfig
from src.network.tcp_client import TCP_Client
from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class AccountDeposit(Command):
    def __init__(self, bank):
        self.bank = bank
        config = ReadConfig.read_tcp_config()
        self.port = config.get('tcp_port', 65525)
        self.timeout = config.get('timeout', 5)

    def execute(self, args: list[str]) -> str:
        logger.info(f"service AD started")
        if len(args) != 2:
            logger.error('Account deposit command requires exactly two arguments')
            return "ER MISSING ARGUMENTS"

        account_str = args[0]
        amount_str = args[1]

        if '/' in account_str:
            id_str, target_ip = account_str.split('/')
        else:
            id_str = account_str
            target_ip = self.bank.bank_code()

        try:
            amount = int(amount_str)
            if amount <= 0:
                logger.error('Account deposit amount must be greater than zero')
                return "ER AMOUNT MUST BE POSITIVE"
        except ValueError:
            logger.error('Account deposit amount must be an integer')
            return "ER INVALID AMOUNT"

        my_ip = self.bank.bank_code()

        if target_ip == my_ip:
            try:
                account_id = int(id_str)
            except ValueError:
                logger.error('Account deposit id must be an integer')
                return "ER INVALID ACCOUNT ID"

            try:
                self.bank.deposit(account_id, amount)
                logger.info(f"AD service ended successfully")
                return "AD\r"
            except ValueError as e:
                logger.error(f"AD service ended with error: {e}")
                return f"ER {e}\r"

        # PROXY
        else:
            client = TCP_Client(self.port, self.timeout)
            command = f"AD {account_str} {amount}"
            logger.info(f"AD service ended successfully")
            return client.send_command(target_ip, command)
