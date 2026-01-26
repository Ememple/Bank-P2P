import socket
import threading
from src.network.client_handler import ClientHandler

class TCPServer:
    def __init__(self, host, port, timeout, protocol_handler):
        self.protocol_handler = protocol_handler
        self.client_handler = ClientHandler
        self.timeout = timeout
        self.host = host
        self.port = port
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
                    target=self.client_handler,
                    args=(conn, self.protocol_handler, self.timeout),
                    daemon=True
                ).start()
            except Exception as e:
                print(e)

    def stop(self):
        self.is_running = False
        if self.server_socket:
            self.server_socket.close()