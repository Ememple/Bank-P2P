import socket
import logging

logger = logging.getLogger(__name__)

class ClientHandler:
    def __init__(self, conn: socket.socket, addr, timeout, protocol_handler):
        self.conn = conn
        self.addr = addr
        self.protocol_handler = protocol_handler
        self.is_active = True
        self.conn.settimeout(timeout)

    def run(self):
        try:
            #self.conn.sendall(b"CONNECTED TO BANK\n")
            #self.send_menu()

            while self.is_active:
                try:
                    data = self.conn.recv(1024)
                    if not data:
                        break
                except socket.timeout:
                    logger.error(f"client {self.addr} Timed out")
                    print("closing connection with client {} client timed out".format(self.addr))
                    break

                line = data.decode("utf-8").strip()
                if line.upper() == "QUIT":
                    logger.info(f"client {self.addr} has closed the connection")
                    break

                if not line:
                    continue

                response = self.protocol_handler.handle(str(line))
                self.conn.sendall((response + "\n").encode("utf-8"))
        finally:
            logger.info("closing connection with client {} client timed out".format(self.addr))
            self.conn.close()


    def send_menu(self):
        menu_lines = [
            "Welcome to the P2P Bank!",
            "",
            "Available commands:",
            "-----------------------------------------------------",
            "AC                             - Create account",
            "AD <account>/<ip> <amount>     - Deposit",
            "AW <account_id>//<ip> <amount> - Withdraw",
            "AB <account_id>/<ip>           - Check balance",
            "AR <account_id>/<ip>           - Remove account",
            "BC                             - Bank code",
            "BA                             - Bank total amount",
            "BN                             - Number of clients",
            "RP <number>                    - Robbery plan (local only), (not implemented yet)",
            "QUIT                     - Disconnect"
        ]
        menu = "\r\n".join(menu_lines) + "\r\n"
        self.conn.sendall(menu.encode("utf-8"))

