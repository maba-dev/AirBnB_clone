#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing a Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Call the construtor of BaseModel class"""
        super().__init__(*args, **kwargs)
