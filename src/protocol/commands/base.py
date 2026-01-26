from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    """
    Base class for all protocol commands.
    Each command must implement the execute method,
    which takes a list of string arguments and returns a string response.
    """

    @abstractmethod
    def execute(self, args: List[str]):
        """
        Execute the command with the given arguments.
        Args: args (List[str]): Command arguments extracted from the protocol line.
        Returns: Response string to send back to the client.
        """
        pass
