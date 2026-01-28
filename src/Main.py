import socket, Server, threading
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
    encoding="utf-8",
)

def get_storage_strategy():
    try:
        config = ReadConfig.read_database_config()

        storage = MysqlStorage(config)
        print("Using Database storage")
        return storage

    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Using JSON storage")
        return JsonStorage()

def run_web_server():
    Server.app.run(port=8080, debug=False, use_reloader=False)

def main():
    storage = get_storage_strategy()
    bank = Bank(storage)
    Server.bank = bank

    web_thread = threading.Thread(target=run_web_server)
    web_thread.start()

    tcp_config = ReadConfig.read_tcp_config()

    timeout = tcp_config.get("timeout",5)
    tcp_port = tcp_config.get("tcp_port",65525)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    server = TCPServer(host=ip_address, port=tcp_port, timeout=timeout, bank=bank)
    Server.tcp_server_instance = server

    try:
        print(f"Starting TCP server on {ip_address}:{tcp_port}")
        server.start()
    except KeyboardInterrupt:
        print("Server shutdown")
        server.stop()


if __name__ == "__main__":
    main()