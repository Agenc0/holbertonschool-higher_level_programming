#!/usr/bin/python3
"""adds argument to a python list and saves them to a file"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    saved_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    saved_list = []
finally:
    saved_list.extend(argv[1:])
    save_to_json_file(saved_list, "add_item.json")
