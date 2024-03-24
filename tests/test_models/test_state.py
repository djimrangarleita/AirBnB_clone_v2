#!/usr/bin/python3
"""Tests for the module state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test suite for the State model"""

    def test_instantiation(self):
        """Test instantiation without attribute"""
        state = State()
        self.assertIsNotNone(state.name)
        self.assertEqual(state.name, '')
        state.name = 'Kode'
        self.assertEqual(state.name, 'Kode')
