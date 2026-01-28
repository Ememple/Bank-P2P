import configparser
import logging

logger = logging.getLogger(__name__)

class ReadConfig:

    @staticmethod
    def read_database_config():
        config = configparser.ConfigParser()
        config.read('../res/config.ini')

        db_host = config.get('database', 'db_host')
        db_port = config.get('database', 'db_port')
        db_name = config.get('database', 'db_name')
        db_user = config.get('database', 'db_user')
        db_password = config.get('database', 'db_password')

        config_values = {
            'host': db_host,
            'port': db_port,
            'database': db_name,
            'user': db_user,
            'password': db_password
        }

        return config_values

    @staticmethod
    def read_tcp_config():
        config = configparser.ConfigParser()
        config.read('../res/config.ini')

        timeout = config.get('tcp', 'timeout')
        tcp_port = config.get('tcp', 'tcp_port')

        if not 65525 <= int(tcp_port) <= 65535:
            logger.error('tcp port must be in range [65525-65535]')
            tcp_port = 65525

        config_values = {
            'timeout': timeout,
            'tcp_port': tcp_port
        }

        return config_values