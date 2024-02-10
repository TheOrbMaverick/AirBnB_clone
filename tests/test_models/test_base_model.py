#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel class."""

    def test_id(self):
        """Test to show that the id us created"""

        # Create an instance of BaseModel
        base_model = BaseModel()
        # Check if the id attribute is not None
        self.assertIsNotNone(base_model.id)

    def test_str_method(self):
        """Test for expected string output."""

        # Create an instance of BaseModel
        base_model = BaseModel()
        # Check if __str__ method returns the expected string representation
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_to_dict_method(self):
        """Test for expected dictionary output."""

        # Create an instance of BaseModel
        base_model = BaseModel()
        # Get the dictionary representation of the instance
        model_dict = base_model.to_dict()
        # Check if the keys and values in the dictionary are correct
        self.assertEqual(model_dict['__class__'],
                         'BaseModel')
        self.assertEqual(model_dict['id'],
                         base_model.id)
        self.assertEqual(model_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
