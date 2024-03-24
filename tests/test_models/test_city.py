#!/usr/bin/python3
"""Tests for the module city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the City class"""

    def test_instantiation_without_args(self):
        """Test instantiation of a new City object without arguments"""
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.state_id)
        self.assertIsNotNone(city.name)

    def test_instantiation_with_args(self):
        """Test instantiation of a new City object with defined args"""
        city = City()
        city.state_id = 'fce12f8a-fdb6-439a-afe8-2881754de71c'
        city.name = 'Ngalo City'
        self.assertEqual(city.name, 'Ngalo City')
        self.assertEqual(city.state_id, 'fce12f8a-fdb6-439a-afe8-2881754de71c')
