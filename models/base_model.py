#!/usr/bin/python3
"""
This module contains the base class that has all common methods and
attributes that other class will inherit from
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class is the base class for all model classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.__create_from_kwargs(**kwargs)

    def __str__(self):
        """Return a string representing an instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Save an instance and update updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        raw_dict = self.__dict__.copy()
        raw_dict['created_at'] = self.created_at.isoformat()
        raw_dict['updated_at'] = self.updated_at.isoformat()
        raw_dict['__class__'] = type(self).__name__
        return raw_dict

    def __create_from_kwargs(self, **kwargs):
        """Create an instance from dictionary"""
        for key, val in kwargs.items():
            if key != '__class__':
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.fromisoformat(val)
                setattr(self, key, val)
