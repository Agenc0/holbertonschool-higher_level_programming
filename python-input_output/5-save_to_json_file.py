#!/usr/bin/python3
"""object to text file writer function"""
import json


def save_to_json_file(my_obj, filename):
    """writes object to text file using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
