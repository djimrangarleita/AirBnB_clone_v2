#!/usr/bin/python3
"""
This module contains the real implementation of the commands
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def create(class_name):
    """Create a new instance of BaseModel, save it and print its id"""
    new_instance = globals()[class_name]()
    new_instance.save()
    print(new_instance.id)


def show(args):
    """Print a string representation of an instance given its class name
    and id"""
    key = "{}.{}".format(args[0], args[1])
    objects = storage.all()
    print(objects[key])


def destroy(args):
    """Delete an instance based on class name and id, then save changes"""
    key = "{}.{}".format(args[0], args[1])
    storage.destroy_object(key)
    storage.save()


def all(class_name):
    """Print list of all classes"""
    classes = []
    objects = storage.all()
    for key, obj in objects.items():
        if class_name in key:
            classes.append(str(obj))
    print(classes)


def update(args, values):
    """Update attributes of a given instance"""
    key = "{}.{}".format(args[0], args[1])
    objects = storage.all()
    obj = objects[key]
    if isinstance(values, dict):
        for attr, val in values.items():
            setattr(obj, attr, val)
    else:
        setattr(obj, values[0], values[1])
    obj.save()


def count(class_name):
    """Count number of instances of class_name in storage"""
    result = 0
    objects = storage.all()
    for key, obj in objects.items():
        if class_name in key:
            result += 1
    print(result)
