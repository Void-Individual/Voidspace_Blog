#!/usr/bin/python3
"""Module containing the parent class for the developing program"""

import uuid
from datetime import datetime
from models import storage


class SpaceBase():
    """The parent class for the sub-classes to be developed"""

    def __init__(self, *args, **kwargs):
        """Instantiation of the SpaceBase instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at =datetime.now()
            self.title = 'Blank'
            self.tag = 'N/A'
            storage.new(self)

    def save(self):
        """Method to save the changes an instance"""

        self.updated_at = datetime.now()
        storage.save()

    def delete(self):
        """Method to delete this instance"""

        storage.delete(self)

    def __str__(self) -> str:
        """String representation of the class"""

        prompt = f"{type(self).__name__}({self.id}): {self.__dict__}"
        return prompt

    def to_dict(self):
        """Method to return dictionary representation of the class"""

        obj_dict = self.__dict__.copy()
        obj_dict['class'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
