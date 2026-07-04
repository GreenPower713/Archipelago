import typing
from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import KTANELocation, all_sections_completed_table, section1_table, section2_table, section3_table, section4_table, section5_table, section1m_table, section2m_table, section3m_table, section4m_table, section5m_table, section6m_table,section7m_table

def create_regions_generic(world: MultiWorld, player: int):
    world.regions.append(Region("Menu", player, world))

    # Bomb sections
    region_section_1: Region = Region("Section 1", player, world)
    region_section_1.locations += [KTANELocation(player, "Section 1 Completed",
                                                 all_sections_completed_table["Section 1 Completed"], region_section_1)]
    world.regions.append(region_section_1)

    region_section_2: Region = Region("Section 2", player, world)
    region_section_2.locations += [KTANELocation(player, "Section 2 Completed",
                                                 all_sections_completed_table["Section 2 Completed"], region_section_2)]
    world.regions.append(region_section_2)

    region_section_3: Region = Region("Section 3", player, world)
    region_section_3.locations += [KTANELocation(player, "Section 3 Completed",
                                                 all_sections_completed_table["Section 3 Completed"], region_section_3)]
    world.regions.append(region_section_3)

    region_section_4: Region = Region("Section 4", player, world)
    region_section_4.locations += [KTANELocation(player, "Section 4 Completed",
                                                 all_sections_completed_table["Section 4 Completed"], region_section_4)]
    world.regions.append(region_section_4)

    region_section_5: Region = Region("Section 5", player, world)
    region_section_5.locations += [KTANELocation(player, "Section 5 Completed",
                                                 all_sections_completed_table["Section 5 Completed"], region_section_5)]
    world.regions.append(region_section_5)


