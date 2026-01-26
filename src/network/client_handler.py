import socket

class ClientHandler:
    def __init__(self, conn: socket.socket, addr, protocol_handler, timeout):
        self.conn = conn
        self.addr = addr
        self.protocol_handler = protocol_handler
        self.is_active = True
        self.conn.settimeout(timeout)


    def run(self):
        try:
            self.conn.sendall(b"CONNECTED TO BANK\n")
            self.send_menu()

            while self.is_active:
                try:
                    data = self.conn.recv(1024)
                    if not data:
                        break
                except socket.timeout:
                    print("closing connection with client {} client timed out".format(self.addr))
                    break

                line = data.decode("utf-8").strip()
                if line.upper() == "QUIT":
                    break

                if not line:
                    continue

                response = self.protocol_handler.handle(line)
                self.conn.sendall((response + "\n").encode("utf-8"))
        finally:
            self.conn.close()


    def send_menu(self):
            menu = """
                Welcome to the P2P Bank!
                Available commands:
            
                AC <account_id>          - Create account
                AD <account_id> <amount> - Deposit
                AW <account_id> <amount> - Withdraw
                AB <account_id>          - Check balance
                AR <account_id>          - Remove account
                BC                       - Bank code
                BA                       - Bank total amount
                BN                       - Number of clients
                RP <number>              - Robbery plan (local only)
                QUIT                     - Disconnect
            """
            self.conn.sendall(menu.encode("utf-8"))

