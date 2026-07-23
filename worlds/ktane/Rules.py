import typing
from ..generic.Rules import add_rule
#from .Regions import v6areas

def getModuleCounts(state, _player, modListList):
    mod_count = 0
    pHas = state.has
    for modList in modListList:
        poolValue = 1
        if isinstance(modList[-1], int):
            poolValue = modList[-1]
            modList = modList[:-1]
        for mod in modList:
            if not pHas(mod, _player):
                break
        else:
            mod_count += poolValue
    return mod_count

def isAllFound(state, _player, itemList):
    for _item in itemList:
        if not state.has(_item, _player):
            return False
    return True

def set_rules_generic(multiworld, options, player):
    # sections rules
    menu_region = multiworld.get_region("Menu", player)
    section1_region = multiworld.get_region("Section 1", player)
    section2_region = multiworld.get_region("Section 2", player)
    section3_region = multiworld.get_region("Section 3", player)
    section4_region = multiworld.get_region("Section 4", player)
    section5_region = multiworld.get_region("Section 5", player)
    section6_region = multiworld.get_region("Section 6", player)

    menu_region.connect(connecting_region=section1_region, rule=lambda state: True)
    menu_region.connect(connecting_region=section2_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 1))
    menu_region.connect(connecting_region=section3_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 5))
    menu_region.connect(connecting_region=section4_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 15))
    menu_region.connect(connecting_region=section5_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 30))
    menu_region.connect(connecting_region=section6_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 50))

    # bomb rules
    section1_region.connect(connecting_region=multiworld.get_region("Bomb 1.1", player),
                            rule=lambda state: True)

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.1", player),
                            rule=lambda state: True)

