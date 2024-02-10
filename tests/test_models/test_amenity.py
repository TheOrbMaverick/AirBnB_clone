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


if __name__ == '__main__':
    unittest.main()
