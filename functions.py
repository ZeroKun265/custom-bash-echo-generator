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
    "BOLD": 1,
    "DIM": 2,
    "ITALIC": 3,
    "UNDERLINEE": 4,
    "BLINKING": 5,
    "REVERSE": 7,
    "INVISIBLE": 8,
}

HIGHLIGHTS = {
    "BLACK HIGHLIGHT": 40,
    "RED HIGHLIGHT": 41,
    "GREEN HIGHLIGHT": 42,
    "YELLOW HIGHLIGHT": 43,
    "BLUE HIGHLIGHT": 44,
    "MAGENTA HIGHLIGHT": 45,
    "CYAN GIGHLIGHT": 46,
    "GRAY HIGHLIGHT":47,
    "DEFAULT": 49,
    "DARK GREY HIGHLIGHT": 100,
    "LIGHT RED HIGHLIGHT": 101,
    "LIGHT GREEN HIGHLIGHT": 102,
    "LIGHT YELLOW HIGHLIGHT": 103,
    "LIGHT BLUE HIGHLIGHT": 104,
    "LIGHT MAGENTA HIGHLIGHT":105,
    "LIGHT CYAN HIGHLIGHT": 106,
    "WHITE HIGHLIGHT": 107
}

# Note that when assigning colors to 
# a component the actual colornthat will be used to generate 
# the escape code is the first in the list
# so adding more colors is useless
# also, as good practice, only one color
# should beninside of a component
def generate_escapes(attributes):
    rv = "\\033["
    color_assigned = False
    highlight_assigned = False
    for attribute in attributes:
        if COLORS.get(attribute, False) and not color_assigned:
            rv += str(COLORS[attribute]) + ";"
            color_assigned = True
        elif HIGHLIGHTS.get(attribute, False) and not highlight_assigned:
            rv += str(HIGHLIGHTS[attribute]) + ";"
            highlight_assigned = True
        elif DECORATIONS.get(attribute, False):
            rv += str(DECORATIONS[attribute]) + ";"
    return rv + "m"

def generate_echo(list_repr):
    result = "echo -e \""
    for component in list_repr:
        result += component[2] + component[0]
    result += "\""
    return result

def print_colors():
    print(u"""
COLORS:

\033[0mBLACK    \033[30mExample
\033[0mRED      \033[31mExample
\033[0mGREEN    \033[32mExample
\033[0mYELLOW   \033[33mExample
\033[0mBLUE     \033[34mExample
\033[0mMAGENTA  \033[35mExample
\033[0mCYAN     \033[36mExample
\033[0mGRAY    \033[37mExample

\033[0mRESET    \033[0mExample

\033[0mDARK GRAY      \033[90mExample
\033[0mLIGHT RED      \033[91mExample
\033[0mLIGHT GREEN    \033[92mExample
\033[0mLIGHT YELLOW   \033[93mExample
\033[0mLIGHT BLUE     \033[94mExample
\033[0mLIGHT MAGENTA  \033[95mExample
\033[0mLIGHT CYAN     \033[96mExample
\033[0mWHITE          \033[97mExample
\033[0m
""")

def print_highlights():
    print(u"""
HIGHLIGHT COLORS:

\033[49mBLACK HIGHLIGHT \033[40mExample\033[49m
\033[49mRED HIGHLIGHT     \033[41mExample\033[49m
\033[49mGREEN HIGHLIGHT   \033[42mExample\033[49m
\033[49mYELLOW HIGHLIGHT  \033[43mExample\033[49m
\033[49mBLUE HIGHLIGHT    \033[44mExample\033[49m
\033[49mMAGENTA HIGHLIGHT \033[45mExample\033[49m
\033[49mCYAN HIGHLIGHT    \033[46mExample\033[49m
\033[49mGRAY HIGHLIGHT   \033[47mExample\033[49m

\033[49mRESET HIGHLIGHT   \033[49mExample\033[49m

\033[49mDARK GRAY HIGHLIGHT     \033[100mExample\033[49m
\033[49mLIGHT RED HIGHLIGHT     \033[101mExample\033[49m
\033[49mLIGHT GREEN HIGHLIGHT   \033[102mExample\033[49m
\033[49mLIGHT YELLOW HIGHLIGHT  \033[103mExample\033[49m
\033[49mLIGHT BLUE HIGHLIGHT    \033[104mExample\033[49m
\033[49mLIGHT MAGENTA HIGHLIGHT \033[105mExample\033[49m
\033[49mLIGHT CYAN HIGHLIGHT    \033[106mExample\033[49m
\033[49mWHITE HIGHLIGHT         \033[107mExample
\033[49m
""")
