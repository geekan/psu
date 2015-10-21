import os
import re

def mkdir(*args):
    try:
        return os.mkdir(*args)
    except:
        return 

def ls(path='.'):
    return os.listdir(path)

def cd(path):
    return os.chdir(path)

def touch(path):
    return os.system('touch ' + path)

def pwd():
    return os.curdir

def cat():
    return

def echo():
    return

def head():
    return

def tail():
    return

def grep():
    return

