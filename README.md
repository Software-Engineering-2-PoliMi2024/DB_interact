# DB interact

This package provides modules to interact with a database, specifically it provides context managers to handle database connections and closures.
The package is designed to be just a starting point for database interaction, and can be extended to support specific operations as needed.

## Modules

in particualar, it includes:

- `DBinteract`: an abstract base class that defines the interface for database interaction.
- `NoDB`: a concrete implementation of `DBinteract` that does not connect to any database, useful for testing or for cases in which perstistent storage is not required.
- `MongoInteract`: a concrete implementation of `DBinteract` that connects to a MongoDB database given a .env file containing the connection URI, and the name of the database to connect to.

## Usage - MongoDB

To use the `MongoInteract` class, you need to have a `.env` file with the following content:

- `DB_URI`: the connection URI for your MongoDB database.
- `DB_NAME`: the name of the database you want to connect to.

an example of a `.env` file:

```.env
DB_URI = 'your_mongodb_connection_uri'
DB_NAME = 'your_database_name'
```

To use the `MongoInteract` class, you can do the following:

```python
from DB_interact import MongoInteract
from dotenv import find_dotenv

db = MongoInteract(path=find_dotenv())

with db as database:
    # Perform database operations here

```
