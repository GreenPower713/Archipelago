import os, json
from typing import Dict
from .Items import item_table, KTANEItem, modules_item_table, modules_item_nohl_table, other_progression_items, useful_items
from .Locations import location_table, KTANELocation
from .Options import KTANEOptions, get_option_value
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Item, ItemClassification, Tutorial
from ..AutoWorld import World, WebWorld
from random import randint

client_version = 1


class KTANEWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Keep Talking and Nobody Explodes for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["GreenPower713"]
    )]


class KTANEWorld(World):
    """ 
     Keep Talking and Nobody Explodes game description.
    """

    game: str = "Keep Talking and Nobody Explodes"
    topology_present = False
    web = KTANEWeb()

    item_name_to_id = item_table
    location_name_to_id = location_table

    data_version = 1

    options_dataclass = KTANEOptions

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)

    def create_item(self, name: str) -> Item:
        classification = ItemClassification.filler
        if name in modules_item_table.keys():
            classification = ItemClassification.progression
        elif name in other_progression_items.keys():
            classification = ItemClassification.progression_skip_balancing
        elif name in useful_items.keys():
            classification = ItemClassification.useful
        return KTANEItem(name, classification, item_table[name], self.player)

    def create_items(self):
        hardlock_modules = self.options.hardlock_modules.value
        ohko_mode = self.options.ohko_mode.value
        if hardlock_modules:
            for module in modules_item_table:  # 11 modules
                self.multiworld.itempool += [self.create_item(module)]
        else:
            for module in modules_item_nohl_table: # 9 modules
                self.multiworld.itempool += [self.create_item(module)]
        for i in range(10):
            self.multiworld.itempool += [self.create_item("Time++")]
        for i in range(18):
            self.multiworld.itempool += [self.create_item("Time+")]
        if not ohko_mode:
            for i in range(5):
                self.multiworld.itempool += [self.create_item("Strike+")]
        for i in range(72 + (0 if hardlock_modules else 2) + (5 if ohko_mode else 0)):
            self.multiworld.itempool += [self.create_item("Bomb Fragment")]

    def generate_basic(self):
        pass

    def generate_early(self):
        if self.options.random_rule_seed.value:
            self.options.rule_seed.value = randint(2, 10000)

    def fill_slot_data(self):
        slot_data: Dict[str, object] = {
            "random_rule_seed": self.options.random_rule_seed.value,
            "rule_seed": self.options.rule_seed.value,
            "hardlock_modules": self.options.hardlock_modules.value,
            "ohko_mode": self.options.ohko_mode.value,
            "manuals_language": self.options.manuals_language.value
        }

        return slot_data

    # def generate_output(self, output_directory: str):
    #    if self.multiworld.players != 1:
    #        return
    #    data = {
    #        "slot_data": self.fill_slot_data(),
    #        "location_to_item": {self.location_name_to_id[i.name] : item_table[i.item.name] for i in self.multiworld.get_locations()},
    #        "data_package": {
    #            "data": {
    #                "games": {
    #                    self.game: {
    #                        "item_name_to_id": self.item_name_to_id,
    #                        "location_name_to_id": self.location_name_to_id
    #                    }
    #                }
    #            }
    #        }
    #    }
    #    filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apv6"
    #    with open(os.path.join(output_directory, filename), 'w') as f:
    #        json.dump(data, f)
