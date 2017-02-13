#!/usr/bin/python3
"""
This is the HBNBCommand module. This module defines HBNBCommand class.
The HBNBCommand inherits from Cmd class and opens a command line interpreter
and prompts user for a command. Type help to list available commands.
"""
import cmd
import re
import sys
import inspect
import ast
from models import storage, user, base_model
from models import city, state, amenity, review, place


class HBNBCommand(cmd.Cmd):
    """
    This is the HBNBCommand Class
    """
    prompt = '(hbnb) '
    class_dict = {'BaseModel': base_model.BaseModel, 'User': user.User,
                  'State': state.State, 'City': city.City,
                  'Amenity': amenity.Amenity, 'Place': place.Place,
                  'Review': review.Review}

    @staticmethod
    def __arg_chk(arg, cmd):
        """
        Error handling to check the format

        Returns the args in toks if pass else 0
        """
        cmd_by_numarg = {"create": 1, "show": 2, "destroy": 2, "update": 4,
                         "all": 1, "update_dict": 2}
        if len(arg) > 0:
            toks = arg.split(' ')
        else:
            print("** class name is missing **")
            return 0
        if HBNBCommand.__validate(toks[0]):
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
    def __format_chk(args):
        """
        checks the format of the args passed to do_<class>
        Returns: the args in a string separate by white space

        Issues:
            - Unable to take arguements with "(" ")" "," the string unless
              in there is once dictionary
            - Will accept if user give certain strange formattings
                + eg will accept User.all)(
        """
        must_have = "()"
        must_have_chk = 0
        args, dict_in_args = HBNBCommand.__chk_if_dict_in_args(args)

        if args == 0:
            print("** dictionary bad format **")
            return 0, 0

        for char in args:
            if char in must_have:
                must_have_chk += 1
        if len(args) > 0 and args[0] is '.':
            arg_list = re.split('[\(\),]+', args[1:])
            if arg_list[-1] == '' and must_have_chk == len(must_have):
                arg_list = arg_list[:-1] + dict_in_args
                cls_cmd = "do_" + arg_list[0]
                for i in range(len(arg_list)):
                    arg_list[i] = arg_list[i].strip(' ')
                while '' in arg_list:
                    arg_list.remove('')
                arg_list[0] = HBNBCommand.cls
                args = " ".join(arg_list)
                return cls_cmd, args
            else:
                print("** no command given or bad format **")
        else:
            print("*** Unknown syntax: {}, Please use . after <class>"
                  .format(args))
        return 0, 0

    @staticmethod
    def __validate(arg):
        """validates if arg is a class"""
        if arg in HBNBCommand.class_dict.keys():
            return True
        return False

    @staticmethod
    def __chk_if_dict_in_args(args):
        """
        check if dicts is given in args

        if found, returns args without dict, dict with the dict
        if not found, returns args, dict = []
        if incorrect format, returns 0,0

        Need to Update: to account for {} pairs
            - Now it will accept {} }} as a valid dictionary
        """
        dict_char = "{}"
        dict_chk = 0
        tmp_dict = tmp_args = ""
        dict_in_args = []

        for char in args:
            if char in dict_char:
                dict_chk += 1
        if dict_chk % len(dict_char) == 0 and dict_chk >= len(dict_char):
            dict_start = 0
            for char in args:
                if char == '{':
                    dict_start = 1
                    tmp_dict += char
                elif char == '}':
                    dict_start = 0
                    tmp_dict += char
                    dict_in_args.append(tmp_dict)
                    tmp_dict = ""
                elif dict_start == 1:
                    tmp_dict += char
                else:
                    tmp_args += char
            return tmp_args, dict_in_args
        elif dict_chk == 0:
            return args, dict_in_args
        else:
            return 0, 0

    def preloop(self):
        """
        dynamically create the do_<class> methods
        """
        for cls in HBNBCommand.class_dict.keys():
            setattr(self, 'do_{}'.format(cls), self.create_method)

    def onecmd(self, line):
        """
        catches the cmd input and sets HBNBCommand.cls = <class name>
        """
        cls = ''
        for letter in line:
            if letter == '.':
                break
            cls += letter

        HBNBCommand.cls = cls.strip(" ")
        return(cmd.Cmd.onecmd(self, line))

    def create_method(self, args):
        """
        creates the do_<class> methods and calls the desired command
        """

        cls_cmd, args = HBNBCommand.__format_chk(args)
        if args != 0:
            try:
                HBNBCommand.__dict__[cls_cmd](self, args)
            except Exception as e:
                print("** invalid command, exception:{} **".format(e))

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
        print()
        return True

    """
    Don't execute anything on emptyline and ENTER
    """
    def emptyline(self):
        pass

    """
    create a new instances and saves it into the json
    """
    def do_create(self, args):
        """
        creates an instance of the desired class

        Format: create <class>
        avaliable classes:
        BaseModel, User, State, City, Amenity, Place, Review
        """
        toks = HBNBCommand.__arg_chk(args, 'create')
        if toks != 0:
            instance = HBNBCommand.class_dict[toks[0]]()
            instance.save()
            print("{:s}".format(instance.id))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Format: destroy <class> <id>
        """
        toks = HBNBCommand.__arg_chk(arg, 'destroy')
        if toks != 0:
            obj = storage.all()
            obj_id = toks[1]
            if obj[obj_id].to_json()['__class__'] == toks[0]:
                obj.pop(toks[1], None)
                storage.__objects = obj
                storage.save()
            else:
                print("** no id found of that class **")

    def do_show(self, arg):
        """
        Prints the string representation an instance based on a class.
        Format: show <class> <id>
        """
        toks = HBNBCommand.__arg_chk(arg, 'show')
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
            toks = HBNBCommand.__arg_chk(arg, 'all')
            if toks != 0:
                for obj_id in obj.keys():
                    if obj[obj_id].to_json()['__class__'] == toks[0]:
                        print("{}".format(obj[obj_id]))

    def do_count(self, args):
        """
        returns the number of instances of a class
        """
        obj = storage.all()
        toks = HBNBCommand.__arg_chk(args, 'all')
        count = 0
        for obj_id in obj:
            if obj[obj_id].to_json()['__class__'] == toks[0]:
                count += 1
        print("{:d}".format(count))

    def do_update(self, args):
        """
        Updates the instance based on the class name, id by adding or updating
        an attribute

        Uses ast.literal_eval, not sure if this is a good thing
        Format: update <class> <id> <attribute> <value>
                <class>.update(<id>, {<dict>})
        """
        tmp_args = args
        args, dict_in_args = HBNBCommand.__chk_if_dict_in_args(args)
        if len(dict_in_args) > 0:
            toks = HBNBCommand.__arg_chk(tmp_args, "update_dict")
        else:
            toks = HBNBCommand.__arg_chk(tmp_args, "update")
        if toks != 0:
            obj = storage.all()
            obj_id = toks[1]
            if toks[2][0] == '{' and toks[-1][-1] == '}':
                try:
                    arg_dict = ast.literal_eval(dict_in_args[0])
                    for key in arg_dict.keys():
                        obj[obj_id].__dict__[key] = arg_dict[key]
                    storage.__objects = obj
                    storage.save()
                except Exception as e:
                    print("** Not a dictionary. {} **".format(e))
            else:
                attribute = toks[2]
                if obj[obj_id].to_json()['__class__'] == toks[0]:
                    obj[obj_id].__dict__[attribute] = toks[3]
                    storage.__objects = obj
                    storage.save()
                else:
                    print("** no id found of that class **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
