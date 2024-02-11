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
        self.classes = ["BaseModel", "User", "Place", "State",
                        "City", "Amenity", "Review"]

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

    def test_do_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cmd.onecmd("quit"))
        self.assertEqual(f.getvalue(), '')

    def test_do_EOF(self):
        """Tests EOF commmand."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.cmd.onecmd("EOF"))
        self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        """Tests empty line command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("\n")
        self.assertEqual(f.getvalue(), '')

    # def test_help_command(self):
#         """Tests the help command."""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.cmd.onecmd("help")
#         exp_o = """
# Documented commands (type help <topic>):
# ========================================
# EOF  all  count  create  destroy  exit  help  quit  show  update

# """
#         self.assertEqual(f.getvalue(), exp_o)

    def test_do_create(self):
        """Test create command.
        Includes checks for errors.
        """
        for classname in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.cmd.onecmd(f"create {classname}")
            uid = f.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)
            key = (f"{classname}.{uid}")

            with patch('sys.stdout', new=StringIO()) as f:
                self.cmd.onecmd(f"all {classname}")
            self.assertTrue(uid in f.getvalue())

        # no class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create")
        self.assertEqual(f.getvalue()[:-1], "** class name missing **")

        # nonexistent class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create srhbk")
        self.assertEqual(f.getvalue()[:-1], "** class doesn't exist **")

    def test_do_show(self):
        """Tests show for all classes.
        Includes error checks.
        """
        for classname in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.cmd.onecmd(f"create {classname}")
            uid = f.getvalue().strip()
            self.assertTrue(len(uid) > 0)

            with patch('sys.stdout', new=StringIO()) as f:
                self.cmd.onecmd(f"show {classname} {uid}")
            strn = f.getvalue().strip()
            self.assertTrue(uid in strn)

        # no class_name
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("show")
        self.assertEqual(f.getvalue()[:-1], "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd(".show()")
        self.assertEqual(f.getvalue()[:-1], "** class name missing **")

        # nonexistent class_name
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("show dtjlv7")
        self.assertEqual(f.getvalue()[:-1], "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("ftyko6.show()")
        self.assertEqual(f.getvalue()[:-1], "** class doesn't exist **")

        # no id
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("show BaseModel")
        self.assertEqual(f.getvalue()[:-1], "** instance id missing **")

        # with patch('sys.stdout', new=StringIO()) as f:
        #     self.cmd.onecmd("BaseModel.show()")
        # self.assertEqual(f.getvalue()[:-1], "** instance id missing **")

        # nonexistent id
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("show BaseModel 12345379359")
        self.assertEqual(f.getvalue()[:-1], "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('BaseModel.show("123456524359")')
        self.assertEqual(f.getvalue()[:-1], "** no instance found **")

    # def test_do_show_x(self, classname):
    #     """Tests .show() command."""
    #     for classname in self.classes:
    #         with patch('sys.stdout', new=StringIO()) as f:
    #             self.cmd.onecmd(f"create {classname}")
    #         uid = f.getvalue()[:-1]
    #         self.assertTrue(len(uid) > 0)

    #         with patch('sys.stdout', new=StringIO()) as f:
    #             self.cmd.onecmd('{}.show("{}")'.format(classname, uid))
    #         self.assertTrue(uid in f.getvalue())

    def test_do_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

    # def test_do_all(self):
    #     """Test all command."""
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         self.cmd.onecmd("all")
    #         self.assertEqual(f.getvalue().strip(),
    #                          "** class name missing **")

    def test_do_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("update")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

    def test_count_command(self):
        """Test count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("count")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")


if __name__ == '__main__':
    unittest.main()
