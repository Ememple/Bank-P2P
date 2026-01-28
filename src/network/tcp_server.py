import socket
import threading
from src.network.client_handler import ClientHandler
from src.protocol.dispatcher import Dispatcher
from src.protocol.protocol_handler import ProtocolHandler
import logging

logger = logging.getLogger(__name__)

class TCPServer:
    def __init__(self, host, port, timeout, bank):
        self.client_handler = ClientHandler
        self.timeout = int(timeout)
        self.host = host
        self.port = int(port)
        self.server_socket = None
        self.is_running = False

        self.bank = bank
        self.dispatcher = Dispatcher(self.bank)
        self.protocol_handler = ProtocolHandler(self.dispatcher)

    def start(self):
        logger.info("Starting TCP server")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.is_running = True

        while self.is_running:
            try:
                connection, address = self.server_socket.accept()
                threading.Thread(target=self._redirect_to_handler, args=(connection, address), daemon=True).start()
            except Exception as e:
                print(e)

    def _redirect_to_handler(self, conn, address):
        logger.info(f"client {address} has connected")
        handler = (self.client_handler(conn, address, self.timeout, self.protocol_handler))
        handler.run()

    def stop(self):
        logger.info("Stopping TCP server")
        self.is_running = False
        if self.server_socket:
            self.server_socket.close()