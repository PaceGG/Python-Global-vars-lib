import glovar

glovar.var_file() # link reset py vars with its directory

glovar.set("x", glovar.get("x") + 1)

print(glovar.get("x"))