#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_attributes(self):
        """Test if the attributes of Amenity are present and initialized."""
        # Create an instance of Amenity
        amenity = Amenity()

        # Check if the attributes are present and initialized to default values
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        # Create an instance of Amenity
        amenity = Amenity()

        # Check if Amenity inherits from BaseModel
        self.assertIsInstance(amenity, BaseModel)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary."""
        # Create an instance of User
        amenity = Amenity()

        # Get the dictionary representation of the instance
        amenity_dict = amenity.to_dict()

        # Check if the keys and values in the dictionary are correct
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
