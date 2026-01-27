from src.ReadConfig import ReadConfig
from src.TCP_Client import TCP_Client
from src.protocol.commands.base import Command

class AccountRemove(Command):
    def __init__(self, bank):
        self.bank = bank
        config = ReadConfig.read_tcp_config()
        self.port = config.get('tcp_port', 65525)
        self.timeout = config.get('timeout', 5)

    def execute(self, args: list[str]):
        if len(args) != 1:
            return "ER MISSING_ACCOUNT_ID"

        account_str = args[0]

        if '/' in account_str:
            id_str, target_ip = account_str.split('/')
        else:
            id_str = account_str
            target_ip = self.bank.bank_code()

        my_ip = self.bank.bank_code()
        if target_ip == my_ip:
            try:
                account_id = int(id_str)
            except ValueError:
                return "ER INVALID ACCOUNT ID"

            try:
                self.bank.remove_account(account_id)
                return "AR\r"
            except ValueError as e:
                return f"ER {e}\r"
            except Exception as e:
                return f"ER LOCAL ERROR {e}\r"

        # 3. Proxy
        else:
            client = TCP_Client(self.port, self.timeout)
            command = f"AR {account_str}"
            return client.send_command(target_ip, command)
