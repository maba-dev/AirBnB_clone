#!/usr/bin/python3
from models.base_model import BaseModel

class city(BaseModel):
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
