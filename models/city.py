#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ Call the construtor of BaseModel class"""
        super().__init__(*args, **kwargs)
