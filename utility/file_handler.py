import os

def mkdir(dir_name, mode=0x775, exist_ok=True):
    os.makedirs(dir_name, mode, exist_ok)