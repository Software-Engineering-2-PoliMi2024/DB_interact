from .DBinteract import DBinteract
from .NoDB import NoDB
from .MongoInteract import MongoInteract

def check_install():
    """
    Test function to verify that the module is working correctly.
    """
    print(f"🚀 Package {__package__} is working correctly 🚀")