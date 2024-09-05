import json
import inspect
import os

globals_file = "globals.json"
with open(globals_file, "w") as f:
    pass

def set(name, value=None):
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_filename = os.path.abspath(caller_frame.filename).replace("\\", "/")

    with open(globals_file, "r") as f:
        try: globals = json.load(f)[caller_filename]
        except:
            with open(globals_file, "w") as f:
                json.dump({caller_filename: {}}, f)
            with open(globals_file, "r") as f:
                globals = json.load(f)[caller_filename]

    globals[name] = value
    
    with open(globals_file, "r") as f:
        data = json.load(f)
    data[caller_filename] = globals

    with open(globals_file, "w") as f:
        json.dump(data, f)

def get(name):
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_filename = os.path.abspath(caller_frame.filename).replace("\\", "/")
    
    with open(globals_file, "r") as f:
        globals = json.load(f)[caller_filename]

    return globals[name]

def remove(name):
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_filename = os.path.abspath(caller_frame.filename).replace("\\", "/")

    with open(globals_file, "r") as f:
        globals = json.load(f)[caller_filename]

    globals.pop(name, None)

    with open(globals_file, "r") as f:
        data = json.load(f)

    data[caller_filename] = globals

    with open(globals_file, "w") as f:
        json.dump(data, f)

    return globals

def peek():
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_filename = os.path.abspath(caller_frame.filename).replace("\\", "/")

    with open(globals_file, "r") as f:
        globals = json.load(f)[caller_filename]

    return globals