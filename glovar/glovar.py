import json
import os
import sys

user_path = os.path.normpath(os.path.abspath(sys.argv[0])).replace(os.sep, "/") # default is caller frame path
def file(file_path):
    global user_path
    user_path = os.path.normpath(file_path).replace(os.sep, "/").lower()

data_path = os.getcwd() # default is caller frame directory
def data(directory=os.path.dirname(__file__)):
    global data_path
    data_path = os.path.join(os.path.normpath(directory).replace(os.sep, "/"), "glovar.json").lower()


def read_globals():
    if not os.path.exists(data_path):
        return {}
    with open(data_path, "r") as f:
        return json.load(f)

def write_globals(data):
    with open(data_path, "w") as f:
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