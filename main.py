# list representation of the text:
# [component1, compinent2, component3]
# components:
# ["some text", attributes, escape_code]
# escape_code -> string(example, "\033[31m")
# attributes: (human-friendly escape code representation)
# ["bold", "italic", "lightred"]

# the double \ is to escape the first \, or else it would
# be considered a non-printable character like \n
test_list_repr = [
["I", ["WHITE"], "\\033[97;0m"],
[" love", ["RED", "BOLD", "ITALIC"], "\\033[31;1;3m"],
[" Stack", ["WHITE", "ITALIC"], "\\033[97;3m"],
["Overflow", ["YELLOW", "BOLD", "ITALIC"], "\\033[33;1;3m"],
]

test_expected_result = "echo -e \"\\033[0mI\\033[31;1;3m love\\033[97;3m Stack\\033[33;1;3mOverflow\""

COLORS = {
    "BLACK": 30,
    "RED": 31,
    "GREEN": 32,
    "YELLOW": 33,
    "BLUE": 34,
    "MAGENTA": 35,
    "CYAN": 36,
    "GRAY": 37,
    "DARK GRAY": 90,
    "LIGHT RED": 91,
    "LIGHT GREEN": 92,
    "LIGHT YELLOW": 93,
    "LIGHT BLUE": 94,
    "LIGHT MAGENTA": 95,
    "LIGHT CYAN": 96,
    "WHITE": 97
}

DECORATIONS = {
    "NORMAL": 0,

}



def generate_escapes(attributes):
    rv = "\\033["
    for attribute in attribute:
        pass
def generate_echo(list_repr):
    result = "echo -e \""
    for component in list_repr:
        result += component[2] + component[0]
    result += "\""
    return result

print(generate_echo(test_list_repr))
