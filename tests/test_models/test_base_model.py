#!/usr/bin/python3
"""Unit tests for the BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test functions of BaseModel"""

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
