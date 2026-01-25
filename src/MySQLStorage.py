import mysql.connector
from src.StorageStrategy import StorageStrategy
from src.Account import Account


class MysqlStorage(StorageStrategy):
    def __init__(self, db_config):
        self.db_config = db_config
        self._init_db()

    def _get_connection(self):
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
        conn = self._get_connection()
        cursor = conn.cursor()
        sql = "replace into account (id, balance) values (%s, %s)"
        val = (account.id, account.balance)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()

    def get(self, id: int):
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
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("delete from account where id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_all(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from account")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return [Account(row[0], row[1]) for row in results]