#!/usr/bin/python3

"""
Console that runs commands for the airbnb project.
Importing the cmd and other necessary modules
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    """
    HBNBCommand class for handling commands in the HBNB application.

    Attributes:
    - prompt (str): The prompt displayed to the user.

    Methods:
    - do_quit(arg): Exits the program.
    - do_exit(arg): Alias for the quit command.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # aliasing the command
    do_exit = do_quit

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""

        if not arg:
            print("** class name missing **")
            return
        
        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
