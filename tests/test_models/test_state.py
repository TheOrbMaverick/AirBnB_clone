#!/usr/bin/python3

"""
Testing expected Output from classes.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_attributes(self):
        """Test if the attributes of State are present and initialized."""
        # Create an instance of State
        state = State()

        # Check if the attributes are present and initialized to default
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        # Create an instance of State
        state = State()

        # Check if State inherits from BaseModel
        self.assertIsInstance(state, BaseModel)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected
        dictionary representation.
        """
        # Create an instance of State
        state = State()

        # Get the dictionary representation of the instance
        state_dict = state.to_dict()

        # Check if the keys and values in the dictionary are correct
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], state.name)


if __name__ == '__main__':
    unittest.main()
