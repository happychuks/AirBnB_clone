#!/usr/bin/python3
"""
    The Base_Module!
"""
from uuid import uuid4
from datetime import datetime
import models
# from sqlalchemy import create_engine, Column, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from os import environ

# storage_engine = environ.get("HBNB_TYPE_STORAGE")

# if (storage_engine == "db"):
#     Base = declarative_base()
# else:
#     Base = object


class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    
    def __init__(self, *args, **kwargs):
        """
            To initialize a new BaseModel

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    iso_format = "%Y-%m-%dT%H:%M:%S.%f"
                    try:
                        setattr(self, key, datetime.strptime(
                            kwargs[key], iso_format
                            ))
                    except ValueError:
                        """
                            Handle invalid date
                        """
                        print("Invalid date {}: {}".format(key, kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
                self.id = str(uuid4())
            if "id" not in kwargs:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
            Then return string representation of the Model
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """
            to update time of the model
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            the custom representation of a model
        """
        custom_dict = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        for key, value in self.__dict__.items():
            if key not in ("id", "_sa_instance_state"):
                custom_dict[key] = value
        return custom_dict

    def delete(self):
        """
            To delete the current instance from storage
        """
        k = "{}.{}".format(type(self).__name__, self.id)
        del models.storage.__objects[k]
