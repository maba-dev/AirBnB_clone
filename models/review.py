#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Call the construtor of BaseModel class"""
        super().__init__(*args, **kwargs)
