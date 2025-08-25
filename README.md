# DB interact

This package provides modules to interact with a database, specifically it provides context managers to handle database connections and closures.
The package is designed to be just a starting point for database interaction, and can be extended to support specific operations as needed.

## Modules

in particualar, it includes:

- `DBinteract`: an abstract base class that defines the interface for database interaction.
- `NoDB`: a concrete implementation of `DBinteract` that does not connect to any database, useful for testing or for cases in which perstistent storage is not required.
- `MongoInteract`: a concrete implementation of `DBinteract` that connects to a MongoDB database given a .env file containing the connection URI, and the name of the database to connect to.

## Usage

To use the package, you can import the desired class and use it as a context manager. For example:

```python
from DB_interact import MongoInteract
from dotenv import find_dotenv

db = MongoInteract(db_name="mydatabase", path=find_dotenv(), uriVarName="DB_URI")

with db as database:
    # Perform database operations here

```
