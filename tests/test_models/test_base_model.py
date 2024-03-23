#!/usr/bin/python3
"""Unit tests for the BaseModel class"""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime, timedelta
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test functions of BaseModel"""

    def setUp(self):
        """Setup common behavior for each test"""
        try:
            os.rename('file.json', 'backup.json')
        except IOError:
            pass

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

    def test_init_without_arg(self):
        """Check that a new instance has been created with proper properties"""
        new_model = BaseModel()
        self.assertIsNotNone(new_model.id)
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_save_method_will_update_updated_at(self):
        """Check updated_at property is updated when save() is called"""
        b_model = BaseModel()
        initial_datetime = b_model.updated_at
        b_model.save()
        self.assertNotEqual(initial_datetime, b_model.updated_at)
        self.assertNotEqual(b_model.updated_at, b_model.created_at)
        self.assertAlmostEqual(b_model.updated_at, datetime.now(),
                               delta=timedelta(seconds=5))

    def test_str_method_return_a_string_with_expected_format(self):
        """Test that the __str__() method return the correct string"""
        b_model = BaseModel()
        str_rep = str(b_model)
        self.assertIsInstance(str_rep, str)
        self.assertIn('[BaseModel]', str_rep)
        self.assertIn("({})".format(b_model.id), str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(b_model)
            self.assertEqual(fake_out.getvalue().rstrip('\n'), str_rep)

    def test_to_dict(self):
        """Test that to dict method returns the correct dict with all keys"""
        model = BaseModel()
        dict_rep = model.to_dict()
        self.assertEqual(dict_rep['id'], model.id)
        self.assertEqual(dict_rep['__class__'], type(model).__name__)
        self.assertEqual(dict_rep['created_at'], model.created_at.isoformat())
        self.assertEqual(dict_rep['updated_at'], model.updated_at.isoformat())

    def test_init_with_kwargs(self):
        """Test that model can be initialize from dictionary kwargs"""
        dict_rep = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                    'created_at': '2017-09-28T21:03:54.052298',
                    'updated_at': '2017-09-28T21:03:54.052302'}
        model = BaseModel(**dict_rep)
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.id, dict_rep['id'])
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at,
                         datetime.fromisoformat(dict_rep['created_at']))
        self.assertEqual(model.updated_at,
                         datetime.fromisoformat(dict_rep['updated_at']))
