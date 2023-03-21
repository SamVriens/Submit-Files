__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import os.path
import pathlib
import shutil
import sys
from os import path
from pathlib import Path
from zipfile import ZipFile

cwd = os.getcwd()
f_file = Path("files/")
data_zip = Path("data.zip/")
dir_cache = Path("cache/")
list_files = []

def clean_cache():
    os.chdir(cwd)
    if not os.path.exists(dir_cache):
         os.mkdir(dir_cache)
    else:
        #if os.path.exists(dir_cache):
            shutil.rmtree(dir_cache)
            os.chdir(cwd)
            os.mkdir(dir_cache)
    return

def cache_zip(zip_file, cache_dir):
    with ZipFile(zip_file, 'r') as f:
        f.extractall(cache_dir)
        return

    
def cached_files():
   os.chdir(dir_cache)
   files = os.listdir()
   for file_name in files:
    abs_path  = os.path.abspath(file_name)
    list_files.append(abs_path)
   return list_files
    
def find_password(list_files):
    #os.chdir(dir_cache)
    for file_name in list_files:
        abs_path = os.path.abspath(file_name)
        text = "password"
        if os.path.isfile(abs_path):
            with open(abs_path, 'r', encoding='utf-8') as f:
                if text in f.read():
                    final_path = os.path.abspath(file_name)
                    print(text + " found at " + final_path)
                else:
                    print("no password found at " + abs_path)
                pass     
clean_cache()
cache_zip(data_zip, dir_cache)
cached_files()
find_password(list_files)
#print(list_files)