import os

import glovar
glovar.file(os.path.dirname(__file__)) # link reset py vars with its directory

glovar.set("x", 0)