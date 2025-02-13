#!/usr/bin/python3
"""
This script provides a utility function to convert a CSV file into a JSON file.

The function reads data from a CSV file, processes it
into a list of dictionaries, and writes the serialized
JSON data to a file named 'data.json'.
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to JSON format and writes it to 'data.json'.

    Args:
        filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion was successful
            False if the file was not found.
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            data = [row for row in csvreader]
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except FileNotFoundError:
        return False
