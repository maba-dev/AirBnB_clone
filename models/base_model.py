#!/usr/bin/python3
"""
    a class BaseModel that defines all common
    attributes/methods for other classes
 """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ define the class"""
    def __init__(self, *args, **kwargs):
        """ initialize the  constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value,
                        '%Y-%m-%ddT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
            The special __str__ method is used to indicate
            the string representation of an object.
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """call save(self) method of storage """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ a method to generate a dictionary representation of an instance"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
