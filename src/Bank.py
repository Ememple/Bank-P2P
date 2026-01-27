import random
import socket
from src.StorageStrategy import StorageStrategy
from src.Account import Account


class Bank:
    def __init__(self, repository: StorageStrategy):
        self.repo = repository

    def bank_code(self) :
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def create_account(self) :
        while True:
            new_id = random.randint(10000, 99999)
            if self.repo.get(new_id):
                continue

            new_account = Account(new_id, 0)
            try:
                self.repo.save(new_account)
                return new_id
            except Exception as e:
                continue

    def deposit(self, account_id: int, amount: int):
        account = self.repo.get(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")

        account.balance += amount
        self.repo.save(account)

    def withdraw(self, account_id: int, amount: int):
        account = self.repo.get(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")

        if account.balance < amount:
            raise ValueError("Insufficient balance")

        account.balance -= amount
        self.repo.save(account)

    def get_balance(self, account_id: int):
        account = self.repo.get(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")
        return account.balance

    def remove_account(self, account_id: int):
        account = self.repo.get(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")

        if account.balance != 0:
            raise ValueError("Cannot delete account with non-zero balance")

        self.repo.delete(account_id)

    def get_total_balance(self):
        all_accounts = self.repo.get_all()
        return sum(acc.balance for acc in all_accounts)

    def get_accounts_count(self) :
        return len(self.repo.get_all())