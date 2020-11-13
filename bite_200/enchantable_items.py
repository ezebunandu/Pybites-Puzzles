from pathlib import Path
from urllib.request import urlretrieve
import roman
from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


class Enchantment:
    """Minecraft enchantment class
    Implements the following:
        id_name, name, max_level, description, items
    """

    def __init__(self, id_name, name, max_level, description, items=None):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = items or []

    def __repr__(self):
        return f"{self.name} ({self.max_level}): {self.description}"


class Item:
    """Minecraft enchantable item class
    Implements the following:
        name, enchantments
    """

    def __init__(self, name, enchantments=None):
        self.name = name
        self.enchantments = enchantments or []

    def __repr__(self):
        string = f"{self.name.title()}\n"
        for enchantment in self.enchantments:
            string += f"{enchantment.max_level} {enchantment.name}"
        return string


def _scrape_items(data_src):
    out = []
    items = data_src.split("/")[-1]
    unwanted_strings_to_replace = [".", "enchanted_", "iron", "png", "sm"]
    for unwanted_string in unwanted_strings_to_replace:
        items = items.replace(unwanted_string, "")
    if "fishing_rod" in items:
        out.append("fishing_rod")
        items = items.replace("fishing_rod", "")
    out += items.split("_")
    return [item for item in out if item]


def generate_enchantments(soup: Soup) -> dict:
    """Generates a dictionary of Enchantment objects
    With the key being the id_name of the enchantment.
    """
    enchantments = {}
    table = soup.find_all("table", class_="std_table")
    for tr in table[0].find_all("tr")[1:]:
        elements = tr.find_all("td")
        if elements:
            full_name = elements[0].text
            name, id_name = full_name.split("(")
            id_name = id_name.strip(")")
            max_level = roman.fromRoman(elements[1].text)
            description = elements[2].text
            items = _scrape_items(elements[4].img["data-src"])
            enchantments[id_name] = Enchantment(id_name,
                                                name,
                                                max_level,
                                                description,
                                                items)
    return enchantments


def generate_items(data):
    """Generates a dictionary of Item objects
    With the key being the item name.
    """
    pass


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code."""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()
