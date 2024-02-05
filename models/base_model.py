#!/usr/bin/python3
"""base_model
This module defines the BaseModel class.

Classes:
    - BaseModel: A base model class with common attributes and methods.
"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            - id (str): Unique identifier for the instance.
            - created_at (datetime): Date and time of instance creation.
            - updated_at (datetime): Date and time of last update.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Format: "[Class Name] (ID) Attributes"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
