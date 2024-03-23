#!/usr/bin/python3
"""
This module is used to persist our objects into a file
"""
import json
import importlib


class FileStorage:
    """Serialize/deserialize objects, to and from file storage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return all objects"""
        return self.__objects

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
        base_mod = importlib.import_module('models.base_model')
        dict_data = self.__load_from_file()
        for key, val in dict_data.items():
            base_model_class = getattr(base_mod, val['__class__'])
            obj = base_model_class(**val)
            self.new(obj)

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
