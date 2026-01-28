import mysql.connector
from src.storage.StorageStrategy import StorageStrategy
from src.services.Account import Account
import logging

logger = logging.getLogger(__name__)

class MysqlStorage(StorageStrategy):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(MysqlStorage, cls).__new__(cls)
        return cls.instance

    def __init__(self, db_config):
        if not getattr(self, 'initialized', False):
            self.db_config = db_config
            try:
                self._init_db()
                self.initialized = True
            except Exception:
                raise

    def _get_connection(self):
        logger.info('Connecting to MySQL DB')
        return mysql.connector.connect(**self.db_config)

    def _init_db(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            create table if not exists account (
                id int primary key,
                balance int
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()

    def save(self, account: Account):
        logger.info('mysql Saving account')
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = "replace into account (id, balance) values (%s, %s)"
        val = (account.id, account.balance)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()

    def get(self, id: int):
        logger.info('mysql Getting account')
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from account where id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return Account(result[0], result[1])
        return None

    def delete(self, id: int):
        logger.info('mysql Deleting account')
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("delete from account where id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_all(self):
        logger.info('mysql Getting all accounts')
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from account")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return [Account(row[0], row[1]) for row in results]