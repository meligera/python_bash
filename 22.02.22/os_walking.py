from os import walk
from os.path import join

root = "home/gera/PycharmProjects/bash_lang/"
allfiles = [join(root,f) for root,dirs,files in walk(root) for f in files]

print(allfiles)