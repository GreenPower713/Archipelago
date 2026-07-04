from BaseClasses import Item


class KTANEItem(Item):
    game: str = "Keep Talking and Nobody Explodes"

#Name classification:
#713 01 001
#713 Auth
#01 Game
#001 itemID

generic_vanilla_modules_table = {
    "Complicated Wires": 71301001,
    "Maze": 71301002,
    "Memory": 71301003,
    "Morse Code": 71301004,
    "Password": 71301005,
    "Simon Says": 71301006,
    "Who's on First": 71301007,
    "Wire Sequence": 71301008,
    "Knob": 71301010
}

hardlock_specific_needies_table = {
    "Capacitor": 71301009,
    "Vent Gas": 71301011
}

modded_modules_table = {
    "Switches": 71301016,
    "Chess": 71301017,
    "Mouse in the Maze": 71301018,
    "3D Maze": 71301019,
    "Tic Tac Toe": 71301020,
    "Follow the Leader": 71301021,
    "Friendship": 71301022,
    "The Bulb": 71301023,
    "Blind Alley": 71301024,
    "Rock-Paper-Scissors-Lizard-Spock": 71301025,
    "Hexamaze": 71301026,
    "Bitmaps": 71301027,
    "Colored Squares": 71301028,
    "Simon Screams": 71301029,
    "Wire Placement": 71301030,
    "Double-Oh": 71301031,
    "Cheap Checkout": 71301032,
    "FizzBuzz": 71301033,
    "Fast Math": 71301034,
    "Zoo": 71301035,
    "X-Ray": 71301036,
    "Color Morse": 71301037,
    "Big Circle": 71301038,
    "Morse-A-Maze": 71301039,
    "Polyhedral Maze": 71301040,
    "Blind Maze": 71301041,
    "Backgrounds": 71301042,
    "Radiator": 71301043
}

progression_skip_balancing_items = {
    "Bomb Fragment": 71301012,
    "Time++": 71301013
}

useful_items = {
    "Time+": 71301014,
    "Strike+": 71301015
}

filler_item = {
    "Empty Manual Page": 71301044
}

all_items_table = {
    **generic_vanilla_modules_table,
    **hardlock_specific_needies_table,
    **modded_modules_table,
    **progression_skip_balancing_items,
    **useful_items,
    **filler_item
}

modules_item_vanilla_nohl_table = {
    **generic_vanilla_modules_table
}

modules_item_vanilla_hl_table = {
    **generic_vanilla_modules_table,
    **hardlock_specific_needies_table
}

all_modules_table = {
    **generic_vanilla_modules_table,
    **hardlock_specific_needies_table,
    **modded_modules_table
}

progression_items_table = {
    **generic_vanilla_modules_table,
    **hardlock_specific_needies_table,
    **modded_modules_table,
    **progression_skip_balancing_items
}