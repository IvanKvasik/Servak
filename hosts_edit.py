import os, subprocess
import sys
from sys import argv

def etc_update(name, *args):
    path = "/etc/hosts"
    name = name[0]
    fw = open(path,'a')
    fw.write('127.0.0.1\t' + name + "\n")

etc_update(sys.argv[1:])