#!/usr/bin/python3
"""
    1. Instantiates the storage system based on
        the value of the HBNB_TYPE_STORAGE
        environment variable
    2. Defines dummy classes and tables for further use
        in the application
    3. Reloads data from storage

    Dummy Classes:
        - BaseModel
        - User
        - Review
        - City
        - State
        - Place
        - Amenity

    Dummy Tables:
        - states
        - cities
        - users
        - places
        - reviews
        - amenities
"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity

from os import environ

"""
    Defines the dummy classes for further use!
"""
dummy_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Review": Review,
    "City": City,
    "State": State,
    "Place": Place,
    "Amenity": Amenity
}

"""
    Defines the dummy tables for further use!
"""
dummy_tables = {
    "states": State,
    "cities": City,
    "users": User,
    "places": Place,
    "reviews": Review,
    "amenities": Amenity
}

"""
    Gets the storage engine type from environment variable
"""
storage_engine = environ.get("HBNB_TYPE_STORAGE")

"""
    Instantiates the storage based on the storage engine type
"""
if storage_engine == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

"""
    Loads the stored data
"""
storage.reload()
