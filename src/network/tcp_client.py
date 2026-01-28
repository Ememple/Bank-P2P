import socket
import logging

logger = logging.getLogger(__name__)

class TCP_Client:
    def __init__(self, port, timeout=5):
        self.port = int(port)
        self.timeout = int(timeout)

    def send_command(self, target_ip, command_str):
        try:
            logger.info("communications with other banks start")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                s.connect((target_ip, self.port))

                if not command_str.endswith("\n"):
                    command_str += "\n"
                s.sendall(command_str.encode('utf-8'))

                data = s.recv(4096)
                if not data:
                    logger.warning("remote server didn't respond")
                    return "ER EMPTY RESPONSE FROM REMOTE"
                logger.info("remote server responded with data ending communication")
                return data.decode('utf-8').strip()

        except socket.timeout:
            logger.error("remote server timed out")
            return "ER TIMEOUT REMOTE BANK"
        except ConnectionRefusedError:
            logger.error("remote server refused connection")
            return "ER CONNECTION REFUSED REMOTE BANK"
        except Exception as e:
            logger.error(f"proxy error: {e}")
            return f"ER PROXY ERROR {e}"