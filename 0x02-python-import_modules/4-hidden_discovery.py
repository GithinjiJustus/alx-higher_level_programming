#!/usr/bin/python3
# 4-hidden_discovery.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Prints all names defined in the hidden_4 module."""
    import hidden_4

    # Retrieve all names in hidden_4 module
    names = dir(hidden_4)

    # Filter and print names that do not start with "__"
    for name in names:
        if name[:2] != "__":
            print(name)
