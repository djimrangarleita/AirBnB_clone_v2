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

    def test_make_dict_from_str(self):
        """Test that a key val string pair will be normalized to a dict"""
        self.assertEqual(general.make_dict_from_str(['name="Djimra_NGARLEITA"']),
                         {'name': 'Djimra NGARLEITA'})
        self.assertEqual(general.make_dict_from_str(['age=1000']), {'age': 1000})
        self.assertEqual(general.make_dict_from_str(['height=182.50']),
                         {'height': 182.50})
        input_data = ['name="Djimra"', 'age=1000', 'height=182.50']
        expected_output = {'name': 'Djimra', 'age': 1000, 'height': 182.50}
        self.assertEqual(general.make_dict_from_str(input_data), expected_output)
