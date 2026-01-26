import configparser
import socket
import threading
from src.network.client_handler import ClientHandler

class TCPServer:
    def __init__(self, protocol_handler):
        config = configparser.ConfigParser()
        config.read('../res/config.ini')
        self.timeout = config.get('tcp', 'timeout')
        self.host = config.get('tcp', 'server_bind_ip')
        self.port = config.get('tcp', 'tcp_port')
        self.protocol_handler = protocol_handler
        self.client_handler = ClientHandler
        self.server_socket = None
        self.is_running = False

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.is_running = True

        while self.is_running:
            try:
                conn, address = self.server_socket.accept()
                threading.Thread(
                    target=ClientHandler,
                    args=(conn, self.protocol_handler, self.timeout),
                    daemon=True
                ).start()
            except Exception as e:
                print(e)

    def stop(self):
        self.is_running = False
        if self.server_socket:
            self.server_socket.close()