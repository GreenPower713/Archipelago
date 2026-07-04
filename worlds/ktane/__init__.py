import os, json
from typing import Dict, TextIO
from .Items import all_items_table, KTANEItem, modules_item_vanilla_nohl_table, modules_item_vanilla_hl_table, modded_modules_table, all_modules_table, progression_skip_balancing_items, useful_items
from .Locations import all_locations_table, KTANELocation
from .Options import KTANEOptions, get_option_value
from .Rules import set_rules_vanilla, set_rules_modded
from .Regions import create_regions_vanilla, create_regions_modded
from BaseClasses import Item, ItemClassification, Tutorial
from ..AutoWorld import World, WebWorld

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

    item_name_to_id = all_items_table
    location_name_to_id = all_locations_table

    data_version = 1

    options_dataclass = KTANEOptions

    def create_regions(self):
        adventure_mode = self.options.adventure_mode.value
        if adventure_mode == 0: #Vanilla Vanguard
            create_regions_vanilla(self.multiworld, self.player)
        else:
            create_regions_modded(self.multiworld, self.player)

    def set_rules(self):
        adventure_mode = self.options.adventure_mode.value
        if adventure_mode == 0: #Vanilla Vanguard
            set_rules_vanilla(self.multiworld, self.options, self.player)
        else:
            set_rules_modded(self.multiworld, self.options, self.player, self._finalChallengeComposition)

    def create_item(self, name: str) -> Item:
        classification = ItemClassification.filler
        if name in all_modules_table:
            classification = ItemClassification.progression
        elif name in progression_skip_balancing_items:
            classification = ItemClassification.progression_skip_balancing
        elif name in useful_items:
            classification = ItemClassification.useful
        return KTANEItem(name, classification, all_items_table[name], self.player)

    def create_items(self):
        hardlock_modules = self.options.hardlock_modules.value
        ohko_mode = self.options.ohko_mode.value
        adventure_mode = self.options.adventure_mode.value
        if adventure_mode == 0: #Vanilla Vanguard
            if hardlock_modules:
                self.multiworld.itempool += [self.create_item(module) for module in modules_item_vanilla_hl_table] # 11 modules
            else:
                self.multiworld.itempool += [self.create_item(module) for module in modules_item_vanilla_nohl_table] # 9 modules
            self.multiworld.itempool += [self.create_item("Time++") for _ in range(10)]
            self.multiworld.itempool += [self.create_item("Time+") for _ in range(18)]
            if not ohko_mode:
                self.multiworld.itempool += [self.create_item("Strike+") for _ in range(5)]
            self.multiworld.itempool += [self.create_item("Bomb Fragment") for _ in range(72 + (0 if hardlock_modules else 2) + (5 if ohko_mode else 0))]
        else: #Praetorian Pact
            self.multiworld.itempool += [self.create_item(module) for module in modded_modules_table] # 28 modules
            self.multiworld.itempool += [self.create_item("Time++") for _ in range(15)]
            self.multiworld.itempool += [self.create_item("Time+") for _ in range(40)]
            if not ohko_mode:
                self.multiworld.itempool += [self.create_item("Strike+") for _ in range(15)]
            self.multiworld.itempool += [self.create_item("Bomb Fragment") for _ in range(200)]
            self.multiworld.itempool += [self.create_item("Empty Manual Page") for _ in range(273 + (15 if ohko_mode else 0))]

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.options.adventure_mode.value == 1:
            spoiler_handle.write("Final Challenge Composition:     [" + ", ".join(self._finalChallengeComposition) + "]")

    def generate_early(self):
        if self.options.random_rule_seed.value:
            self.options.rule_seed.value = self.multiworld.random.randint(2, 10000)
        if self.options.adventure_mode.value == 1: #Praetorian Pact
            self._finalChallengeComposition = self.multiworld.random.sample(list(modded_modules_table.keys()), 15)
        else:
            self._finalChallengeComposition = []
    
    def fill_slot_data(self):
        slot_data: Dict[str, object] = {
            "random_rule_seed": self.options.random_rule_seed.value,
            "rule_seed": self.options.rule_seed.value,
            "adventure_mode": self.options.adventure_mode.value,
            "final_challenge_composition": self._finalChallengeComposition,
            "hardlock_modules": self.options.hardlock_modules.value,
            "ohko_mode": self.options.ohko_mode.value,
            #"manuals_language": self.options.manuals_language.value
            "death_link": self.options.death_link.value,
            "death_link_behaviour": self.options.death_link_behaviour.value
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
