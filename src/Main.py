from src.ReadConfig import ReadConfig
from src.MySQLStorage import MysqlStorage
from src.JsonStorage import JsonStorage
from src.Bank import Bank


def get_storage_strategy():
    try:
        config = ReadConfig.read_config()

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
    try:
        new_id = bank.create_account()
        print(f"Created Account ID: {new_id}")

        bank.deposit(new_id, 1000)
        print(f"Deposited 1000, new balance: {bank.get_balance(new_id)}")

        bank.withdraw(new_id, 200)
        print(f"Withdrew 200, new balance: {bank.get_balance(new_id)}")

        print(f"Total bank balance: {bank.get_total_balance()}")
        print(f"Total clients: {bank.get_accounts_count()}")

    except Exception as e:
        print(f"An error occurred during testing: {e}")


if __name__ == "__main__":
    main()