def set_rules_vanilla(multiworld, options, player):
    set_rules_generic(multiworld, options, player)

    # hardlock_modules
    hardlock_modules = options.hardlock_modules.value

    # region variables
    section2_region = multiworld.get_region("Section 2", player)
    section3_region = multiworld.get_region("Section 3", player)
    section4_region = multiworld.get_region("Section 4", player)
    section5_region = multiworld.get_region("Section 5", player)
    section6_region = multiworld.get_region("Section 6", player)

    # bomb rules
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.2", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Simon Says", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.3", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Memory", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.4", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Maze", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.5", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Who's on First", player))

    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Says", player)
                                                    and state.has("Memory", player)
                                                    and state.has("Maze", player)
                                                    and state.has("Who's on First", player)
                                                    and state.has("Time++", player, 1)
                                                ))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.1", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Morse Code", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.2", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Password", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.3", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Complicated Wires", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.4", player),
                            rule=lambda state: (not hardlock_modules) or state.has("Wire Sequence", player))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Says", player)
                                                    and state.has("Memory", player)
                                                    and state.has("Maze", player)
                                                    and state.has("Who's on First", player)
                                                ))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Complicated Wires", player)
                                                    and state.has("Memory", player)
                                                    and state.has("Maze", player)
                                                    and state.has("Wire Sequence", player)
                                                    and state.has("Password", player)
                                                    and state.has("Morse Code", player)
                                                    and state.has("Time++", player, 1)
                                                ))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Complicated Wires", player)
                                                    and state.has("Wire Sequence", player)
                                                ))

    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Says", player)
                                                    and state.has("Maze", player)
                                                    and state.has("Morse Code", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Who's on First", player)
                                                    and state.has("Complicated Wires", player)
                                                    and state.has("Capacitor", player)
                                                    and state.has("Time++", player, 1)
                                                ))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Says", player)
                                                    and state.has("Memory", player)
                                                    and state.has("Vent Gas", player)
                                                    and state.has("Time++", player, 1)
                                                ))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Maze", player)
                                                    and state.has("Morse Code", player)
                                                    and state.has("Knob", player)
                                                    and state.has("Time++", player, 1)
                                                ))

    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Maze", player)
                                                    and state.has("Password", player)
                                                    and state.has("Complicated Wires", player)
                                                    and state.has("Wire Sequence", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Who's on First", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Maze", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Password", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Says", player)
                                                    and state.has("Morse Code", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Knob", player)
                                                    and state.has("Capacitor", player)
                                                    and state.has("Vent Gas", player)
                                                    and state.has("Who's on First", player)
                                                    and state.has("Maze", player)
                                                    and state.has("Password", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Complicated Wires", player)
                                                    and state.has("Simon Says", player)
                                                    and state.has("Wire Sequence", player)
                                                    and state.has("Time++", player, 2)
                                                ))

    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.1", player),
                            rule=lambda state: state.has("Knob", player)
                                               and (
                                                    (not hardlock_modules) or (
                                                        state.has("Capacitor", player)
                                                        and state.has("Vent Gas", player)
                                                    ))
                                               and state.has("Who's on First", player)
                                               and state.has("Maze", player)
                                               and state.has("Memory", player)
                                               and state.has("Simon Says", player)
                                               and state.has("Morse Code", player)
                                               and state.has("Password", player)
                                               and state.has("Complicated Wires", player)
                                               and state.has("Wire Sequence", player)
                                               and state.has("Time++", player, 7))

    # section completed rules
    add_rule(multiworld.get_location("Section 1 Completed", player),
             lambda state: state.can_reach("1.1 The First Challenge - 3 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 2 Completed", player),
             lambda state: state.can_reach("2.1 Make it Double - 6 Modules Solved", "Location", player)
                           and state.can_reach("2.2 Oh! The Lights! - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.3 Remember - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.4 Don't Get Lost - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.5 Confusion - 3 Modules Solved", "Location", player)
                           and state.can_reach("2.6 Speedster I - 3 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 3 Completed", player),
             lambda state: state.can_reach("3.1 Back in the 40s - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.2 Code Breaker - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.3 Verticality - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.4 Learning the Alphabet - 3 Modules Solved", "Location", player)
                           and state.can_reach("3.5 Precision Time - 4 Modules Solved", "Location", player)
                           and state.can_reach("3.6 Longer Bomb - 9 Modules Solved", "Location", player)
                           and state.can_reach("3.7 Rat Nest - 6 Modules Solved", "Location", player)
                           and state.can_reach("3.8 Speedster II - 5 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 4 Completed", player),
             lambda state: state.can_reach("4.1 Hold it! - 4 Modules Solved", "Location", player)
                           and state.can_reach("4.2 Master Hacker - 4 Modules Solved", "Location", player)
                           and state.can_reach("4.3 Wheel of Misfortune - 4 Modules Solved", "Location", player)
                           and state.can_reach("4.4 Speedster III - 4 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 5 Completed", player),
             lambda state: state.can_reach("5.1 Miscommunication - 4 Modules Solved", "Location", player)
                           and state.can_reach("5.2 Invisible Walls - 7 Modules Solved", "Location", player)
                           and state.can_reach("5.3 Cipher Decrypter - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.4 Stroboscopic - 6 Modules Solved", "Location", player)
                           and state.can_reach("5.5 Attention Needed - 5 Modules Solved", "Location", player)
                           and state.can_reach("5.6 Speedster IV - 4 Modules Solved", "Location", player))

    # hardlock modules rules
    if not hardlock_modules:

        # Section 2
        add_rule(multiworld.get_location("2.2 Oh! The Lights! - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Simon Says"]]) >= 1)
        add_rule(multiworld.get_location("2.3 Remember - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Memory"]]) >= 1)
        add_rule(multiworld.get_location("2.4 Don't Get Lost - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Maze"]]) >= 1)
        add_rule(multiworld.get_location("2.5 Confusion - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Who's on First"]]) >= 1)
        add_rule(multiworld.get_location("2.6 Speedster I - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Maze", "Who's on First"],
                     ["Memory"]
                 ]) >= 1)
        add_rule(multiworld.get_location("2.6 Speedster I - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Maze", "Who's on First"],
                     ["Memory"]
                 ]) >= 2 and state.has("Time++", player, 1))

        # Section 3
        add_rule(multiworld.get_location("3.1 Back in the 40s - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Morse Code"]]) >= 1)
        add_rule(multiworld.get_location("3.2 Code Breaker - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("3.3 Verticality - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Complicated Wires"]]) >= 1)
        add_rule(multiworld.get_location("3.4 Learning the Alphabet - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Wire Sequence"]]) >= 1)
        add_rule(multiworld.get_location("3.5 Precision Time - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Memory", "Maze", "Who's on First"]
                 ]) >= 1)
        add_rule(multiworld.get_location("3.5 Precision Time - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Memory", "Maze", "Who's on First"]
                 ]) >= 1)
        add_rule(multiworld.get_location("3.6 Longer Bomb - 5 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Morse Code"],
                     ["Memory", "Maze"],
                     ["Maze", "Complicated Wires"],
                     ["Wire Sequence", "Complicated Wires"],
                     ["Password"]
                 ]) >= 1)
        add_rule(multiworld.get_location("3.6 Longer Bomb - 6 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Morse Code"],
                     ["Memory", "Maze"],
                     ["Maze", "Complicated Wires"],
                     ["Wire Sequence", "Complicated Wires"],
                     ["Password"]
                 ]) >= 2)
        add_rule(multiworld.get_location("3.6 Longer Bomb - 7 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Morse Code"],
                     ["Memory", "Maze"],
                     ["Maze", "Complicated Wires"],
                     ["Wire Sequence", "Complicated Wires"],
                     ["Password"]
                 ]) >= 3)
        add_rule(multiworld.get_location("3.6 Longer Bomb - 8 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Morse Code"],
                     ["Memory", "Maze"],
                     ["Maze", "Complicated Wires"],
                     ["Wire Sequence", "Complicated Wires"],
                     ["Password"]
                 ]) >= 4 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("3.6 Longer Bomb - 9 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Morse Code"],
                     ["Memory", "Maze"],
                     ["Maze", "Complicated Wires"],
                     ["Wire Sequence", "Complicated Wires"],
                     ["Password"]
                 ]) >= 5 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("3.7 Rat Nest - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 1)
        add_rule(multiworld.get_location("3.7 Rat Nest - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 1)
        add_rule(multiworld.get_location("3.7 Rat Nest - 5 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 2)
        add_rule(multiworld.get_location("3.7 Rat Nest - 6 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 2)
        add_rule(multiworld.get_location("3.8 Speedster II - 4 Modules Solved", player),
                 lambda state: state.has("Time++", player, 1))
        add_rule(multiworld.get_location("3.8 Speedster II - 5 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Maze", "Morse Code"]
                 ]) >= 1 and state.has("Time++", player, 2))

        # Section 4
        add_rule(multiworld.get_location("4.1 Hold it! - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Who's on First", "Complicated Wires"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("4.2 Master Hacker - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Memory"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("4.3 Wheel of Misfortune - 1 Module Solved", player),
                 lambda state: state.has("Knob", player))
        add_rule(multiworld.get_location("4.3 Wheel of Misfortune - 2 Modules Solved", player),
                 lambda state: state.has("Knob", player))
        add_rule(multiworld.get_location("4.3 Wheel of Misfortune - 3 Modules Solved", player),
                 lambda state: state.has("Knob", player))
        add_rule(multiworld.get_location("4.3 Wheel of Misfortune - 4 Modules Solved", player),
                 lambda state: state.has("Knob", player) and getModuleCounts(state, player, [
                     ["Maze", "Morse Code"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("4.4 Speedster III - 2 Modules Solved", player),
                 lambda state: state.has("Time++", player, 1))
        add_rule(multiworld.get_location("4.4 Speedster III - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Maze", "Password"],
                     ["Complicated Wires", "Wire Sequence"]
                 ]) >= 1 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("4.4 Speedster III - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Maze", "Password"],
                     ["Complicated Wires", "Wire Sequence"]
                 ]) >= 2 and state.has("Time++", player, 2))

        # Section 5
        add_rule(multiworld.get_location("5.1 Miscommunication - 1 Module Solved", player),
                 lambda state: getModuleCounts(state, player, [["Who's on First"]]) >= 1)
        add_rule(multiworld.get_location("5.1 Miscommunication - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Who's on First"]]) >= 1)
        add_rule(multiworld.get_location("5.1 Miscommunication - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Who's on First"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.1 Miscommunication - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Who's on First"]
                 ]) >= 1 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.2 Invisible Walls - 1 Module Solved", player),
                 lambda state: getModuleCounts(state, player, [["Maze"]]) >= 1)
        add_rule(multiworld.get_location("5.2 Invisible Walls - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Maze"]]) >= 1)
        add_rule(multiworld.get_location("5.2 Invisible Walls - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Maze"]]) >= 1)
        add_rule(multiworld.get_location("5.2 Invisible Walls - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Maze"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.2 Invisible Walls - 5 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Maze"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.2 Invisible Walls - 6 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Maze"]
                 ]) >= 1 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.2 Invisible Walls - 7 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Maze"]
                 ]) >= 1 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 1 Module Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 5 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 6 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Password"]]) >= 1)
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 7 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Password"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 8 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Password"]
                 ]) >= 1 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.3 Cipher Decrypter - 9 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Password"]
                 ]) >= 1 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.4 Stroboscopic - 1 Module Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Morse Code"]
                 ]) >= 1)
        add_rule(multiworld.get_location("5.4 Stroboscopic - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Morse Code"]
                 ]) >= 1)
        add_rule(multiworld.get_location("5.4 Stroboscopic - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Morse Code"]
                 ]) >= 1)
        add_rule(multiworld.get_location("5.4 Stroboscopic - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Morse Code"]
                 ]) >= 2)
        add_rule(multiworld.get_location("5.4 Stroboscopic - 5 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Morse Code"]
                 ]) >= 2 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.4 Stroboscopic - 6 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Morse Code"]
                 ]) >= 2 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.5 Attention Needed - 1 Module Solved", player),
                 lambda state: state.has("Knob", player))
        add_rule(multiworld.get_location("5.5 Attention Needed - 2 Modules Solved", player),
                 lambda state: state.has("Knob", player))
        add_rule(multiworld.get_location("5.5 Attention Needed - 3 Modules Solved", player),
                 lambda state: state.has("Knob", player) and getModuleCounts(state, player, [
                     ["Maze"],
                     ["Password"],
                     ["Who's on First"]
                 ]) >= 1)
        add_rule(multiworld.get_location("5.5 Attention Needed - 4 Modules Solved", player),
                 lambda state: state.has("Knob", player) and getModuleCounts(state, player, [
                     ["Maze"],
                     ["Password"],
                     ["Who's on First"]
                 ]) >= 2 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.5 Attention Needed - 5 Modules Solved", player),
                 lambda state: state.has("Knob", player) and getModuleCounts(state, player, [
                     ["Maze"],
                     ["Password"],
                     ["Who's on First"]
                 ]) >= 3 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.6 Speedster IV - 1 Module Solved", player),
                 lambda state: state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.6 Speedster IV - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 1 and state.has("Time++", player, 1))
        add_rule(multiworld.get_location("5.6 Speedster IV - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 2 and state.has("Time++", player, 2))
        add_rule(multiworld.get_location("5.6 Speedster IV - 4 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says"],
                     ["Complicated Wires"],
                     ["Wire Sequence"]
                 ]) >= 3 and state.has("Time++", player, 2))

    # multiworld completion rule
    multiworld.completion_condition[player] = lambda state: state.can_reach("Bomb 6.1", 'Region', player)

