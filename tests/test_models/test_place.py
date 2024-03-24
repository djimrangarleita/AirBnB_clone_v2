#!/usr/bin/python3
"""Tests for the module place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test suite for the model Place"""

    def test_instantiation_without_args(self):
        """Test instantiation of a place without defined args"""
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_instantiation_with_args(self):
        """Test instantiation of a place object"""
        description_text = 'Longonot Loft is eco-friendly loft house'
        place = Place()
        place.city_id = 'fce12f8a-fdb6-439a-afe8-2881754de71c'
        place.user_id = 'fce12f8a-fdb6-439a-afe8-2881754de53b'
        place.name = 'Kode Central Park'
        place.description = description_text
        place.number_rooms = 2
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 252
        place.latitude = 12.2
        place.longitude = 9.1
        place.amenity_ids = ['fce12f8a', 'fdb6', '439a']
        self.assertEqual(place.city_id, 'fce12f8a-fdb6-439a-afe8-2881754de71c')
        self.assertEqual(place.user_id, 'fce12f8a-fdb6-439a-afe8-2881754de53b')
        self.assertEqual(place.name, 'Kode Central Park')
        self.assertEqual(place.description, description_text)
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 252)
        self.assertEqual(place.latitude, 12.2)
        self.assertEqual(place.longitude, 9.1)
        self.assertEqual(place.amenity_ids, ['fce12f8a', 'fdb6', '439a'])