def create_regions_vanilla(world: MultiWorld, player: int):
    create_regions_generic(world, player)

    # Bomb sections
    region_section_6: Region = Region("Section 6", player, world)
    world.regions.append(region_section_6)

    # Bombs
    region_bomb_11: Region = Region("Bomb 1.1", player, world)
    for locationKey in [x for x in section1_table if x[0:3] == "1.1"]:
        location = KTANELocation(player, locationKey, section1_table[locationKey], region_bomb_11)
        region_bomb_11.locations += [location]
    world.regions.append(region_bomb_11)

    region_bomb_21: Region = Region("Bomb 2.1", player, world)
    for locationKey in [x for x in section2_table if x[0:3] == "2.1"]:
        location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_21)
        region_bomb_21.locations += [location]
    world.regions.append(region_bomb_21)

    region_bomb_22: Region = Region("Bomb 2.2", player, world)
    for locationKey in [x for x in section2_table if x[0:3] == "2.2"]:
        location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_22)
        region_bomb_22.locations += [location]
    world.regions.append(region_bomb_22)

    region_bomb_23: Region = Region("Bomb 2.3", player, world)
    for locationKey in [x for x in section2_table if x[0:3] == "2.3"]:
        location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_23)
        region_bomb_23.locations += [location]
    world.regions.append(region_bomb_23)

    region_bomb_24: Region = Region("Bomb 2.4", player, world)
    for locationKey in [x for x in section2_table if x[0:3] == "2.4"]:
        location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_24)
        region_bomb_24.locations += [location]
    world.regions.append(region_bomb_24)

    region_bomb_25: Region = Region("Bomb 2.5", player, world)
    for locationKey in [x for x in section2_table if x[0:3] == "2.5"]:
        location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_25)
        region_bomb_25.locations += [location]
    world.regions.append(region_bomb_25)

    region_bomb_26: Region = Region("Bomb 2.6", player, world)
    for locationKey in [x for x in section2_table if x[0:3] == "2.6"]:
        location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_26)
        region_bomb_26.locations += [location]
    world.regions.append(region_bomb_26)

    region_bomb_31: Region = Region("Bomb 3.1", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.1"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_31)
        region_bomb_31.locations += [location]
    world.regions.append(region_bomb_31)

    region_bomb_32: Region = Region("Bomb 3.2", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.2"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_32)
        region_bomb_32.locations += [location]
    world.regions.append(region_bomb_32)

    region_bomb_33: Region = Region("Bomb 3.3", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.3"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_33)
        region_bomb_33.locations += [location]
    world.regions.append(region_bomb_33)

    region_bomb_34: Region = Region("Bomb 3.4", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.4"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_34)
        region_bomb_34.locations += [location]
    world.regions.append(region_bomb_34)

    region_bomb_35: Region = Region("Bomb 3.5", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.5"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_35)
        region_bomb_35.locations += [location]
    world.regions.append(region_bomb_35)

    region_bomb_36: Region = Region("Bomb 3.6", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.6"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_36)
        region_bomb_36.locations += [location]
    world.regions.append(region_bomb_36)

    region_bomb_37: Region = Region("Bomb 3.7", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.7"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_37)
        region_bomb_37.locations += [location]
    world.regions.append(region_bomb_37)

    region_bomb_38: Region = Region("Bomb 3.8", player, world)
    for locationKey in [x for x in section3_table if x[0:3] == "3.8"]:
        location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_38)
        region_bomb_38.locations += [location]
    world.regions.append(region_bomb_38)

    region_bomb_41: Region = Region("Bomb 4.1", player, world)
    for locationKey in [x for x in section4_table if x[0:3] == "4.1"]:
        location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_41)
        region_bomb_41.locations += [location]
    world.regions.append(region_bomb_41)

    region_bomb_42: Region = Region("Bomb 4.2", player, world)
    for locationKey in [x for x in section4_table if x[0:3] == "4.2"]:
        location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_42)
        region_bomb_42.locations += [location]
    world.regions.append(region_bomb_42)

    region_bomb_43: Region = Region("Bomb 4.3", player, world)
    for locationKey in [x for x in section4_table if x[0:3] == "4.3"]:
        location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_43)
        region_bomb_43.locations += [location]
    world.regions.append(region_bomb_43)

    region_bomb_44: Region = Region("Bomb 4.4", player, world)
    for locationKey in [x for x in section4_table if x[0:3] == "4.4"]:
        location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_44)
        region_bomb_44.locations += [location]
    world.regions.append(region_bomb_44)

    region_bomb_51: Region = Region("Bomb 5.1", player, world)
    for locationKey in [x for x in section5_table if x[0:3] == "5.1"]:
        location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_51)
        region_bomb_51.locations += [location]
    world.regions.append(region_bomb_51)

    region_bomb_52: Region = Region("Bomb 5.2", player, world)
    for locationKey in [x for x in section5_table if x[0:3] == "5.2"]:
        location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_52)
        region_bomb_52.locations += [location]
    world.regions.append(region_bomb_52)

    region_bomb_53: Region = Region("Bomb 5.3", player, world)
    for locationKey in [x for x in section5_table if x[0:3] == "5.3"]:
        location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_53)
        region_bomb_53.locations += [location]
    world.regions.append(region_bomb_53)

    region_bomb_54: Region = Region("Bomb 5.4", player, world)
    for locationKey in [x for x in section5_table if x[0:3] == "5.4"]:
        location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_54)
        region_bomb_54.locations += [location]
    world.regions.append(region_bomb_54)

    region_bomb_55: Region = Region("Bomb 5.5", player, world)
    for locationKey in [x for x in section5_table if x[0:3] == "5.5"]:
        location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_55)
        region_bomb_55.locations += [location]
    world.regions.append(region_bomb_55)

    region_bomb_56: Region = Region("Bomb 5.6", player, world)
    for locationKey in [x for x in section5_table if x[0:3] == "5.6"]:
        location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_56)
        region_bomb_56.locations += [location]
    world.regions.append(region_bomb_56)

    world.regions.append(Region("Bomb 6.1", player, world))

