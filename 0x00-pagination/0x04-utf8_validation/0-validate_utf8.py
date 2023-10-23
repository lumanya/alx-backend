#!/usr/bin/env python3
""" Write a method that determines if a given data set represents a
  valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the
 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check if the number is a valid start of a UTF-8 character
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        """ If there are no bytes to be processed, check for the number\
        of bytes in the current character """
        if num_bytes == 0:
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            # A single byte character
            if num_bytes == 0:
                continue

            # Invalid number of bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the number is a valid continuation byte
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes remaining to process
        num_bytes -= 1

    # If there are remaining bytes to be processed, the data is invalid
    return num_bytes == 0
