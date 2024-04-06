#!/usr/bin/python3
"""Json representation function"""
import json


def to_json_string(my_obj):
    """returns my_obj in JSON representation"""
    return json.dumps(my_obj)
