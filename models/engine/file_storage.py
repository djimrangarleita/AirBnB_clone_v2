#!/usr/bin/python3
"""
This module is used to persist our objects into a file
"""
import json
import importlib
from utils.general import pascal_to_snake


class FileStorage:
    """Serialize/deserialize objects, to and from file storage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return all objects"""
        result = {}
        if cls is None:
            return self.__objects
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                result[key] = obj
        return result

    def new(self, obj):
        """Add a new object to the dictionary __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize an object to json and store it to a file"""
        json_str = json.dumps(self.__serialize_objects())
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """Deserializes json file to object"""
        dict_data = self.__load_from_file()
        for key, val in dict_data.items():
            class_name = val['__class__']
            my_class = self.__import_class(class_name)
            model_class = getattr(my_class, val['__class__'])
            obj = model_class(**val)
            self.new(obj)

    def destroy_object(self, key):
        """Delete an object from the __objects dictionary"""
        del self.__objects[key]

    def __load_from_file(self):
        """Load a file to json"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            return json.loads(data)
        except FileNotFoundError:
            return {}

    def __serialize_objects(self):
        """Serialize all objects to dictionary"""
        dict_of_objects = {}
        for key, obj in self.__objects.items():
            dict_of_objects[key] = obj.to_dict()
        return dict_of_objects

    def __import_class(self, class_name):
        """Import the proper class according to class name for instantiation"""
        my_class = ''
        module_name = pascal_to_snake(class_name)
        my_class = importlib.import_module('models.{}'.format(module_name))
        return my_class

    def delete(self, obj=None):
        """Delete obj from __objects if available"""
        if obj is None:
            return
        self.__objects.pop('{}.{}'.format(type(obj).__name__, obj.id), None)
