#!/usr/bin/python3
"""
This is the CustomShell module. This module defines CustomShell class.
The CustomShell inherits from Cmd class and opens a command line interpreter
and prompts user for a command. Type help to list available commands.
"""
import cmd
from models import storage, user, base_model
from models import city, state, amenity, review, place


class CustomShell(cmd.Cmd):
    """
    This is the Custom Shell Class
    """
    prompt = '(hbnb) '
    class_dict = {'BaseModel': base_model.BaseModel, 'User': user.User,
                  'State': state.State, 'City': city.City,
                  'Amenity': amenity.Amenity, 'Place': place.Place,
                  'Review': review.Review}

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
        toks = CustomShell.__format_chk(arg, 'create')
        if toks != 0:
            instance = CustomShell.class_dict[toks[0]]()
            instance.save()
            print("{:s}".format(instance.id))

    def do_destory(self, arg):
        """
        Deletes an instance based on the class name and id
        Format: destory <class> <id>
        """
        toks = CustomShell.__format_chk(arg, 'destory')
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
        toks = CustomShell.__format_chk(arg, 'show')
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
            toks = CustomShell.__format_chk(arg, 'all')
            if toks != 0:
                for obj_id in obj.keys():
                    if obj[obj_id].to_json()['__class__'] == toks[0]:
                        print("{}".format(obj[obj_id]))

    def do_User(self):
        count = 0
        obj = storage.all()
        for obj_id in obj.keys():
            if obj[obj_id].to_json()['__class__'] == type(self).__name__:
                obj[obj_id] += 1
                print("{}".format(count))
        return count

    def do_count(self, arg):
        """
        Print the number of instances of a class.
        Format: <class name>.count().
        """
        toks = arg.split('.')
        if len(toks) > 1:
            count = CustomShell.class_dict[toks[0]].do_count()
            print("{}".format(count))

    def do_update(self, arg):
        """
        Updates the instance based on the class name, id by adding or updating
        an attribute
        Format: update <class> <id> <attribute> <value>
        """
        toks = CustomShell.__format_chk(arg, "update")
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
    def __format_chk(arg, cmd):
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
