#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    
    Args:
        roman_string: Input string representing a Roman numeral
    
    Returns:
        The integer value of the Roman numeral, or 0 if invalid input
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_dict.get(char, 0)
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value

    return result

# For testing the function
if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
