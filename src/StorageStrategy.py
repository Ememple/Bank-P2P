from abc import ABC, abstractmethod
from src.Account import Account

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, account: Account):
        pass

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass