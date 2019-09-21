import re
import random
import discord
from auth import *

d_re = re.compile(r'(?:(\d+))?(?:(d))?(?:(\d+))?(?:([+-])(\d+))?')

def get_stuff(text, regex_name=d_re):
    """Gets matches with regex. Defaults to the dice rolling one, but if I add more it's easier."""
    matches = regex_name.search(text)
    if matches:
        return matches.groups()

def cast_input(text="", T=int, fallback=1):
    """Prevents ValueErrors during input."""
    try:
        return T(text)
    except ValueError:
        return fallback

def open_file(file, x):
    """Attempts to open a file."""
    try:
        open_file = open(files.get(file), x)
        return open_file
    except FileNotFoundError:
        return "Error: Unable to find file."

def get_random_choice(file_name):
    """Gets a random choice from an array written by a file."""
    x = open_file(file_name, "r")
    choices = x.readlines()
    x.close()
    return random.choice(choices)
