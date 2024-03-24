#!/usr/bin/python3
"""Tests for the module amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity model"""

    def test_instantiation(self):
        """Test instantiation of an Amenity object"""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.name)
        self.assertIsInstance(amenity.name, str)
        amenity.name = 'Restaurant'
        self.assertEqual(amenity.name, 'Restaurant')
