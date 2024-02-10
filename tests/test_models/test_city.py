#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_attributes(self):
        """Test if the attributes of City are present and initialized."""
        # Create an instance of City
        city = City()

        # Check if the attributes are present and initialized to default values
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        # Create an instance of City
        city = City()

        # Check if City inherits from BaseModel
        self.assertIsInstance(city, BaseModel)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary."""
        # Create an instance of City
        city = City()

        # Get the dictionary representation of the instance
        city_dict = city.to_dict()

        # Check if the keys and values in the dictionary are correct
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], city.state_id)
        self.assertEqual(city_dict['name'], city.name)


if __name__ == '__main__':
    unittest.main()
