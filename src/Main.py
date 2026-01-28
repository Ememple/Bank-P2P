import socket
from src.ReadConfig import ReadConfig
from src.MySQLStorage import MysqlStorage
from src.JsonStorage import JsonStorage
from src.Bank import Bank
from src.network.tcp_server import TCPServer
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename="actions_log.log",
    filemode="a",
)

def get_storage_strategy():
    try:
        config = ReadConfig.read_database_config()

        storage = MysqlStorage(config)
        print("Using Database storage")
        return storage

    except Exception as e:
        print(f"Database connection failed ({e})")
        print("Using JSON storage")
        return JsonStorage()


def main():
    storage = get_storage_strategy()
    bank = Bank(storage)

    tcp_config = ReadConfig.read_tcp_config()

    timeout = tcp_config.get("timeout",5)
    tcp_port = tcp_config.get("tcp_port",65525)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    server = TCPServer(host=ip_address, port=tcp_port, timeout=timeout, bank=bank)

    try:
        print(f"Starting TCP server on {ip_address}:{tcp_port}")
        server.start()
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop()


if __name__ == "__main__":
    main()