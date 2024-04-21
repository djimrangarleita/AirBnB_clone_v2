#!/usr/bin/python3
"""Tests for the module validator"""
import unittest
from io import StringIO
from unittest.mock import patch
from utils import validator
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestValidator(unittest.TestCase):
    """Test suite for validators"""

    def test_class_name_not_null(self):
        """Test that class name arg is noot null"""
        self.assertTrue(validator.class_name_not_null('MyClass'))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(validator.class_name_not_null(''))
            self.assertEqual(fake_out.getvalue(),
                             "** class name missing **\n")
            self.assertFalse(validator.class_name_not_null(None))

    def test_class_name_exist(self):
        """Test if class name exists"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(validator.class_name_exist('MyClass'))
            self.assertEqual(fake_out.getvalue(),
                             '** class doesn\'t exist **\n')
            self.assertTrue(validator.class_name_exist('User'))

    def test_instance_exist(self):
        """Test if given class instance exists"""
        base = BaseModel()
        key = "BaseModel.{}".format(base.id)
        self.assertIn(key, storage.all())

    def test_instance_arg_exist(self):
        """Test that function is called with an instance arg"""
        user = User()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(validator.instance_arg_exist(user.id))
            self.assertFalse(validator.instance_arg_exist(None))
            self.assertEqual(fake_out.getvalue(),
                             "** instance id missing **\n")
            fake_out.truncate(0)
            fake_out.seek(0)
            self.assertFalse(validator.instance_arg_exist(''))
            self.assertEqual(fake_out.getvalue(),
                             "** instance id missing **\n")

    def test_class_name_and_instance_exist(self):
        """Test that function is called with class name and instance id"""
        pass
