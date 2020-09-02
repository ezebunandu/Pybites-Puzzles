from pathlib import Path
from urllib.request import urlretrieve

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

    def __init__(self, id_name, name, max_level, description, items):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = items or []


class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    def __init__(self, name, enchantments):
        self.name = name
        self.enchantments = enchantments or []

    def __repr__(self):
        return f"{self.name.title().replace('_', ' ')}:\n [{enchantment.max_level}] {enchantment.name} for enchantment in self.enchantments"
        
def _scrape_items(data_src):
    items = data_src.split("/")[-1]
    unwanted_strings_to_replace = [".", "_", "enchanted", "iron", "png", "sm"]
    for unwanted_string in unwanted_strings_to_replace:
        items = items.replace(unwanted_string, " ")
    return items.split()

def generate_enchantments(soup: Soup) -> dict:
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    enchantments = {}
    table = soup.find_all("table", class_="std_table")
    for tr in table[0].find_all("tr")[1:]:
        elements = tr.find_all("td")
        if elements:
            name = elements[0].text
            max_level = elements[1].text
            description = elements[2].text
            id_ = elements[3].text
            items = _scrape_items(elements[4].img["data-src"])
            enchantments[name] = [name, max_level, description, items]
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
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
