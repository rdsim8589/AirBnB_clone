#!/usr/bin/python3
"""
This is the CustomShell module. This module defines CustomShell class.
The CustomShell inherits from Cmd class and opens a command line interpreter
and prompts user for a command. Type help to list available commands.
"""


import cmd
from models.base_model import BaseModel
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

    """
    create a new instances and saves it into the json
    """
    def do_create(self, arg):
        """
        creates an instance of the desired class

        avaliable classes:
        BaseClass
        """
        if len(arg) > 0:
            tokens = arg.split(' ')
            if self.__validate(tokens[0]):
                from tokens[0]
                instance = tokens[0]
                instance.save()
                print("{}".format(instance.id()))

    def __validate(self, arg):
        class_list = ['BaseModel']
        if arg in class_list:
            return True
        return False

    def class_selector(self, arg):
        class_dict = {'BaseModel' : BaseModel}


if __name__ == '__main__':
    CustomShell().cmdloop()
