import socket

class TCP_Client:
    def __init__(self, port, timeout=5):
        self.port = int(port)
        self.timeout = int(timeout)

    def send_command(self, target_ip, command_str):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                s.connect((target_ip, self.port))

                if not command_str.endswith("\n"):
                    command_str += "\n"
                s.sendall(command_str.encode('utf-8'))

                data = s.recv(4096)
                if not data:
                    return "ER EMPTY RESPONSE FROM REMOTE"

                return data.decode('utf-8').strip()

        except socket.timeout:
            return "ER TIMEOUT REMOTE BANK"
        except ConnectionRefusedError:
            return "ER CONNECTION REFUSED REMOTE BANK"
        except Exception as e:
            return f"ER PROXY ERROR {e}"