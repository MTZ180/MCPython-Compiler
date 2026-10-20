import re


def is_hex(text):
    """Check whether astring is a hexadecimal string."""

    return bool(re.fullmatch("[a-f0-9]+", text))


def hex_to_binary(text):
    """Convert a hexadecimal string to binary"""

    return bin(int(text, 16))[2:].zfill(16)


def convert_code(code, file_path):
    """Convert the entire code from hexadecimal to binary"""
    
    binary_code = []
    line_index = 0
    lines = list(filter(None, code.split("\n")))

    for line in lines:
        line = line.strip()
        line_index += 1
        if len(line) == 4 and is_hex(line):
            binary_code.append(hex_to_binary(line))
        elif len(line) == 4:
            return f"Error in file {file_path} line {line_index}:\n[ValueError] The code must contain only hexadecimal content."
        elif is_hex(line):
            return f"Error in file {file_path} line {line_index}:\n[ValueError] A hexadecimal instruction must be 4 characters long."
        else:
            return f"Error in file {file_path} line {line_index}:\n[ValueError] The code must contain only hexadecimal content.\n[ValueError] A hexadecimal instruction must be 4 characters long."
    
    return "\n".join(binary_code)