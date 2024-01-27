#!/usr/bin/python3
"""
Defines a text indentation function.
"""

def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the index
    index = 0

    # Skip leading spaces
    while index < len(text) and text[index] == ' ':
        index += 1

    # Iterate through the text
    while index < len(text):
        # Print the current character
        print(text[index], end="")

        # Check for new lines or specific characters
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1

            # Skip trailing spaces after newline or specific characters
            while index < len(text) and text[index] == ' ':
                index += 1
            continue

        # Move to the next character
        index += 1

# Example usage
if __name__ == "__main__":
    example_text = """This is a sample text. It has multiple sentences.
    Each sentence should be on a new line. Will it work? Let's check."""
    text_indentation(example_text)
