#!/usr/bin/python3
"""Tests for the module validator"""
import unittest
from io import StringIO
from unittest.mock import patch
from utils import validator


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
