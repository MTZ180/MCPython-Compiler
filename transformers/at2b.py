commands_dict = {     # A dictionary containing a binary representation of each of the commands
    'NOP': '0000',
    'XNOR': '0001',
    'NAND': '0010',
    'NOR': '0011',
    'XOR': '0100',
    'AND': '0101',
    'OR': '0110',
    'ADD': '0111',
    'SUB': '1000',
    'LDI': '1001',
    'HALT': '1010',
    'BRH': '1011',
    'CALL': '1100',
    'RET': '1101',
    'LOAD': '1110',
    'STR': '1111'
}


def compile_line(line):
    """Single-line compilation."""

    match line[0]:
        case 'ADD' | 'SUB' | 'XNOR' | 'NAND' | 'NOR' | 'XOR' | 'AND' | 'OR':
            binary_line = f"{commands_dict[line[0]]}{line[1][0]:04b}{line[1][1]:04b}{line[1][2]:04b}"
        case 'NOP' | 'RET' | 'HALT':
            binary_line = f"{commands_dict[line[0]]}"
        case 'LDI' | 'LOAD' | 'STR':
            binary_line = f"{commands_dict[line[0]]}{line[1][0]:08b}{line[1][1]:04b}"

    return binary_line


def compile_code(code):
    """Entire code compilation."""

    compiled_code = [compile_line(line) for line in code]

    return compiled_code