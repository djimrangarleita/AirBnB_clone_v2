#!/usr/bin/python3
"""Unit tests for the module file_storage"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from io import StringIO
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""
    def setUp(self):
        """Setup common behavior for each test"""
        try:
            os.rename('file.json', 'backup.json')
        except IOError:
            pass
        self.tmp_objects = storage._FileStorage__objects
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Reset state of app to default after test"""
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('backup.json', 'file.json')
        except IOError:
            pass
        storage._FileStorage__objects = self.tmp_objects

    def test_file_path_property_not_accessible(self):
        """Test that the __file_path property is file.json"""
        self.assertEqual(storage._FileStorage__file_path, 'file.json')

    def test_objects_dictionary(self):
        """Test that the __objects dict is empty"""
        self.assertIsNotNone(storage._FileStorage__objects)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(storage._FileStorage__objects, {})
        my_obj = BaseModel()
        storage.new(my_obj)
        self.assertNotEqual(storage._FileStorage__objects, {})
        key = "BaseModel.{}".format(my_obj.id)
        self.assertIn(key, storage._FileStorage__objects)
        new_obj = storage._FileStorage__objects[key]
        self.assertIs(my_obj, new_obj)
        self.assertEqual(len(storage._FileStorage__objects), 1)
        storage.__objects = {}
        self.assertNotEqual(storage._FileStorage__objects, storage.__objects)

    def test_all_will_return_a_dict_with_all_objects(self):
        """Test the all() method of the file storage will return all obj"""
        with patch('sys.stdout', new=StringIO()) as out:
            objects = storage.all()
            self.assertIsInstance(objects, dict)
            self.assertEqual(objects, {})

    def test_all_filtering(self):
        """Test that all can filter with class name"""
        with patch('sys.stdout', new=StringIO()) as out:
            storage.new(BaseModel())
            storage.new(State())
            storage.new(State())
            storage.new(City())
            self.assertEqual(len(storage.all()), 4)
            self.assertEqual(len(storage.all(State)), 2)

    def test_new_method(self):
        """Test that add() will add new object to the dictionary of objects"""
        with patch('sys.stdout', new=StringIO()) as out:
            model = BaseModel()
            storage.new(model)
            objects = storage.all()
            self.assertEqual(len(objects), 1)
            self.assertIn("{}.{}".format(type(model).__name__, model.id),
                          objects)
            storage.new(BaseModel())
            self.assertEqual(len(storage.all()), 2)

    def test_save_will_create_or_update_a_file(self):
        """Test that save() will create or update a json file"""
        self.assertFalse(os.path.exists('file.json'))
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_will_load_objects_from_json_file(self):
        """Test that the reload() method will load objects from json file"""
        with patch('sys.stdout', new=StringIO()) as out:
            storage.new(BaseModel())
            storage.new(BaseModel())
            storage.save()
            storage._FileStorage__objects = {}
            self.assertEqual(len(storage.all()), 0)
            storage.reload()
            self.assertEqual(len(storage.all()), 2)

    def test_delete_object_from_objects(self):
        """Test that an object can be deleted from __objects in storage"""
        with patch('sys.stdout', new=StringIO()) as out:
            state = State()
            storage.new(state)
            self.assertEqual(len(storage.all()), 1)
            storage.delete(state)
            self.assertEqual(len(storage.all()), 0)
