#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True
	
	#aliasing the command
	do_exit = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()