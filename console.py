#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            fmtted_token = [i.strip(",") for i in lexer]
            fmtted_token.append(brackets.group())
            return fmtted_token
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        fmtted_token = [i.strip(",") for i in lexer]
        fmtted_token.append(curly_braces.group())
        return fmtted_token

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }


if __name__ == "__main__":
    HBNBCommand().cmdloop()