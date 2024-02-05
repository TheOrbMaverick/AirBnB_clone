#!/usr/bin/python3

"""
Console that runs commands for the airbnb project.
Importing the cmd module
"""
import cmd

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
	
	#aliasing the command
	do_exit = do_quit

if __name__ == '__main__':
	HBNBCommand().cmdloop()