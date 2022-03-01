#!/usr/bin/python3
"""
    a class BaseModel that defines all common attributes/methods for other classes
 """

import uuid
from datetime import datetime
class BaseModel:
    """ define the class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        val = datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, val)
                    else:
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at


    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
