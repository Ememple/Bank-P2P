from src.ReadConfig import ReadConfig
from src.TCP_Client import TCP_Client
from src.protocol.commands.base import Command

class AccountBalance(Command):
    def __init__(self, bank):
        self.bank = bank
        config = ReadConfig.read_tcp_config()
        self.port = config.get('tcp_port',65525)
        self.timeout = config.get('timeout',5)

    def execute(self, args: list[str]):
        if len(args) != 1:
            return "ER MISSING ACCOUNT ID"

        arg_parts = args[0].split('/')

        if len(arg_parts) == 2:
            account_id = arg_parts[0]
            target_ip = arg_parts[1]
        elif len(arg_parts) == 1:
            account_id = arg_parts[0]
            target_ip = self.bank.bank_code()
        else:
            return "ER INVALID ACCOUNT FORMAT"

        my_ip = self.bank.bank_code()

        if target_ip == my_ip:
            try:
                account_id = int(account_id)
            except ValueError:
                return "ER INVALID ACCOUNT ID"

            balance = self.bank.get_balance(account_id)
            return f"AB {balance}\r"

        else:
            client = TCP_Client(self.port, self.timeout)
            command = f"AB {args[0]}"
            response = client.send_command(target_ip, command)
            return response
