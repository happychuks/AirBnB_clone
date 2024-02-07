#!/usr/bin/python3
"""
    The Base_Module!
"""

from uuid import uuid4
from datetime import datetime
import json

class BaseModel:
    """BaseModel class for AirBnB"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save method to update updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

class FileStorage:
    """FileStorage class for serializing and deserializing instances to/from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = {k: v if k in ['created_at', 'updated_at'] else v for k, v in value.items()}
                    obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    cls = globals()[class_name]
                    self.new(cls(**obj_dict))
        except FileNotFoundError:
            pass
