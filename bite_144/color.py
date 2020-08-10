import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self._color = color
        self.rgb = COLOR_NAMES.get(self._color.upper(), None)

    @staticmethod
    def hex2rgb(x):
        """Class method that converts a hex value into an rgb one"""
        r, g, b = bytes.fromhex(x[1:])
        return (r, g, b)

    @staticmethod
    def rgb2hex(x):
        """Class method that converts an rgb value into a hex one"""
        r, g, b = x
        if any(comp < 0 for comp in x) or any(comp > 255 for comp in x):
            raise ValueError
        return f"#{r:02x}{g:02x}{b:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}({self._color!r})"

    def __str__(self):
        """Returns the string value of the color object"""
        if not self.rgb:
            return "Unknown"
        return f"{self.rgb}"


if __name__ == "__main__":
    c = Color("brown")
    print(c.rgb)
