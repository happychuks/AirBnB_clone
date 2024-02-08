#!/usr/bin/python3
"""
    This is user class module
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """
    User class that represents a user

    Attributes:
        email (str): The email address of the user!
        password (str): The password of the user!
        first_name (str): The first name of the user!
        last_name (str): The last name of the user!
        places (relationship): Relationship with the Place class!
        reviews (relationship): Relationship with the Review class!
    """
    if (storage_engine == 'db'):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
