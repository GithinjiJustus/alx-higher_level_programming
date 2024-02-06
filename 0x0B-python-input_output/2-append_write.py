#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to which the string will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added

if __name__ == "__main__":
    filename = "file_append.txt"
    text = "This School is so cool!\n"
    
    # If the file doesn't exist, create it
    append_write(filename, text)

    # Append the text again
    nb_characters_added = append_write(filename, text)
    print(nb_characters_added)
