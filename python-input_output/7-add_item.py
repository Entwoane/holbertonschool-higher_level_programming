#!/usr/bin/python3
"""
A script that adds all command-line arguments to a Python list,
saves the list to a file in JSON format, and loads it back.

This script uses the `save_to_json_file` and `load_from_json_file`
functions from external modules.
"""
import sys
from os import path
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, "a+", encoding="utf-8") as file:
    if path.exists(filename):
        my_list = load(filename)
    else:
        my_list = []
    my_list.extend(args[1:])
    save(my_list, filename)
    load(filename)
