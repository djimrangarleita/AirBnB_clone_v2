"""Contains methods for cmd validation"""
from models import storage

classes = ['BaseModel']


def class_name_not_null(class_name):
    """Check that the class name is not empty string"""
    if not class_name:
        print("** class name missing")
        return False
    return True


def class_name_exist(class_name):
    """Check class name exists"""
    if not class_name_not_null(class_name):
        return False
    if class_name not in classes:
        print("** class doesn't exist **")
        return False
    return True


def instance_arg_exist(instance_id):
    """Check an instance id is passed as argument"""
    if not instance_id:
        print('** instance id missing **')
        return False
    return True


def instance_exist(class_name, instance_id):
    if not instance_arg_exist(instance_id):
        return False
    key = "{}.{}".format(class_name, instance_id)
    objects = storage.all()
    if key not in objects:
        print("** no instance found **")
        return False
    return True


def class_name_and_instance_exist(args):
    """Check argument line has valid class name and has instance id"""
    if len(args) == 0:
        class_name_not_null(None)
        return False
    if len(args) == 1:
        return class_name_exist(args[0]) and instance_arg_exist(None)
    return class_name_exist(args[0]) and instance_exist(args[0], args[1])


def valid_attribute_name_and_value(args):
    """Check that attribute name and value exist and are valid"""
    if len(args) == 0:
        print("** attribute name missing **")
        return False
    if len(args) == 1:
        print("** value missing **")
        return False
    return True
