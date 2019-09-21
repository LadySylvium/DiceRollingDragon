import configparser
import discord

config = configparser.ConfigParser()

def get_id(cat, name):
    config.read('auth.ini')
    try:
        return config.get(cat, name)
    except:
        return None

def get_dict(cat):
    config.read('auth.ini')
    try:
        return dict(config.items(cat))
    except:
        return None

files = get_dict('files')
commands = get_dict('commands')
