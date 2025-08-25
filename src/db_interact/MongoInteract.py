from pymongo.mongo_client import MongoClient
from .DBinteract import DBinteract

from dotenv import load_dotenv
from os import getenv

from typing import Self


class MongoInteract(DBinteract):
    """ Class to interact with a MongoDB database.
        The class is designed to be used as a context manager to ensure proper resource management."""
    
    def __init__(self, dbName: str, path="./.env", uriVarName="DB_URI"):
        """ Initialize the MongoInteract class.
            Args:
             path (str): path to the .env file containing the DB_URI
             dbMane (str): name of the mongo db database to interact with
        """

        load_dotenv(path)
        self.dbUri = getenv(uriVarName)

        if self.dbUri is None:
            raise ValueError("DB_URI environment variable not set. Please set it in your .env file.")

        self.client = None
        self.db = None
        self.dbName = dbName

    
    def __enter__(self) -> Self:
        self.client = MongoClient(self.dbUri)
        try:
            self.client.admin.command('ping')
            self.db = self.client[self.dbName]
            return self

        except Exception as e:
            self.__exit__(None, None, None)
            raise ConnectionError(f"Could not connect to Mongo DataBase: {e}")
        
    def __exit__(self, exc_type, exc_value, exc_traceback) -> Self:        
        if self.client: self.client.close()