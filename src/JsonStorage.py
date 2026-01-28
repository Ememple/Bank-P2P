import json
import os
from src.StorageStrategy import StorageStrategy
from src.Account import Account
import logging

logger = logging.getLogger(__name__)

class JsonStorage(StorageStrategy):
    def __init__(self):
        self.filepath = "../res/data.json"
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump({}, f)

    def load(self):
        with open(self.filepath, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return {}
        loaded_accounts = {}
        for k, v in data.items():
            loaded_accounts[int(k)] = Account(v['id'], v['balance'])
        return loaded_accounts

    def save_file(self, data):
        export_data = {
            str(acc.id): {"id": acc.id, "balance": acc.balance}
            for acc in data.values()
        }
        with open(self.filepath, "w") as f:
            json.dump(export_data, f, indent=4)

    def save(self, account: Account):
        logger.info("Saving data to JSON file")
        data = self.load()
        data[account.id] = account
        self.save_file(data)

    def get(self, id: int):
        logger.info("Loading data from JSON file")
        data = self.load()
        return data.get(id)

    def delete(self, id: int):
        logger.info("deleting data from JSON file")
        data = self.load()
        if id in data:
            del data[id]
            self.save_file(data)

    def get_all(self):
        logger.info("Getting all values from JSON file")
        return list(self.load().values())