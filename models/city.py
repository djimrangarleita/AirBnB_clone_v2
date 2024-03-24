#!/usr/bin/python3
"""
Module city, has class city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of a city within the project"""
    state_id = ''
    name = ''
