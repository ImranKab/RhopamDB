import os, sys

comn = str(input("RhopamShell*= "))
if comn == 'addblock':
    with open('data.rnf', 'x') as dataf:
        dataf.write("[block] @ <blockdata>")
