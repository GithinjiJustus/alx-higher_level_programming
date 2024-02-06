#!/usr/bin/python3

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters

if __name__ == "__main__":
    filename = "my_first_file.txt"
    text = "This School is so cool!\n"
    nb_characters = write_file(filename, text)
    print(nb_characters)
