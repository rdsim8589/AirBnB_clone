#!/usr/bin/python3
"""
This is the CustomShell module. This module opens a command line interpreter
and prompts user for a command. Type help to list available commands.
"""


import cmd
class CustomShell(cmd.Cmd):
    prompt = '(hbnb) '

    """
    Document quit command information and exit the program.
    """
    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    """
    Document EOF command information and exit the program.
    """
    def do_EOF(self, arg):
        'Ctrl-D shortcut to exit the program\n'
        return True

    """
    Don't execute anything on emptyline and ENTER
    """
    def emptyline(self):
        pass


if __name__ == '__main__':
    CustomShell().cmdloop()
