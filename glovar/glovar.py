import json
import os
import sys

user_path = os.path.abspath(sys.argv[0]).replace("\\", "/") # default is caller frame path
def path(custom_path):
    global user_path
    user_path = custom_path

globals_file = "glovar.json"

def read_globals():
    if not os.path.exists(globals_file):
        return {}
    with open(globals_file, "r") as f:
        return json.load(f)

def write_globals(data):
    with open(globals_file, "w") as f:
        json.dump(data, f)

def set(name, value=None):
    data = read_globals()
    globals = data.get(user_path, {})
    globals[name] = value
    data[user_path] = globals
    write_globals(data)

def get(name):
    data = read_globals()
    globals = data.get(user_path, {})
    return globals.get(name)

def remove(name):
    data = read_globals()
    globals = data.get(user_path, {})
    globals.pop(name, None)
    data[user_path] = globals
    write_globals(data)
    return globals

def peek():
    data = read_globals()
    return data.get(user_path, {})