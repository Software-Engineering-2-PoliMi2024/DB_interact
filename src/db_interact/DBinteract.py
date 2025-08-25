from abc import ABC, abstractmethod
from typing import Dict, Self

class DBinteract(ABC):
    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def __enter__(self) -> Self:
        """Establish a connection to the database"""
        print("must be implemented in subclass")

    @abstractmethod
    def __exit__(self, exc_type, exc_value, exc_traceback) -> Self:        
        """Disconnect from the database."""
        print("must be implemented in subclass")
        return