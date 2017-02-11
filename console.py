#!/usr/bin/python3
"""
This is the CustomShell module. This module defines CustomShell class.
The CustomShell inherits from Cmd class and opens a command line interpreter
and prompts user for a command. Type help to list available commands.
"""
import cmd
import re
from models import storage, user, base_model
from models import city, state, amenity, review, place

import sys,inspect
class CustomShell(cmd.Cmd):
    """
    This is the Custom Shell Class
    """
    prompt = '(hbnb) '
    class_dict = {'BaseModel': base_model.BaseModel, 'User': user.User,
                  'State': state.State, 'City': city.City,
                  'Amenity': amenity.Amenity, 'Place': place.Place,
                  'Review': review.Review}

    def preloop(self):
        """
        dynamically create the do_<class> methods
        """
        import models
        for cls in CustomShell.class_dict.keys():
            setattr(self, 'do_{}'.format(cls), self.create_method)

    def onecmd(self, line):
        """
        catches the cmd input and sets CustomShell.cls = <class name>
        """
        cls = ''
        for letter in line:
            if letter == '.':
                break
            cls += letter
        CustomShell.cls = cls
        return(cmd.Cmd.onecmd(self, line))

    def create_method(self, args):
        """
        creates the do_<class> methods and calls the desired command
        """
        cls_cmd, args = CustomShell.__format_chk(args)
        if args != 0:
            print("\n\nthese are the cls_cmd:", cls_cmd)
            print("these are the arugs:", args)
            try:
                CustomShell.__dict__[cls_cmd](self, args)
            except Exception as e:
                print("invalid command, exception:{}".format(e))


    @staticmethod
    def __format_chk(args):
        """
        checks the format of the args passed to do_<class>
        Returns: the args in a string separate by white space

        Issues:
            - Unable to take arguements with "(" ")" "," the string
            - Will accept if user give certain strange formattings
                + eg will accept User.all)(
        """
        must_have="()"
        flag = 0
        for char in must_have:
            if char in args:
                flag += 1
        if len(args) > 0 and args[0] is '.':
            arg_list = re.split('[\(\),]+', args[1:])
            if arg_list[-1] == '' and len(arg_list) > 1 and flag == len(must_have):
                arg_list = arg_list[:-1]
                cls_cmd = "do_" + arg_list[0]
                for i in range(len(arg_list)):
                    arg_list[i] = arg_list[i].strip(' ')
                arg_list[0] = CustomShell.cls
                args = " ".join(arg_list)
                return cls_cmd, args
            else:
                print("no command given or bad format")
        else:
            print("*** Unknown syntax: {}, Please use . after <class>"
                  .format(args))
        return 0, 0

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

        Format: create <class>
        avaliable classes:
        BaseModel
        """
        toks = CustomShell.__arg_chk(arg, 'create')
        if toks != 0:
            instance = CustomShell.class_dict[toks[0]]()
            instance.save()
            print("{:s}".format(instance.id))

    def do_destory(self, arg):
        """
        Deletes an instance based on the class name and id
        Format: destory <class> <id>
        """
        toks = CustomShell.__arg_chk(arg, 'destory')
        if toks != 0:
            obj = storage.all()
            obj_id = toks[1]
            if obj[obj_id].to_json()['__class__'] == toks[0]:
                obj.pop(toks[1], None)
                storage.__objects = obj
                storage.save()
            else:
                print("no id found of that class")

    def do_show(self, arg):
        """
        Prints the string representation an instance based on a class.
        Format: show <class> <id>
        """
        toks = CustomShell.__arg_chk(arg, 'show')
        if toks != 0:
            obj = storage.all()
            obj_id = toks[1]
            if obj[obj_id].to_json()['__class__'] == toks[0]:
                print("{}".format(obj[obj_id]))
            else:
                print("no id found of that class")

    def do_all(self, arg):
        """
        prints all strings representations of all instances or not based
        on a class.
        Format: all <class>(optional)
        """
        obj = storage.all()
        if len(arg) == 0:
            for obj_id in obj.keys():
                print("{}".format(obj[obj_id]))
        else:
            toks = CustomShell.__arg_chk(arg, 'all')
            if toks != 0:
                for obj_id in obj.keys():
                    if obj[obj_id].to_json()['__class__'] == toks[0]:
                        print("{}".format(obj[obj_id]))

    def do_update(self, arg):
        """
        Updates the instance based on the class name, id by adding or updating
        an attribute
        Format: update <class> <id> <attribute> <value>
        """
        toks = CustomShell.__arg_chk(arg, "update")
        if toks != 0:
            obj = storage.all()
            obj_id = toks[1]
            attribute = toks[2]
            if obj[obj_id].to_json()['__class__'] == toks[0]:
                obj[obj_id].__dict__[attribute] = toks[3]
                storage.__objects = obj
                storage.save()
            else:
                print("no id found of that class")

    @staticmethod
    def __arg_chk(arg, cmd):
        """
        Error handling to check the format

        Returns the args in toks if pass else 0
        """
        cmd_by_numarg = {"create": 1, "show": 2, "destory": 2, "update": 4,
                         "all": 1}
        if len(arg) > 0:
            toks = arg.split(' ')
        else:
            print("** class name is missing **")
            return 0
        if CustomShell.__validate(toks[0]):
            if cmd_by_numarg[cmd] == 1:
                return toks
            obj = storage.all()
            if len(toks) < 2:
                print("** no instance found **")
            elif toks[1] not in obj:
                print("** instance id missing **")
            else:
                if cmd_by_numarg[cmd] == 2:
                    return toks
                if len(toks) < 3:
                    print("** no attributes found **")
                elif len(toks) < 4:
                    print("** value missing **")
                elif cmd_by_numarg[cmd] == 4:
                    return toks
        else:
            print("** class doesn't exist **")
        return 0

    @staticmethod
    def __validate(arg):
        """validates if arg is a class"""
        if arg in CustomShell.class_dict.keys():
            return True
        return False


if __name__ == '__main__':
    CustomShell().cmdloop()
