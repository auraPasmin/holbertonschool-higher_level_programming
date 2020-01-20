#!/urs/bin/python3
"""function that returns True if that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Args:
    obj: a object
    a_class: a Class
    Return: True or False
    """
    tyobj = type(obj)
    if issubclass(tyobj, a_class) and tyobj != a_class:
        return True
    else:
        return False
