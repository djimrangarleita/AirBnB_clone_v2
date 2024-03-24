#!/usr/bin/python3
"""
Tests for the module review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test suite for the model Review"""

    def test_instiation_without_args(self):
        """Test default values of a Review object"""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_instantiation_with_args(self):
        """Test instantiation with custom args"""
        review = Review()
        review_text = 'The loft was absolutely beautiful and so peaceful'
        review.user_id = 'fce12f8a-fdb6-439a-afe8-2881754de71c'
        review.place_id = 'a42ee380-c959-450e-ad29-c840a898cfce'
        review.text = review_text
        self.assertEqual(review.user_id,
                         'fce12f8a-fdb6-439a-afe8-2881754de71c')
        self.assertEqual(review.place_id,
                         'a42ee380-c959-450e-ad29-c840a898cfce')
        self.assertEqual(review.text, review_text)
