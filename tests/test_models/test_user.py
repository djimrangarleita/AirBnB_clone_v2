#!/usr/bin/python3
"""Test module for the user module"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test suite for the User class"""

    def test_user_instantiation(self):
        """Test that user instantiation succeed with default attributes"""
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

    def test_user_instantiation_with_attributes(self):
        """Test user instantiation with defined attributes"""
        user = User()
        user.password = 'password'
        user.email = 'djimra@hbnb.com'
        user.first_name = 'Djimra'
        user.last_name = 'NGARLEITA'
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.email, 'djimra@hbnb.com')
        self.assertEqual(user.first_name, 'Djimra')
        self.assertEqual(user.last_name, 'NGARLEITA')
