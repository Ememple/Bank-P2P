from src.services.ReadConfig import ReadConfig
from src.network.tcp_client import TCP_Client
from src.protocol.commands.base import Command
import logging

logger = logging.getLogger(__name__)

class AccountBalance(Command):
    def __init__(self, bank):
        self.bank = bank
        config = ReadConfig.read_tcp_config()
        self.port = config.get('tcp_port',65525)
        self.timeout = config.get('timeout',5)

    def execute(self, args: list[str]):
        logger.info(f"service AB started")
        if len(args) != 1:
            logger.error('Account balance command requires exactly one argument')
            return "ER MISSING ACCOUNT ID"

        arg_parts = args[0].split('/')

        if len(arg_parts) == 2:
            account_id = arg_parts[0]
            target_ip = arg_parts[1]
        elif len(arg_parts) == 1:
            account_id = arg_parts[0]
            target_ip = self.bank.bank_code()
        else:
            logger.error('Account balance command missing ip')
            return "ER INVALID ACCOUNT FORMAT"

        my_ip = self.bank.bank_code()

        if target_ip == my_ip:
            try:
                account_id = int(account_id)
            except ValueError:
                logger.error(f"Account ID {account_id} is not valid")
                return "ER INVALID ACCOUNT ID"

            balance = self.bank.get_balance(account_id)
            logger.info(f"service AB ended successfully")
            return f"AB {balance}\r"

        else:
            client = TCP_Client(self.port, self.timeout)
            command = f"AB {args[0]}"
            response = client.send_command(target_ip, command)
            logger.info(f"service AB ended successfully")
            return response
