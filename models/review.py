#!/usr/bin/python3
"""
Module review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of a Review in the project"""
    place_id = ''
    user_id = ''
    text = ''