def create_regions_modded(world: MultiWorld, player: int):
    create_regions_generic(world, player)

    # Bomb sections
    region_section_6: Region = Region("Section 6", player, world)
    region_section_6.locations += [KTANELocation(player, "Section 6 Completed",
                                                 all_sections_completed_table["Section 6 Completed"], region_section_6)]
    world.regions.append(region_section_6)

    region_section_7: Region = Region("Section 7", player, world)
    region_section_7.locations += [KTANELocation(player, "Section 7 Completed",
                                                 all_sections_completed_table["Section 7 Completed"], region_section_7)]
    world.regions.append(region_section_7)

    region_section_8: Region = Region("Section 8", player, world)
    world.regions.append(region_section_8)

    # Bombs
    region_bomb_11: Region = Region("Bomb 1.1", player, world)
    for locationKey in [x for x in section1m_table if x[0:3] == "1.1"]:
        location = KTANELocation(player, locationKey, section1m_table[locationKey], region_bomb_11)
        region_bomb_11.locations += [location]
    world.regions.append(region_bomb_11)

    region_bomb_21: Region = Region("Bomb 2.1", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.1"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_21)
        region_bomb_21.locations += [location]
    world.regions.append(region_bomb_21)

    region_bomb_22: Region = Region("Bomb 2.2", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.2"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_22)
        region_bomb_22.locations += [location]
    world.regions.append(region_bomb_22)

    region_bomb_23: Region = Region("Bomb 2.3", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.3"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_23)
        region_bomb_23.locations += [location]
    world.regions.append(region_bomb_23)

    region_bomb_24: Region = Region("Bomb 2.4", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.4"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_24)
        region_bomb_24.locations += [location]
    world.regions.append(region_bomb_24)

    region_bomb_25: Region = Region("Bomb 2.5", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.5"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_25)
        region_bomb_25.locations += [location]
    world.regions.append(region_bomb_25)

    region_bomb_26: Region = Region("Bomb 2.6", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.6"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_26)
        region_bomb_26.locations += [location]
    world.regions.append(region_bomb_26)

    region_bomb_27: Region = Region("Bomb 2.7", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.7"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_27)
        region_bomb_27.locations += [location]
    world.regions.append(region_bomb_27)

    region_bomb_28: Region = Region("Bomb 2.8", player, world)
    for locationKey in [x for x in section2m_table if x[0:3] == "2.8"]:
        location = KTANELocation(player, locationKey, section2m_table[locationKey], region_bomb_28)
        region_bomb_28.locations += [location]
    world.regions.append(region_bomb_28)

    region_bomb_31: Region = Region("Bomb 3.1", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.1"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_31)
        region_bomb_31.locations += [location]
    world.regions.append(region_bomb_31)

    region_bomb_32: Region = Region("Bomb 3.2", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.2"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_32)
        region_bomb_32.locations += [location]
    world.regions.append(region_bomb_32)

    region_bomb_33: Region = Region("Bomb 3.3", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.3"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_33)
        region_bomb_33.locations += [location]
    world.regions.append(region_bomb_33)

    region_bomb_34: Region = Region("Bomb 3.4", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.4"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_34)
        region_bomb_34.locations += [location]
    world.regions.append(region_bomb_34)

    region_bomb_35: Region = Region("Bomb 3.5", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.5"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_35)
        region_bomb_35.locations += [location]
    world.regions.append(region_bomb_35)

    region_bomb_36: Region = Region("Bomb 3.6", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.6"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_36)
        region_bomb_36.locations += [location]
    world.regions.append(region_bomb_36)

    region_bomb_37: Region = Region("Bomb 3.7", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.7"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_37)
        region_bomb_37.locations += [location]
    world.regions.append(region_bomb_37)

    region_bomb_38: Region = Region("Bomb 3.8", player, world)
    for locationKey in [x for x in section3m_table if x[0:3] == "3.8"]:
        location = KTANELocation(player, locationKey, section3m_table[locationKey], region_bomb_38)
        region_bomb_38.locations += [location]
    world.regions.append(region_bomb_38)

    region_bomb_41: Region = Region("Bomb 4.1", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.1"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_41)
        region_bomb_41.locations += [location]
    world.regions.append(region_bomb_41)

    region_bomb_42: Region = Region("Bomb 4.2", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.2"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_42)
        region_bomb_42.locations += [location]
    world.regions.append(region_bomb_42)

    region_bomb_43: Region = Region("Bomb 4.3", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.3"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_43)
        region_bomb_43.locations += [location]
    world.regions.append(region_bomb_43)

    region_bomb_44: Region = Region("Bomb 4.4", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.4"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_44)
        region_bomb_44.locations += [location]
    world.regions.append(region_bomb_44)

    region_bomb_45: Region = Region("Bomb 4.5", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.5"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_45)
        region_bomb_45.locations += [location]
    world.regions.append(region_bomb_45)

    region_bomb_46: Region = Region("Bomb 4.6", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.6"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_46)
        region_bomb_46.locations += [location]
    world.regions.append(region_bomb_46)

    region_bomb_47: Region = Region("Bomb 4.7", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.7"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_47)
        region_bomb_47.locations += [location]
    world.regions.append(region_bomb_47)

    region_bomb_48: Region = Region("Bomb 4.8", player, world)
    for locationKey in [x for x in section4m_table if x[0:3] == "4.8"]:
        location = KTANELocation(player, locationKey, section4m_table[locationKey], region_bomb_48)
        region_bomb_48.locations += [location]
    world.regions.append(region_bomb_48)

    region_bomb_51: Region = Region("Bomb 5.1", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.1"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_51)
        region_bomb_51.locations += [location]
    world.regions.append(region_bomb_51)

    region_bomb_52: Region = Region("Bomb 5.2", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.2"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_52)
        region_bomb_52.locations += [location]
    world.regions.append(region_bomb_52)

    region_bomb_53: Region = Region("Bomb 5.3", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.3"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_53)
        region_bomb_53.locations += [location]
    world.regions.append(region_bomb_53)

    region_bomb_54: Region = Region("Bomb 5.4", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.4"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_54)
        region_bomb_54.locations += [location]
    world.regions.append(region_bomb_54)

    region_bomb_55: Region = Region("Bomb 5.5", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.5"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_55)
        region_bomb_55.locations += [location]
    world.regions.append(region_bomb_55)

    region_bomb_56: Region = Region("Bomb 5.6", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.6"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_56)
        region_bomb_56.locations += [location]
    world.regions.append(region_bomb_56)

    region_bomb_57: Region = Region("Bomb 5.7", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.7"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_57)
        region_bomb_57.locations += [location]
    world.regions.append(region_bomb_57)

    region_bomb_58: Region = Region("Bomb 5.8", player, world)
    for locationKey in [x for x in section5m_table if x[0:3] == "5.8"]:
        location = KTANELocation(player, locationKey, section5m_table[locationKey], region_bomb_58)
        region_bomb_58.locations += [location]
    world.regions.append(region_bomb_58)

    region_bomb_61: Region = Region("Bomb 6.1", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.1"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_61)
        region_bomb_61.locations += [location]
    world.regions.append(region_bomb_61)

    region_bomb_62: Region = Region("Bomb 6.2", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.2"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_62)
        region_bomb_62.locations += [location]
    world.regions.append(region_bomb_62)

    region_bomb_63: Region = Region("Bomb 6.3", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.3"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_63)
        region_bomb_63.locations += [location]
    world.regions.append(region_bomb_63)

    region_bomb_64: Region = Region("Bomb 6.4", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.4"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_64)
        region_bomb_64.locations += [location]
    world.regions.append(region_bomb_64)

    region_bomb_65: Region = Region("Bomb 6.5", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.5"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_65)
        region_bomb_65.locations += [location]
    world.regions.append(region_bomb_65)

    region_bomb_66: Region = Region("Bomb 6.6", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.6"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_66)
        region_bomb_66.locations += [location]
    world.regions.append(region_bomb_66)

    region_bomb_67: Region = Region("Bomb 6.7", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.7"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_67)
        region_bomb_67.locations += [location]
    world.regions.append(region_bomb_67)

    region_bomb_68: Region = Region("Bomb 6.8", player, world)
    for locationKey in [x for x in section6m_table if x[0:3] == "6.8"]:
        location = KTANELocation(player, locationKey, section6m_table[locationKey], region_bomb_68)
        region_bomb_68.locations += [location]
    world.regions.append(region_bomb_68)

    region_bomb_71: Region = Region("Bomb 7.1", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.1"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_71)
        region_bomb_71.locations += [location]
    world.regions.append(region_bomb_71)

    region_bomb_72: Region = Region("Bomb 7.2", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.2"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_72)
        region_bomb_72.locations += [location]
    world.regions.append(region_bomb_72)

    region_bomb_73: Region = Region("Bomb 7.3", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.3"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_73)
        region_bomb_73.locations += [location]
    world.regions.append(region_bomb_73)

    region_bomb_74: Region = Region("Bomb 7.4", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.4"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_74)
        region_bomb_74.locations += [location]
    world.regions.append(region_bomb_74)

    region_bomb_75: Region = Region("Bomb 7.5", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.5"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_75)
        region_bomb_75.locations += [location]
    world.regions.append(region_bomb_75)

    region_bomb_76: Region = Region("Bomb 7.6", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.6"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_76)
        region_bomb_76.locations += [location]
    world.regions.append(region_bomb_76)

    region_bomb_77: Region = Region("Bomb 7.7", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.7"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_77)
        region_bomb_77.locations += [location]
    world.regions.append(region_bomb_77)

    region_bomb_78: Region = Region("Bomb 7.8", player, world)
    for locationKey in [x for x in section7m_table if x[0:3] == "7.8"]:
        location = KTANELocation(player, locationKey, section7m_table[locationKey], region_bomb_78)
        region_bomb_78.locations += [location]
    world.regions.append(region_bomb_78)

    world.regions.append(Region("Bomb 8.1", player, world))