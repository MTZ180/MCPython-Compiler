import re


def is_binary(text):
    """Check whether a string is binary-string"""

    return bool(re.fullmatch("[01]+", text))


def binary_to_hex(text):
    """Convert a binary-string to hexadecimal"""

    return hex(int(text, 2))[2:].zfill(4)


def convert_code(code, file_path):
    """Convert the entire code from binary to hexadecimal"""
    
    hex_code = []
    line_index = 0
    lines = list(filter(None, code.split("\n")))

    for line in lines:
        line_index += 1
        line = line.strip()
        if len(line) == 16 and is_binary(line):
            hex_code.append(binary_to_hex(line))
        elif len(line) == 16:
            return f"Error in file {file_path} line {line_index}:\n[ValueError] The code must contain only binary content."
        elif is_binary(line):
            return f"Error in file {file_path} line {line_index}:\n[ValueError] A binary instruction must be 16 characters long."
        else:
            return f"Error in file {file_path} line {line_index}:\n[ValueError] The code must contain only binary content.\n[ValueError] A binary instruction must be 16 characters long."
    
    return "\n".join(hex_code)