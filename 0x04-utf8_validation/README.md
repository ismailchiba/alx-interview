# UTF-8 Validation

## Description
This project involves writing a method to determine if a given data set represents a valid UTF-8 encoding.

## Prototype
```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
```

## Requirements
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

## Example
```python
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```

## Usage
To test the function, run the provided `0-main.py` script.