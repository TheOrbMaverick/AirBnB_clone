#!/usr/bin/python3
"""test_console
Module for testing the HBNBCommand console.
"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from io import StringIO
from unittest.mock import patch
import console
import os
import unittest


class TestHBNBCommand(unittest.TestCase):
    """
    Test for the HBNBCommand console.
    """
    def setUp(self):
        """Sets up test cases."""
        self.tearDown()
        self.cmd = console.HBNBCommand()
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Resets FileStorage data."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docstrings(self):
        """Tests documentation strings."""
        test_cases = [
            ("module doc", console.__doc__),
            ("class doc", self.cmd.__doc__),
            ("method docs", [
                self.cmd.default,
                self.cmd.dict_update,
                self.cmd.do_EOF,
                self.cmd.do_quit,
                self.cmd.emptyline,
                self.cmd.do_create,
                self.cmd.do_show,
                self.cmd.do_destroy,
                self.cmd.do_all,
                self.cmd.do_count,
                self.cmd.do_update,
            ]),
        ]
        for case_name, case in test_cases:
            with self.subTest(case_name):
                if isinstance(case, list):
                    for method in case:
                        self.assertIsNotNone(method.__doc__)
                else:
                    self.assertIsNotNone(case)

    def test_quit_command(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd("quit"))
            self.assertEqual(fake_out.getvalue(), '')

    def test_create_command(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("create User")
            self.assertTrue(fake_out.getvalue().strip())

    def test_show_command(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("show BaseModel")
            self.assertEqual(fake_out.getvalue().strip(),
                             "** instance id missing **")

    def test_destroy_command(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("destroy BaseModel")
            self.assertEqual(fake_out.getvalue().strip(),
                             "** instance id missing **")

    # def test_all_command(self):
    #     """Test all command."""
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.cmd.onecmd("all")
    #         self.assertEqual(fake_out.getvalue().strip(),
    #                          "** class name missing **")

    def test_update_command(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("update")
            self.assertEqual(fake_out.getvalue().strip(),
                             "** class name missing **")

    def test_count_command(self):
        """Test count command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("count")
            self.assertEqual(fake_out.getvalue().strip(),
                             "** class name missing **")


if __name__ == '__main__':
    unittest.main()
