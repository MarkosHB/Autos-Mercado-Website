from enum import Enum


class Size(Enum):
    ZERO = "0px !important"
    VERY_SMALL = "0.3em"
    SMALL = "0.5em"
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    DEFAULT_MEDIUM = "1.125em"
    DEFAULT_BIG = "1.5em"
    BIG = "2em"
    MEDIUM_BIG = "3em"
    VERY_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "2"
    DEFAULT = "4"  # 1em
    DEFAULT_BIG = "5"
    BIG = "6"
    MEDIUM_BIG = "8"
    VERY_BIG = "9"


class Color(Enum):
    PRIMARY = "#0C1116"
    SECONDARY = "#010408"
    TERTIARY = "#0a0e12"


class TextColor(Enum):
    PRIMARY = "#FFFFFF"
    SECONDARY = "#8A939E"
    TERTIARY = "#0C1116"
    PINK = "rgb(245, 184, 165)"
    YELLOW = "rgb(241, 225, 112)"
    GREEN = "rgb(182, 209, 98)"
    BLUE = "rgb(130, 210, 207)"
    PURPLE = "rgb(188, 154, 250)"
    RED = "rgb(255, 45, 45)"


class Font(Enum):
    DEFAULT = "Mona Sans"


class FontWeight(Enum):
    NORMAL = "400"
    MEDIUM = "500"
    BOLD = "700"
