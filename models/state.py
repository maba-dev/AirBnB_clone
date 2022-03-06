#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """Class representing a State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Call the construtor of BaseModel class"""
        super().__init__(*args, **kwargs)
