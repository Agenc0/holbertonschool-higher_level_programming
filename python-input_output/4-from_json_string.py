#!/usr/bin/python3
"""JSON to object function"""
import json


def from_json_string(my_str):
    """Returns object representation of JSON string"""
    return json.loads(my_str)
