from .DBinteract import DBinteract
from typing import Dict, Self

class NoDB(DBinteract):
    def __init__(self):
        """NoDB is a placeholder for when no database interaction is needed."""

    def __enter__(self) -> Self:
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback) -> Self:        
        pass