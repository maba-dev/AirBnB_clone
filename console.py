#!/usr/bin/python3
""" console """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self):
        return True

    def emptyline(self):
        return False

    def do_quit(self, arg):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
