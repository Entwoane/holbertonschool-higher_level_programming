#!/usr/bin/python3
"""
This module provides functions to serialize a Python dictionary to an XML file
and deserialize an XML file back into a Python dictionary.

Functions:
    - serialize_to_xml(dictionary, filename): Serializes a dictionary
    into XML format and saves it to a file.
    - deserialize_from_xml(filename): Reads an XML file and
    converts it back into a dictionary.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML content.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to parse.

    Returns:
        dict: A dictionary representation of the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
