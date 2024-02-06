#!/usr/bin/python3
"""Add command-line arguments to a list and save them to a JSON file."""
import sys

if __name__ == "__main__":
    # Importing necessary functions from custom modules
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempt to load existing items from the JSON file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        items = []

    # Append command-line arguments to the list of items
    items.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(items, "add_item.json")
