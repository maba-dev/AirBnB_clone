#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd
from models.base_model import BaseModel
from models import storage
import models

classes = ("BaseModel", "User", "State", "City", "Amenity", "Place", "Review")


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
        if line in ["",None]:
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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
