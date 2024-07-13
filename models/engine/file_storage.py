#!/usr/bin/python3
"""Module for storing objects in a json file"""

import json


class FileStorage:
    """Class to handle saving objects"""

    __objects = {}
    __file_path = 'spaceFile.json'

    def all(self):
        """Method to return all saved objects"""

        return self.__objects

    def new(self, obj):
        """Adds a new instance to the colected objects with a format
        <class name>.id"""

        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def delete(self, obj):
        """Method to delete a saved instance from the collection"""

        for key, value in self.__objects.items():
            if value == obj:
                del(self.__objects[key])
                break
        self.save()

    def save(self):
        """Serializes all current objects to a json file"""

        serialized_objects = {}
        # Retrieve the dict representation of all collected objects
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        # Open a json file and save the data in it, overwritting its previous content
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """To deserialize the json file into collected objects"""

        try:
            # Open the saved file if it exists
            with open(self.__file_path, 'r') as file:
                # Load the file if it exists
                object_dict = json.load(file)
                # Reset the collected objects to be an empty dict of values
                self.__objects = {}

                # Iterate over the data from the loaded file
                for key, value in object_dict.items():
                    # Split the key to retrieve the class name
                    class_name, obj_id = key.split('.')
                    obj_dict = value

                    # If the class is a valid one
                    if class_name == "SpaceBase":
                        from models.Space_Base import SpaceBase
                        # Generate an instance of this object with the saved values
                        obj = SpaceBase(**obj_dict)

                    self.__objects[key] = obj
        except Exception as err:
            print(err)
