#!/usr/bin/python3
"""
    Instantiates the storage system and defines
    dummy classes for further use
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.base_model import BaseModel

from os import environ

""" Define dummy classes for further use """
dummy_classes = {
    "BaseModel": BaseModel,
}

""" Get the storage engine type from environment variable """
storage_engine = environ.get("HBNB_TYPE_STORAGE")

""" Instantiate storage based on the storage engine type """
if storage_engine == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

""" Load data from storage """
storage.reload()
