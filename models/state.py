#!/usr/bin/python3
"""
    This Module containing the State class
    It represents a state!
"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """
    State class to represent states!

    Attributes:
        name (str): The name of the state.
        cities (relationship): Relationship with the City class.

    """
    if (storage_engine == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """
            cities list
            Retrieves a list of City instances

            Returns:
                list: List of City instances
            """
            result = []
            for j, i in models.storage.all(models.city.City).items():
                if (i.state_id == self.id):
                    result.append(i)
            return result
