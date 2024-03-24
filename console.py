#!/usr/bin/python3
"""Command line interpreter for the AirBnB clone project"""
import cmd
from utils import exec_cmd
from utils import validator
from utils.general import normalize_custom_cmd


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone project"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Read empty line and pass"""
        pass

    def precmd(self, line):
        """Read and sanitize the user input before cmd"""
        if line:
            line = line.strip()
        if isinstance(line, str):
            return line
        self.emptyline()

    def default(self, line):
        """Default commands"""
        if '.' not in line:
            return cmd.Cmd.default(self, line)
        line = normalize_custom_cmd(line)
        cmd.Cmd.onecmd(self, line)

    def do_EOF(self, line):
        """
        Exit this interactive shell.
        Usage: ^D
        """
        print('')
        return True

    def do_quit(self, line):
        """
        Exit this interactive shell.
        Usage: quit
        """
        return True

    def do_exit(self, line):
        """
        Exit this interactive shell.
        Usage: exit
        """
        return True

    def do_create(self, line):
        """
        Create a new obj of <class_name>, saves it and print its id.
        Usage: create <class_name>
        """
        if not validator.class_name_exist(line):
            return
        exec_cmd.create(line)

    def do_show(self, line):
        """
        Print the string representation of a given instance.
        Usage: show <class_name> <instance_id>
        """
        args = line.split()
        if not validator.class_name_and_instance_exist(args):
            return
        exec_cmd.show(args)

    def do_destroy(self, line):
        """
        Delete an instance from the storage based on class name and id.
        Usage: destroy <class_name> <instance_id>
        """
        args = line.split()
        if not validator.class_name_and_instance_exist(args):
            return
        exec_cmd.destroy(args)

    def do_all(self, line):
        """
        Print string representation of all classes based on class name or not.
        Usage: all [class_name]
        """
        if line and not validator.class_name_exist(line):
            return
        exec_cmd.all(line)

    def do_update(self, line):
        """
        Update an instance based on class name and save changes.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = line.split()
        if not validator.class_name_and_instance_exist(args):
            return
        if not validator.valid_attribute_name_and_value(args[2:]):
            return
        exec_cmd.update(args)

    def do_count(self, line):
        """
        Count instances of a class in the storage.
        Usage: <class_name>.count()
        """
        if not validator.class_name_exist(line):
            return
        exec_cmd.count(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
