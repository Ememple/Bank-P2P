import socket

class ClientHandler:
    def __init__(self, conn: socket.socket, addr, protocol_handler, timeout):
        self.conn = conn
        self.addr = addr
        self.protocol_handler = protocol_handler
        self.timeout = timeout
        self.is_active = True
        self.conn.settimeout(self.timeout)

    def run(self):
        try:
            self.conn.sendall(b"CONNECTED TO BANK\n")
            while self.is_active:
                try:
                    data = self.conn.recv(1024)
                    if not data:
                        break
                except socket.timeout:
                    print("closing connection with client {} client timed out".format(self.addr))
                    break

                line = data.decode("utf-8").strip()
                if not line:
                    continue

                try:
                    response = self.protocol_handler.handle(line)
                except Exception as e:
                    response = f"ERR {e}"

                self.conn.sendall((response + "\n").encode("utf-8"))
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
            print("closing connection with client {}".format(self.addr))

