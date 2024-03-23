#!/usr/bin/python3
"""Command line interpreter for the AirBnB clone project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone project"""
    intro = "Welcome to the hbnb console. Type help to list all commands"
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit this interactive shell"""
        print('')
        return True

    def do_quit(self, line):
        """Exit this interactive shell"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
