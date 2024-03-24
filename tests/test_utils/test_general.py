#!/usr/bin/python3
"""
Tests for the module general
"""
import unittest
from utils import general


class TestGeneral(unittest.TestCase):
    """Test suite for general utils"""

    def test_pascal_to_snake_funtion(self):
        """Test the function pascal_to_snake() works"""
        self.assertEqual(general.pascal_to_snake(''), '')
        self.assertEqual(general.pascal_to_snake('high'), 'high')
        self.assertEqual(general.pascal_to_snake('High'), 'high')
        self.assertEqual(general.pascal_to_snake('ClassName'),
                         'class_name')
        self.assertEqual(general.pascal_to_snake('coolClassName'),
                         'cool_class_name')
