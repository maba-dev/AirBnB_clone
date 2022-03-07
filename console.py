#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd
from models.base_model import BaseModel
import global_usage
from global_usage import *
from models import storage
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """
        Manage the EOF
        """
        print()
        return True

    def do_quit(self, line):
        """_quit_
        quitte le programme

        Args:
            line (_type_): _description_

        Returns:
            _boolean_: _True_
        """
        return True

    def do_create(self, className):
        """do_create
        créer une  nouvelle class

        Args:
            className (_type_): _description_
        """
        if not className:
            print("** class name missing **")
        try:
            newClass = eval(className)()
            print(newClass.id)
            newClass.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """do_show
            Prints the string representation of an instance.
        Args:
            line (_type_): _description_
        """
        if line in ["", None]:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not line:
            print("** class name missing **")
            return False
        data = shlex.split(line)
        print(data)
        if data[0] not in global_usage.classe:
            print("** class doesn't exist **")
            return False
        if len(data) == 1:
            print("** instance id missing **")
            return False
        classNameId = "{}.{}".format(data[0], data[1])
        if classNameId not in models.storage.all():
            print("** no instance found **")
            return False
        del models.storage.all()[classNameId]
        models.storage.save()

    def do_all(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                list_item = [str(obj) for key,
                             obj in storage.all().items()
                             if type(obj).__name__ == words[0]]
                print(list_item)
        else:
            list_item = [str(obj) for key, obj in storage.all().items()]
            print(list_item)

    def do_update(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(line)
        if not line:
            print("** class name missing ** ")
            return False
        data = shlex.split(line)
        print(data)
        if data[0] not in global_usage.classe:
            print("** class doesn't exist **")
            return False
        lendata = len(data)
        if lendata == 1:
            print("** instance id missing **")
        else:
            strLine = "{}.{}".format(data[0], data[1])
            if strLine not in models.storage.all():
                print("** no instance found **")
                return False
            if lendata == 2:
                print("** attribute name missing **")
                return False
            if lendata == 3:
                print("** value missing **")
                return False
        setattr(models.storage.all()[strLine], data[2], data[3])
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
