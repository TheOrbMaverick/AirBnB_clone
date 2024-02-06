#!/usr/bin/python3

"""
Console that runs commands for the airbnb project.
Importing the cmd and other necessary modules
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """
    HBNBCommand class for handling commands in the HBNB application.

    Attributes:
    - prompt (str): The prompt displayed to the user.

    Methods:
    - do_quit(arg): Exits the program.
    - do_exit(arg): Alias for the quit command.
    - do_create(arg): Creates a new instance of BaseModel.
    - do_show(arg): Prints the string representation of an instance.
    - do_destroy(arg): Deletes an instance.
    - do_all(arg): Prints all instances.
    - do_update(arg): Updates an instance.
    """

    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # aliasing the command
    do_exit = do_quit

    def emptyline(self):
        """Emptyline method"""
        pass


    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)


    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in all_objs:
            print("** no instance found **")
            return

        print(all_objs[obj_key])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in all_objs:
            print("** no instance found **")
            return

        del all_objs[obj_key]
        storage.save()


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objs = storage.all()

        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        print([str(all_objs[obj]) for obj in all_objs])


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        all_objs = storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in all_objs:
            print("** no instance found **")
            return

        obj = all_objs[obj_key]
        setattr(obj, args[2], args[3])
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