def set_rules_modded(multiworld, options, player, finalChallengeComposition):
    set_rules_generic(multiworld, options, player)

    # hardlock_modules
    hardlock_modules = options.hardlock_modules.value

    # section rules
    menu_region = multiworld.get_region("Menu", player)
    section2_region = multiworld.get_region("Section 2", player)
    section3_region = multiworld.get_region("Section 3", player)
    section4_region = multiworld.get_region("Section 4", player)
    section5_region = multiworld.get_region("Section 5", player)
    section6_region = multiworld.get_region("Section 6", player)
    section7_region = multiworld.get_region("Section 7", player)
    section8_region = multiworld.get_region("Section 8", player)

    menu_region.connect(connecting_region=section7_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 70))
    menu_region.connect(connecting_region=section8_region,
                        rule=lambda state: state.has("Bomb Fragment", player, 100))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Switches", player)
                                                    and state.has("The Bulb", player)
                                                ))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Tic Tac Toe", player)
                                                    and state.has("Bitmaps", player)
                                                ))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Chess", player)
                                                    and state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Colored Squares", player)
                                                ))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Tic Tac Toe", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Colored Squares", player)
                                                ))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("The Bulb", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Chess", player)
                                                ))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Tic Tac Toe", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Colored Squares", player)
                                                ))
    
    section2_region.connect(connecting_region=multiworld.get_region("Bomb 2.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Chess", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("3D Maze", player)
                                                    and state.has("Mouse in the Maze", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Blind Alley", player)
                                                    and state.has("Follow the Leader", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Wire Placement", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("FizzBuzz", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Bitmaps", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Wire Placement", player)
                                                    and state.has("Double-Oh", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("FizzBuzz", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Switches", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("3D Maze", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Wire Placement", player)
                                                    and state.has("Follow the Leader", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Switches", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("3D Maze", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Follow the Leader", player)
                                                ))
    
    section3_region.connect(connecting_region=multiworld.get_region("Bomb 3.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Wire Placement", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Switches", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Hexamaze", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("3D Maze", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Cheap Checkout", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Friendship", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Cheap Checkout", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Zoo", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Hexamaze", player)
                                                    and state.has("Friendship", player)
                                                    and state.has("Cheap Checkout", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Wire Placement", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("3D Maze", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("3D Maze", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section4_region.connect(connecting_region=multiworld.get_region("Bomb 4.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("3D Maze", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Friendship", player)
                                                    and state.has("Mouse in the Maze", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Time++", player, 3)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Big Circle", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Backgrounds", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Blind Alley", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Wire Placement", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Friendship", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Cheap Checkout", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Friendship", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Big Circle", player)
                                                    and state.has("Blind Maze", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Big Circle", player)
                                                    and state.has("3D Maze", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("Mouse in the Maze", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Time++", player, 3)
                                                ))
    
    section5_region.connect(connecting_region=multiworld.get_region("Bomb 5.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Backgrounds", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Time++", player, 4)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Blind Maze", player)
                                                    and state.has("X-Ray", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Morse-A-Maze", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Cheap Checkout", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Color Morse", player)
                                                    and state.has("Big Circle", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("3D Maze", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Morse-A-Maze", player)
                                                    and state.has("Color Morse", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Big Circle", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Blind Maze", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Morse-A-Maze", player)
                                                    and state.has("3D Maze", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("Mouse in the Maze", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Color Morse", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Big Circle", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Cheap Checkout", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Time++", player, 1)
                                                ))
    
    section6_region.connect(connecting_region=multiworld.get_region("Bomb 6.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Big Circle", player)
                                                    and state.has("Backgrounds", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Switches", player)
                                                    and state.has("Chess", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Time++", player, 5)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.1", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Screams", player)
                                                    and state.has("Color Morse", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Wire Placement", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Backgrounds", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.2", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Simon Screams", player)
                                                    and state.has("Big Circle", player)
                                                    and state.has("X-Ray", player)
                                                    and state.has("Backgrounds", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Friendship", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.3", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Switches", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("Backgrounds", player)
                                                    and state.has("Big Circle", player)
                                                    and state.has("Color Morse", player)
                                                    and state.has("Friendship", player)
                                                    and state.has("Mouse in the Maze", player)
                                                    and state.has("Colored Squares", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.4", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Friendship", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.5", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Big Circle", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.6", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Blind Maze", player)
                                                    and state.has("X-Ray", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.7", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("Backgrounds", player)
                                                    and state.has("Color Morse", player)
                                                    and state.has("Mouse in the Maze", player)
                                                    and state.has("Morse-A-Maze", player)
                                                    and state.has("Time++", player, 2)
                                                ))
    
    section7_region.connect(connecting_region=multiworld.get_region("Bomb 7.8", player),
                            rule=lambda state: (not hardlock_modules) or (
                                                    state.has("3D Maze", player)
                                                    and state.has("Rock-Paper-Scissors-Lizard-Spock", player)
                                                    and state.has("The Bulb", player)
                                                    and state.has("Tic Tac Toe", player)
                                                    and state.has("Morse-A-Maze", player)
                                                    and state.has("Blind Alley", player)
                                                    and state.has("Blind Maze", player)
                                                    and state.has("Double-Oh", player)
                                                    and state.has("Mouse in the Maze", player)
                                                    and state.has("Big Circle", player)
                                                    and state.has("Radiator", player)
                                                    and state.has("Zoo", player)
                                                    and state.has("Wire Placement", player)
                                                    and state.has("FizzBuzz", player)
                                                    and state.has("Cheap Checkout", player)
                                                    and state.has("Fast Math", player)
                                                    and state.has("Polyhedral Maze", player)
                                                    and state.has("Bitmaps", player)
                                                    and state.has("Follow the Leader", player)
                                                    and state.has("Chess", player)
                                                    and state.has("Hexamaze", player)
                                                    and state.has("X-Ray", player)
                                                    and state.has("Simon Screams", player)
                                                    and state.has("Time++", player, 10)
                                                ))
    
    section8_region.connect(connecting_region=multiworld.get_region("Bomb 8.1", player),
                            rule=lambda state: isAllFound(state, player, finalChallengeComposition)
                            and state.has("Time++", player, 9))
    
    # section completed rules
    add_rule(multiworld.get_location("Section 1 Completed", player),
             lambda state: state.can_reach("1.1 First? - 11 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 2 Completed", player),
             lambda state: state.can_reach("2.1 Double Down - 22 Modules Solved", "Location", player)
                           and state.can_reach("2.2 What Are Those? - 8 Modules Solved", "Location", player)
                           and state.can_reach("2.3 Location of Success - 8 Modules Solved", "Location", player)
                           and state.can_reach("2.4 Family Fun - 8 Modules Solved", "Location", player)
                           and state.can_reach("2.5 Keep Talking - 8 Modules Solved", "Location", player)
                           and state.can_reach("2.6 Nobody Explodes - 8 Modules Solved", "Location", player)
                           and state.can_reach("2.7 Be Squared - 8 Modules Solved", "Location", player)
                           and state.can_reach("2.8 Quick Time Event I - 11 Modules Solved", "Location", player))
    
    add_rule(multiworld.get_location("Section 3 Completed", player),
             lambda state: state.can_reach("3.1 Lost - 8 Modules Solved", "Location", player)
                           and state.can_reach("3.2 Dark Path - 8 Modules Solved", "Location", player)
                           and state.can_reach("3.3 Shock - 8 Modules Solved", "Location", player)
                           and state.can_reach("3.4 Gin - 8 Modules Solved", "Location", player)
                           and state.can_reach("3.5 Stateful - 8 Modules Solved", "Location", player)
                           and state.can_reach("3.6 Vulture's Nest - 10 Modules Solved", "Location", player)
                           and state.can_reach("3.7 Colossal I - 23 Modules Solved", "Location", player)
                           and state.can_reach("3.8 Quick Time Event II - 11 Modules Solved", "Location", player))
    
    add_rule(multiworld.get_location("Section 4 Completed", player),
             lambda state: state.can_reach("4.1 Let Me In! - 8 Modules Solved", "Location", player)
                           and state.can_reach("4.2 In Your Head - 8 Modules Solved", "Location", player)
                           and state.can_reach("4.3 Magical - 8 Modules Solved", "Location", player)
                           and state.can_reach("4.4 Entrance - 8 Modules Solved", "Location", player)
                           and state.can_reach("4.5 Back in the 30s - 8 Modules Solved", "Location", player)
                           and state.can_reach("4.6 Vision - 8 Modules Solved", "Location", player)
                           and state.can_reach("4.7 Colossal II - 31 Modules Solved", "Location", player)
                           and state.can_reach("4.8 Quick Time Event III - 11 Modules Solved", "Location", player))
    
    add_rule(multiworld.get_location("Section 5 Completed", player),
             lambda state: state.can_reach("5.1 Grayscale - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.2 Insanity - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.3 Tales of Wonders - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.4 Disturbance - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.5 Commonplace - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.6 Unspoken - 9 Modules Solved", "Location", player)
                           and state.can_reach("5.7 Colossal III - 35 Modules Solved", "Location", player)
                           and state.can_reach("5.8 Quick Time Event IV - 15 Modules Solved", "Location", player))
    
    add_rule(multiworld.get_location("Section 6 Completed", player),
             lambda state: state.can_reach("6.1 Guidance - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.2 As Per Protocol - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.3 Knights - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.4 Pulsed - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.5 Walk in the Woods - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.6 Find Your Way - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.7 Forbidden - 9 Modules Solved", "Location", player)
                           and state.can_reach("6.8 Quick Time Event V - 15 Modules Solved", "Location", player))
    
    add_rule(multiworld.get_location("Section 7 Completed", player),
             lambda state: state.can_reach("7.1 Chromatic - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.2 Let's Cook! - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.3 The Green Power - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.4 Company - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.5 A Good Trick - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.6 Fight! - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.7 Conic Conductor - 11 Modules Solved", "Location", player)
                           and state.can_reach("7.8 Gargantua - 39 Modules Solved", "Location", player))
    
    # hardlock module off rules
    if not hardlock_modules:
        # Section 2
        vanillaModules = 6
        for i in range(1, 3):
            add_rule(multiworld.get_location("2.2 What Are Those? - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Switches"],
                     ["The Bulb"]
                 ]) >= i)
        vanillaModules = 6
        for i in range(1, 3):
            add_rule(multiworld.get_location("2.3 Location of Success - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Tic Tac Toe"],
                     ["Bitmaps"]
                 ]) >= i)
        vanillaModules = 5
        for i in range(1, 4):
            add_rule(multiworld.get_location("2.4 Family Fun - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Chess"],
                     ["Rock-Paper-Scissors-Lizard-Spock"],
                     ["Colored Squares"]
                 ]) >= i)
        vanillaModules = 5
        for i in range(1, 4):
            add_rule(multiworld.get_location("2.5 Keep Talking - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Tic Tac Toe"],
                     ["Switches"],
                     ["Colored Squares"]
                 ]) >= i)
        vanillaModules = 5
        for i in range(1, 4):
            add_rule(multiworld.get_location("2.6 Nobody Explodes - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["The Bulb"],
                     ["Bitmaps"],
                     ["Chess"]
                 ]) >= i)
        vanillaModules = 2
        for i in range(1, 7):
            add_rule(multiworld.get_location("2.7 Be Squared - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Tic Tac Toe"],
                     ["Bitmaps"],
                     ["Colored Squares"]
                 ]) >= (i+1)//2)
        vanillaModules = 7
        for i in range(1, 5):
            if i >= 3:
                add_rule(multiworld.get_location("2.8 Quick Time Event I - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Colored Squares"],
                        ["The Bulb", "Chess"],
                        ["Switches", "Chess"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("2.8 Quick Time Event I - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Colored Squares"],
                        ["The Bulb", "Chess"],
                        ["Switches", "Chess"]
                    ]) >= i)
        
        # Section 3
        vanillaModules = 6
        for i in range(1, 3):
            add_rule(multiworld.get_location("3.1 Lost - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["3D Maze"],
                     ["Mouse in the Maze"]
                 ]) >= i)
        vanillaModules = 6
        for i in range(1, 3):
            add_rule(multiworld.get_location("3.2 Dark Path - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Blind Alley"],
                     ["Follow the Leader"]
                 ]) >= i)
        vanillaModules = 5
        for i in range(1, 4):
            add_rule(multiworld.get_location("3.3 Shock - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Double-Oh"],
                     ["Wire Placement"],
                     ["FizzBuzz"]
                 ]) >= i)
        vanillaModules = 4
        for i in range(1, 5):
            add_rule(multiworld.get_location("3.4 Gin - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Bitmaps"],
                     ["Colored Squares"],
                     ["Wire Placement"],
                     ["Double-Oh"]
                 ]) >= i)
        vanillaModules = 2
        for i in range(1, 7):
            add_rule(multiworld.get_location("3.5 Stateful - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["FizzBuzz"],
                     ["Double-Oh"],
                     ["Bitmaps"],
                     ["Switches"],
                     ["The Bulb"],
                     ["3D Maze"]
                 ]) >= i)
        vanillaModules = 6
        for i in range(1, 5):
            add_rule(multiworld.get_location("3.6 Vulture's Nest - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Follow the Leader"],
                     ["Wire Placement"]
                 ]) >= (i+1)//2)
        vanillaModules = 10
        for i in range(1, 14):
            add_rule(multiworld.get_location("3.7 Colossal I - " + str(i+vanillaModules) + " Modules Solved", player),
                 lambda state, i=i: getModuleCounts(state, player, [
                     ["Switches"],
                     ["The Bulb"],
                     ["Bitmaps", 2],
                     ["Double-Oh"],
                     ["FizzBuzz", 2],
                     ["3D Maze"],
                     ["Chess", 2],
                     ["Tic Tac Toe"],
                     ["Colored Squares"],
                     ["Follow the Leader"]
                 ]) >= i)
        vanillaModules = 4
        for i in range(1, 8):
            if i >= 5:
                reqTime = 2 if i >= 6 else 1
                add_rule(multiworld.get_location("3.8 Quick Time Event II - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Colored Squares"],
                        ["Blind Alley"],
                        ["Wire Placement"],
                        ["Double-Oh"],
                        ["Switches"],
                        ["The Bulb"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("3.8 Quick Time Event II - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Colored Squares"],
                        ["Blind Alley"],
                        ["Wire Placement"],
                        ["Double-Oh"],
                        ["Switches"],
                        ["The Bulb"]
                    ]) >= i)
        
        # Section 4
        vanillaModules = 5
        for i in range(1, 4):
            if i >= 2:
                add_rule(multiworld.get_location("4.1 Let Me In! - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Hexamaze"],
                        ["Simon Screams"],
                        ["3D Maze"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("4.1 Let Me In! - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Hexamaze"],
                        ["Simon Screams"],
                        ["3D Maze"]
                    ]) >= i)
        vanillaModules = 5
        for i in range(1, 4):
            if i >= 2:
                add_rule(multiworld.get_location("4.2 In Your Head - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Cheap Checkout"],
                        ["Fast Math"],
                        ["FizzBuzz"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("4.2 In Your Head - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Cheap Checkout"],
                        ["Fast Math"],
                        ["FizzBuzz"]
                    ]) >= i)
        vanillaModules = 5
        for i in range(1, 4):
            if i >= 2:
                add_rule(multiworld.get_location("4.3 Magical - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Friendship"],
                        ["Zoo"],
                        ["Chess"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("4.3 Magical - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Friendship"],
                        ["Zoo"],
                        ["Chess"]
                    ]) >= i)
        vanillaModules = 4
        for i in range(1, 5):
            if i >= 3:
                add_rule(multiworld.get_location("4.4 Entrance - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Cheap Checkout"],
                        ["Zoo"],
                        ["Blind Alley"],
                        ["Mouse in the Maze"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("4.4 Entrance - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Cheap Checkout"],
                        ["Zoo"],
                        ["Blind Alley"],
                        ["Mouse in the Maze"]
                    ]) >= i)
        vanillaModules = 2
        for i in range(1, 7):
            if i >= 5:
                add_rule(multiworld.get_location("4.5 Back in the 30s - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Zoo"],
                        ["Double-Oh", 3],
                        ["Follow the Leader"],
                        ["Colored Squares"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("4.5 Back in the 30s - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Zoo"],
                        ["Double-Oh", 3],
                        ["Follow the Leader"],
                        ["Colored Squares"]
                    ]) >= i)
        vanillaModules = 1
        for i in range(1, 8):
            if i >= 6:
                add_rule(multiworld.get_location("4.6 Vision - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Hexamaze"],
                        ["Friendship"],
                        ["Cheap Checkout"],
                        ["FizzBuzz"],
                        ["Wire Placement"],
                        ["Blind Maze"],
                        ["3D Maze"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("4.6 Vision - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Hexamaze"],
                        ["Friendship"],
                        ["Cheap Checkout"],
                        ["FizzBuzz"],
                        ["Wire Placement"],
                        ["Blind Maze"],
                        ["3D Maze"]
                    ]) >= i)
        vanillaModules = 12
        for i in range(1, 20):
            if i >= 16:
                reqTime = 2 if i >= 18 else 1
                add_rule(multiworld.get_location("4.7 Colossal II - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["3D Maze"],
                        ["Blind Alley", 2],
                        ["The Bulb"],
                        ["Chess", 2],
                        ["Colored Squares", 3],
                        ["Double-Oh"],
                        ["Follow the Leader"],
                        ["Hexamaze", 3],
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Switches", 2],
                        ["Tic Tac Toe", 2]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("4.7 Colossal II - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["3D Maze"],
                        ["Blind Alley", 2],
                        ["The Bulb"],
                        ["Chess", 2],
                        ["Colored Squares", 3],
                        ["Double-Oh"],
                        ["Follow the Leader"],
                        ["Hexamaze", 3],
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Switches", 2],
                        ["Tic Tac Toe", 2]
                    ]) >= i)
        vanillaModules = 3
        for i in range(1, 9):
            if i >= 5:
                reqTime = 3 if i >= 8 else (2 if i >= 6 else 1)
                add_rule(multiworld.get_location("4.8 Quick Time Event III - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["3D Maze"],
                        ["Bitmaps"],
                        ["Chess"],
                        ["Colored Squares"],
                        ["Friendship"],
                        ["Mouse in the Maze"],
                        ["Simon Screams"],
                        ["Zoo"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("4.8 Quick Time Event III - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["3D Maze"],
                        ["Bitmaps"],
                        ["Chess"],
                        ["Colored Squares"],
                        ["Friendship"],
                        ["Mouse in the Maze"],
                        ["Simon Screams"],
                        ["Zoo"]
                    ]) >= i)
        
        # Section 5
        vanillaModules = 4
        for i in range(1, 6):
            if i >= 5:
                add_rule(multiworld.get_location("5.1 Grayscale - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Big Circle"],
                        ["Polyhedral Maze"],
                        ["Colored Squares"],
                        ["Hexamaze"],
                        ["Follow the Leader"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("5.1 Grayscale - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Big Circle"],
                        ["Polyhedral Maze"],
                        ["Colored Squares"],
                        ["Hexamaze"],
                        ["Follow the Leader"]
                    ]) >= i)
        vanillaModules = 3
        for i in range(1, 7):
            if i >= 5:
                add_rule(multiworld.get_location("5.2 Insanity - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Backgrounds"],
                        ["Radiator"],
                        ["Fast Math"],
                        ["Colored Squares"],
                        ["Tic Tac Toe"],
                        ["Simon Screams"]
                    ]) >= i and state.has("Time++"), player, 1)
            else:
                add_rule(multiworld.get_location("5.2 Insanity - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Backgrounds"],
                        ["Radiator"],
                        ["Fast Math"],
                        ["Colored Squares"],
                        ["Tic Tac Toe"],
                        ["Simon Screams"]
                    ]) >= i)
        vanillaModules = 3
        for i in range(1, 7):
            if i >= 6:
                add_rule(multiworld.get_location("5.3 Tales of Wonders - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Alley"],
                        ["Polyhedral Maze"]
                    ]) >= (i+2)//3 and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("5.3 Tales of Wonders - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Alley"],
                        ["Polyhedral Maze"]
                    ]) >= (i+2)//3)
        vanillaModules = 3
        for i in range(1, 7):
            if i >= 6:
                add_rule(multiworld.get_location("5.4 Disturbance - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Wire Placement"],
                        ["Tic Tac Toe"],
                        ["Follow the Leader"],
                        ["Friendship"],
                        ["FizzBuzz"],
                        ["Fast Math"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("5.4 Disturbance - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Wire Placement"],
                        ["Tic Tac Toe"],
                        ["Follow the Leader"],
                        ["Friendship"],
                        ["FizzBuzz"],
                        ["Fast Math"]
                    ]) >= i)
        vanillaModules = 2
        for i in range(1, 8):
            if i >= 7:
                add_rule(multiworld.get_location("5.5 Commonplace - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Cheap Checkout"],
                        ["Radiator"],
                        ["Zoo"],
                        ["The Bulb"],
                        ["Switches"],
                        ["Friendship"],
                        ["Fast Math"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("5.5 Commonplace - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Cheap Checkout"],
                        ["Radiator"],
                        ["Zoo"],
                        ["The Bulb"],
                        ["Switches"],
                        ["Friendship"],
                        ["Fast Math"]
                    ]) >= i)
        vanillaModules = 0
        for i in range(1, 10):
            if i >= 9:
                add_rule(multiworld.get_location("5.6 Unspoken - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Radiator"],
                        ["Big Circle"],
                        ["Blind Alley"]
                    ]) >= (i+2)//3 and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("5.6 Unspoken - " + str(i+vanillaModules) + " Module" + ("" if i == 1 else "s") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Radiator"],
                        ["Big Circle"],
                        ["Blind Alley"]
                    ]) >= (i+2)//3)
        vanillaModules = 7
        for i in range(1, 29):
            if i >= 26:
                reqTime = 3 if i >= 28 else (2 if i >= 27 else 1)
                add_rule(multiworld.get_location("5.7 Colossal III - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["3D Maze"],
                        ["Big Circle"],
                        ["Bitmaps", 2],
                        ["Blind Alley"],
                        ["Chess", 2],
                        ["Colored Squares", 2],
                        ["Double-Oh"],
                        ["Fast Math"],
                        ["FizzBuzz", 2],
                        ["Follow the Leader", 2],
                        ["Friendship", 2],
                        ["Hexamaze", 2],
                        ["Mouse in the Maze"],
                        ["Polyhedral Maze", 3],
                        ["Rock-Paper-Scissors-Lizard-Spock", 2],
                        ["Radiator"],
                        ["Switches", 2]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("5.7 Colossal III - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["3D Maze"],
                        ["Big Circle"],
                        ["Bitmaps", 2],
                        ["Blind Alley"],
                        ["Chess", 2],
                        ["Colored Squares", 2],
                        ["Double-Oh"],
                        ["Fast Math"],
                        ["FizzBuzz", 2],
                        ["Follow the Leader", 2],
                        ["Friendship", 2],
                        ["Hexamaze", 2],
                        ["Mouse in the Maze"],
                        ["Polyhedral Maze", 3],
                        ["Rock-Paper-Scissors-Lizard-Spock", 2],
                        ["Radiator"],
                        ["Switches", 2]
                    ]) >= i)
        vanillaModules = 4
        for i in range(1, 12):
            if i >= 6:
                reqTime = 1
                if i >= 11:
                    reqTime = 4
                elif i >= 9:
                    reqTime = 3
                elif i >= 8:
                    reqTime = 2
                add_rule(multiworld.get_location("5.8 Quick Time Event IV - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Backgrounds"],
                        ["Blind Alley", 2],
                        ["Follow the Leader"],
                        ["Hexamaze"],
                        ["Polyhedral Maze"],
                        ["Radiator"],
                        ["Simon Screams"],
                        ["Switches"],
                        ["Tic Tac Toe"],
                        ["Zoo"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("5.8 Quick Time Event IV - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Backgrounds"],
                        ["Blind Alley", 2],
                        ["Follow the Leader"],
                        ["Hexamaze"],
                        ["Polyhedral Maze"],
                        ["Radiator"],
                        ["Simon Screams"],
                        ["Switches"],
                        ["Tic Tac Toe"],
                        ["Zoo"]
                    ]) >= i)
        
        # Section 6
        vanillaModules = 3
        for i in range(1, 7):
            if i >= 6:
                add_rule(multiworld.get_location("6.1 Guidance - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Maze"],
                        ["X-Ray"],
                        ["Blind Alley", 2],
                        ["Follow the Leader"],
                        ["FizzBuzz"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.1 Guidance - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Maze"],
                        ["X-Ray"],
                        ["Blind Alley", 2],
                        ["Follow the Leader"],
                        ["FizzBuzz"]
                    ]) >= i)
        vanillaModules = 1
        for i in range(1, 9):
            if i>=8:
                add_rule(multiworld.get_location("6.2 As Per Protocol - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Morse-A-Maze", 2],
                        ["Zoo"],
                        ["Radiator"],
                        ["Fast Math"],
                        ["Cheap Checkout"],
                        ["Blind Alley"],
                        ["Rock-Paper-Scissors-Lizard-Spock"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.2 As Per Protocol - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Morse-A-Maze", 2],
                        ["Zoo"],
                        ["Radiator"],
                        ["Fast Math"],
                        ["Cheap Checkout"],
                        ["Blind Alley"],
                        ["Rock-Paper-Scissors-Lizard-Spock"]
                    ]) >= i)
        vanillaModules = 2
        for i in range(1, 8):
            if i >= 7:
                add_rule(multiworld.get_location("6.3 Knights - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Color Morse"],
                        ["Big Circle"],
                        ["Zoo"],
                        ["Simon Screams"],
                        ["FizzBuzz"],
                        ["3D Maze"],
                        ["Tic Tac Toe"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.3 Knights - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Color Morse"],
                        ["Big Circle"],
                        ["Zoo"],
                        ["Simon Screams"],
                        ["FizzBuzz"],
                        ["3D Maze"],
                        ["Tic Tac Toe"]
                    ]) >= i)
        vanillaModules = 3
        for i in range(1, 7):
            if i >= 6:
                add_rule(multiworld.get_location("6.4 Pulsed - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Morse-A-Maze"],
                        ["Color Morse"],
                        ["Simon Screams"]
                    ]) >= (i+1)//2 and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.4 Pulsed - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Morse-A-Maze"],
                        ["Color Morse"],
                        ["Simon Screams"]
                    ]) >= (i+1)//2)
        vanillaModules = 2
        for i in range(1, 8):
            if i >= 7:
                add_rule(multiworld.get_location("6.5 Walk in the Woods - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Big Circle"],
                        ["Radiator"],
                        ["Fast Math"],
                        ["Simon Screams"],
                        ["Follow the Leader", 2],
                        ["Colored Squares"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.5 Walk in the Woods - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Big Circle"],
                        ["Radiator"],
                        ["Fast Math"],
                        ["Simon Screams"],
                        ["Follow the Leader", 2],
                        ["Colored Squares"]
                    ]) >= i)
        vanillaModules = 1
        for i in range(1, 9):
            if i >= 8:
                add_rule(multiworld.get_location("6.6 Find Your Way - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Maze"],
                        ["Polyhedral Maze"],
                        ["Morse-A-Maze"],
                        ["3D Maze"],
                        ["Hexamaze"],
                        ["Mouse in the Maze"],
                        ["3D Maze", "Mouse in the Maze"],
                        ["Hexamaze", "Polyhedral Maze"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.6 Find Your Way - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Maze"],
                        ["Polyhedral Maze"],
                        ["Morse-A-Maze"],
                        ["3D Maze"],
                        ["Hexamaze"],
                        ["Mouse in the Maze"],
                        ["3D Maze", "Mouse in the Maze"],
                        ["Hexamaze", "Polyhedral Maze"]
                    ]) >= i)
        vanillaModules = 0
        for i in range(1, 10):
            if i >= 9:
                add_rule(multiworld.get_location("6.7 Forbidden - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Color Morse"],
                        ["Radiator", 2],
                        ["Big Circle"],
                        ["Fast Math", 2],
                        ["Cheap Checkout"],
                        ["FizzBuzz"],
                        ["Polyhedral Maze", "Double-Oh", "Bitmaps"]
                    ]) >= i and state.has("Time++", player, 1))
            else:
                add_rule(multiworld.get_location("6.7 Forbidden - " + str(i+vanillaModules) + " Module" + ("s" if i>=2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Color Morse"],
                        ["Radiator", 2],
                        ["Big Circle"],
                        ["Fast Math", 2],
                        ["Cheap Checkout"],
                        ["FizzBuzz"],
                        ["Polyhedral Maze", "Double-Oh", "Bitmaps"]
                    ]) >= i)
        vanillaModules = 3
        for i in range(1, 13):
            if i >= 7:
                reqTime = 1
                if i >= 12:
                    reqTime = 5
                elif i >= 11:
                    reqTime = 4
                elif i >= 10:
                    reqTime = 3
                elif i >= 9:
                    reqTime = 2
                add_rule(multiworld.get_location("6.8 Quick Time Event V - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Blind Alley", 2],
                        ["Big Circle"],
                        ["Backgrounds"],
                        ["Fast Math", 2],
                        ["Switches"],
                        ["The Bulb"],
                        ["Bitmaps"],
                        ["Polyhedral Maze"],
                        ["Follow the Leader"],
                        ["Chess"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("6.8 Quick Time Event V - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Alley", 2],
                        ["Big Circle"],
                        ["Backgrounds"],
                        ["Fast Math", 2],
                        ["Switches"],
                        ["The Bulb"],
                        ["Bitmaps"],
                        ["Polyhedral Maze"],
                        ["Follow the Leader"],
                        ["Chess"]
                    ]) >= i)
        
        # Section 7
        vanillaModules = 1
        for i in range(1, 11):
            if i >= 9:
                reqTime = (2 if i >= 10 else 1)
                add_rule(multiworld.get_location("7.1 Chromatic - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Simon Screams", 2],
                        ["Color Morse", 2],
                        ["Colored Squares", 2],
                        ["Wire Placement"],
                        ["The Bulb"],
                        ["FizzBuzz"],
                        ["Backgrounds"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.1 Chromatic - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Simon Screams", 2],
                        ["Color Morse", 2],
                        ["Colored Squares", 2],
                        ["Wire Placement"],
                        ["The Bulb"],
                        ["FizzBuzz"],
                        ["Backgrounds"]
                    ]) >= i)
        vanillaModules = 0
        for i in range(1, 12):
            if i >= 10:
                reqTime = (2 if i >= 11 else 1)
                add_rule(multiworld.get_location("7.2 Let's Cook! - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Big Circle"],
                        ["X-Ray"],
                        ["Backgrounds"],
                        ["Fast Math"],
                        ["Simon Screams"],
                        ["Friendship"],
                        ["FizzBuzz"],
                        ["Double-Oh"],
                        ["Colored Squares"],
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Tic Tac Toe"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.2 Let's Cook! - " + str(i+vanillaModules) + " Module" + ("s" if i >= 2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Big Circle"],
                        ["X-Ray"],
                        ["Backgrounds"],
                        ["Fast Math"],
                        ["Simon Screams"],
                        ["Friendship"],
                        ["FizzBuzz"],
                        ["Double-Oh"],
                        ["Colored Squares"],
                        ["Rock-Paper-Scissors-Lizard-Spock"],
                        ["Tic Tac Toe"]
                    ]) >= i)
        vanillaModules = 2
        for i in range(1, 10):
            if i >= 8:
                reqTime = 2 if i >= 9 else 1
                add_rule(multiworld.get_location("7.3 The Green Power - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Switches"],
                        ["Chess"],
                        ["Hexamaze"],
                        ["Backgrounds"],
                        ["Big Circle"],
                        ["Color Morse"],
                        ["Friendship"],
                        ["Mouse in the Maze"],
                        ["Colored Squares"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.3 The Green Power - " + str(i+vanillaModules) + " Modules Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Switches"],
                        ["Chess"],
                        ["Hexamaze"],
                        ["Backgrounds"],
                        ["Big Circle"],
                        ["Color Morse"],
                        ["Friendship"],
                        ["Mouse in the Maze"],
                        ["Colored Squares"]
                    ]) >= i)
        for i in range(1, 12):
            if i >= 10:
                reqTime = 2 if i >= 11 else 1
                add_rule(multiworld.get_location("7.4 Company - " + str(i) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Friendship", 6],
                        ["Zoo", 5]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.4 Company - " + str(i) + " Module" + ("s" if i >= 2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Friendship", 6],
                        ["Zoo", 5]
                    ]) >= i)
        for i in range(1, 12):
            if i >= 10:
                reqTime = 2 if i >= 11 else 1
                add_rule(multiworld.get_location("7.5 A Good Trick - " + str(i) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Big Circle", 6],
                        ["The Bulb", 5]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.5 A Good Trick - " + str(i) + " Module" + ("s" if i >= 2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Big Circle", 6],
                        ["The Bulb", 5]
                    ]) >= i)
        for i in range(1, 12):
            if i >= 10:
                reqTime = 2 if i >= 11 else 1
                add_rule(multiworld.get_location("7.6 Fight! - " + str(i) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Blind Maze", 6],
                        ["X-Ray", 5]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.6 Fight! - " + str(i) + " Module" + ("s" if i >= 2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Blind Maze", 6],
                        ["X-Ray", 5]
                    ]) >= i)
        for i in range(1, 12):
            if i >= 10:
                reqTime = 2 if i >= 11 else 1
                add_rule(multiworld.get_location("7.7 Conic Conductor - " + str(i) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["Backgrounds", 3],
                        ["Color Morse", 3],
                        ["Mouse in the Maze", 3],
                        ["Morse-A-Maze", 2]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.7 Conic Conductor - " + str(i) + " Module" + ("s" if i >= 2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["Backgrounds", 3],
                        ["Color Morse", 3],
                        ["Mouse in the Maze", 3],
                        ["Morse-A-Maze", 2]
                    ]) >= i)
        for i in range(1, 40):
            if i >= 30:
                reqTime = i-29
                add_rule(multiworld.get_location("7.8 Gargantua - " + str(i) + " Modules Solved", player),
                    lambda state, i=i, reqTime=reqTime: getModuleCounts(state, player, [
                        ["3D Maze", 4],
                        ["Rock-Paper-Scissors-Lizard-Spock", 3],
                        ["The Bulb", 3],
                        ["Tic Tac Toe", 3],
                        ["Morse-A-Maze", 3],
                        ["Blind Alley", 2],
                        ["Blind Maze", 2],
                        ["Double-Oh", 2],
                        ["Mouse in the Maze", 2],
                        ["Big Circle", 2],
                        ["Radiator"],
                        ["Zoo"],
                        ["Wire Placement"],
                        ["FizzBuzz"],
                        ["Cheap Checkout"],
                        ["Fast Math"],
                        ["Polyhedral Maze"],
                        ["Bitmaps"],
                        ["Follow the Leader"],
                        ["Chess"],
                        ["Hexamaze"],
                        ["X-Ray"],
                        ["Simon Screams"]
                    ]) >= i and state.has("Time++", player, reqTime))
            else:
                add_rule(multiworld.get_location("7.8 Gargantua - " + str(i) + " Module" + ("s" if i >= 2 else "") + " Solved", player),
                    lambda state, i=i: getModuleCounts(state, player, [
                        ["3D Maze", 4],
                        ["Rock-Paper-Scissors-Lizard-Spock", 3],
                        ["The Bulb", 3],
                        ["Tic Tac Toe", 3],
                        ["Morse-A-Maze", 3],
                        ["Blind Alley", 2],
                        ["Blind Maze", 2],
                        ["Double-Oh", 2],
                        ["Mouse in the Maze", 2],
                        ["Big Circle", 2],
                        ["Radiator"],
                        ["Zoo"],
                        ["Wire Placement"],
                        ["FizzBuzz"],
                        ["Cheap Checkout"],
                        ["Fast Math"],
                        ["Polyhedral Maze"],
                        ["Bitmaps"],
                        ["Follow the Leader"],
                        ["Chess"],
                        ["Hexamaze"],
                        ["X-Ray"],
                        ["Simon Screams"]
                    ]) >= i)

    # multiworld completion rule
    multiworld.completion_condition[player] = lambda state: state.can_reach("Bomb 8.1", 'Region', player)