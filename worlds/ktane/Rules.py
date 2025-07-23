import typing
from ..generic.Rules import add_rule
#from .Regions import v6areas


def set_rules(multiworld, options, player):

    #hardlock_modules
    hardlock_modules = self.options.hardlock_modules.value

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
                                               and state.has("Time++", player, 6))

    # section completed rules
    add_rule(multiworld.get_location("Section 1 Completed", player),
             lambda state: state.can_reach("1.1 The First Challenge - 3 Modules Solved", "Location", player))

    add_rule(multiworld.get_location("Section 2 Completed", player),
             lambda state: state.can_reach("2.1 Double Trouble - 6 Modules Solved", "Location", player)
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
        def getModuleCounts(state, _player, modListList):
            mod_count = 0
            for modList in modListList:
                all_pool_modules = True
                for mod in modList:
                    if not state.has(mod, _player):
                        all_pool_modules = False
                        break
                if all_pool_modules:
                    mod_count += 1
            return mod_count

        # Section 2
        add_rule(multiworld.get_location("2.2 Oh! The Lights! - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Simon Says"]]) >= 1)
        add_rule(multiworld.get_location("2.3 Remember - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Memory"]]) >= 1)
        add_rule(multiworld.get_location("2.4 Don't Get Lost - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Maze"]]) >= 1)
        add_rule(multiworld.get_location("2.5 Confusion - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [["Who's on First"]]) >= 1)
        add_rule(multiworld.get_location("2.6 Speedster I - 1 Module Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Memory", "Maze", "Who's on First"]
                 ]) >= 1)
        add_rule(multiworld.get_location("2.6 Speedster I - 2 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Memory", "Maze", "Who's on First"]
                 ]) >= 1)
        add_rule(multiworld.get_location("2.6 Speedster I - 3 Modules Solved", player),
                 lambda state: getModuleCounts(state, player, [
                     ["Simon Says", "Memory", "Maze", "Who's on First"]
                 ]) >= 1 and state.has("Time++", player, 1))

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
