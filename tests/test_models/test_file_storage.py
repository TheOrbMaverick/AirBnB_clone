#!/usr/bin/python3

"""
This is the file storage test case
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up a FileStorage instance for each test."""
        self.storage = FileStorage()

    def test_new(self):
        """Test adding a new object to the storage."""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn('BaseModel.{}'.format(obj.id), all_objs)

    def test_save_reload(self):
        """Test saving and reloading objects from file."""
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn('BaseModel.{}'.format(obj1.id), all_objs)
        self.assertIn('User.{}'.format(obj2.id), all_objs)


if __name__ == '__main__':
    unittest.main()