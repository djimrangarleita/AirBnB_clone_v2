#!/usr/bin/python3
"""Unit tests for the BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test functions of BaseModel"""

    def test_init_without_arg(self):
        """Check that a new instance has been created with proper properties"""
        new_model = BaseModel()
        self.assertIsNotNone(new_model.id)
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
