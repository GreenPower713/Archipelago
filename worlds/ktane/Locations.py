from BaseClasses import Location


class KTANELocation(Location):
    game: str = "Keep Talking and Nobody Explodes"

# Name classification:
# 713 01 001
# 713 Auth
# 01 Game
# 001 locationID

section1_table = {
    "1.1 The First Challenge - 1 Module Solved": 71301001,
    "1.1 The First Challenge - 2 Modules Solved": 71301002,
    "1.1 The First Challenge - 3 Modules Solved": 71301003,
    "Section 1 Completed": 71301004
}

section2_table = {
    "2.1 Make it Double - 1 Module Solved": 71301005,
    "2.1 Make it Double - 2 Modules Solved": 71301006,
    "2.1 Make it Double - 3 Modules Solved": 71301007,
    "2.1 Make it Double - 4 Modules Solved": 71301008,
    "2.1 Make it Double - 5 Modules Solved": 71301009,
    "2.1 Make it Double - 6 Modules Solved": 71301010,
    "2.2 Oh! The Lights! - 1 Module Solved": 71301011,
    "2.2 Oh! The Lights! - 2 Modules Solved": 71301012,
    "2.2 Oh! The Lights! - 3 Modules Solved": 71301013,
    "2.3 Remember - 1 Module Solved": 71301014,
    "2.3 Remember - 2 Modules Solved": 71301015,
    "2.3 Remember - 3 Modules Solved": 71301016,
    "2.4 Don't Get Lost - 1 Module Solved": 71301017,
    "2.4 Don't Get Lost - 2 Modules Solved": 71301018,
    "2.4 Don't Get Lost - 3 Modules Solved": 71301019,
    "2.5 Confusion - 1 Module Solved": 71301020,
    "2.5 Confusion - 2 Modules Solved": 71301021,
    "2.5 Confusion - 3 Modules Solved": 71301022,
    "2.6 Speedster I - 1 Module Solved": 71301023,
    "2.6 Speedster I - 2 Modules Solved": 71301024,
    "2.6 Speedster I - 3 Modules Solved": 71301025,
    "Section 2 Completed": 71301026
}

section3_table = {
    "3.1 Back in the 40s - 1 Module Solved": 71301027,
    "3.1 Back in the 40s - 2 Modules Solved": 71301028,
    "3.1 Back in the 40s - 3 Modules Solved": 71301029,
    "3.2 Code Breaker - 1 Module Solved": 71301030,
    "3.2 Code Breaker - 2 Modules Solved": 71301031,
    "3.2 Code Breaker - 3 Modules Solved": 71301032,
    "3.3 Verticality - 1 Module Solved": 71301033,
    "3.3 Verticality - 2 Modules Solved": 71301034,
    "3.3 Verticality - 3 Modules Solved": 71301035,
    "3.4 Learning the Alphabet - 1 Module Solved": 71301036,
    "3.4 Learning the Alphabet - 2 Modules Solved": 71301037,
    "3.4 Learning the Alphabet - 3 Modules Solved": 71301038,
    "3.5 Precision Time - 1 Module Solved": 71301039,
    "3.5 Precision Time - 2 Modules Solved": 71301040,
    "3.5 Precision Time - 3 Modules Solved": 71301041,
    "3.5 Precision Time - 4 Modules Solved": 71301042,
    "3.6 Longer Bomb - 1 Module Solved": 71301043,
    "3.6 Longer Bomb - 2 Modules Solved": 71301044,
    "3.6 Longer Bomb - 3 Modules Solved": 71301045,
    "3.6 Longer Bomb - 4 Modules Solved": 71301046,
    "3.6 Longer Bomb - 5 Modules Solved": 71301047,
    "3.6 Longer Bomb - 6 Modules Solved": 71301048,
    "3.6 Longer Bomb - 7 Modules Solved": 71301049,
    "3.6 Longer Bomb - 8 Modules Solved": 71301050,
    "3.6 Longer Bomb - 9 Modules Solved": 71301051,
    "3.7 Rat Nest - 1 Module Solved": 71301052,
    "3.7 Rat Nest - 2 Modules Solved": 71301053,
    "3.7 Rat Nest - 3 Modules Solved": 71301054,
    "3.7 Rat Nest - 4 Modules Solved": 71301055,
    "3.7 Rat Nest - 5 Modules Solved": 71301056,
    "3.7 Rat Nest - 6 Modules Solved": 71301057,
    "3.8 Speedster II - 1 Module Solved": 71301058,
    "3.8 Speedster II - 2 Modules Solved": 71301059,
    "3.8 Speedster II - 3 Modules Solved": 71301060,
    "3.8 Speedster II - 4 Modules Solved": 71301061,
    "3.8 Speedster II - 5 Modules Solved": 71301062,
    "Section 3 Completed": 71301063
}

section4_table = {
    "4.1 Hold it! - 1 Module Solved": 71301064,
    "4.1 Hold it! - 2 Modules Solved": 71301065,
    "4.1 Hold it! - 3 Modules Solved": 71301066,
    "4.1 Hold it! - 4 Modules Solved": 71301067,
    "4.2 Master Hacker - 1 Module Solved": 71301068,
    "4.2 Master Hacker - 2 Modules Solved": 71301069,
    "4.2 Master Hacker - 3 Modules Solved": 71301070,
    "4.2 Master Hacker - 4 Modules Solved": 71301071,
    "4.3 Wheel of Misfortune - 1 Module Solved": 71301072,
    "4.3 Wheel of Misfortune - 2 Modules Solved": 71301073,
    "4.3 Wheel of Misfortune - 3 Modules Solved": 71301074,
    "4.3 Wheel of Misfortune - 4 Modules Solved": 71301075,
    "4.4 Speedster III - 1 Module Solved": 71301076,
    "4.4 Speedster III - 2 Modules Solved": 71301077,
    "4.4 Speedster III - 3 Modules Solved": 71301078,
    "4.4 Speedster III - 4 Modules Solved": 71301079,
    "Section 4 Completed": 71301080
}

section5_table = {
    "5.1 Miscommunication - 1 Module Solved": 71301081,
    "5.1 Miscommunication - 2 Modules Solved": 71301082,
    "5.1 Miscommunication - 3 Modules Solved": 71301083,
    "5.1 Miscommunication - 4 Modules Solved": 71301084,
    "5.2 Invisible Walls - 1 Module Solved": 71301085,
    "5.2 Invisible Walls - 2 Modules Solved": 71301086,
    "5.2 Invisible Walls - 3 Modules Solved": 71301087,
    "5.2 Invisible Walls - 4 Modules Solved": 71301088,
    "5.2 Invisible Walls - 5 Modules Solved": 71301089,
    "5.2 Invisible Walls - 6 Modules Solved": 71301090,
    "5.2 Invisible Walls - 7 Modules Solved": 71301091,
    "5.3 Cipher Decrypter - 1 Module Solved": 71301092,
    "5.3 Cipher Decrypter - 2 Modules Solved": 71301093,
    "5.3 Cipher Decrypter - 3 Modules Solved": 71301094,
    "5.3 Cipher Decrypter - 4 Modules Solved": 71301095,
    "5.3 Cipher Decrypter - 5 Modules Solved": 71301096,
    "5.3 Cipher Decrypter - 6 Modules Solved": 71301097,
    "5.3 Cipher Decrypter - 7 Modules Solved": 71301098,
    "5.3 Cipher Decrypter - 8 Modules Solved": 71301099,
    "5.3 Cipher Decrypter - 9 Modules Solved": 71301100,
    "5.4 Stroboscopic - 1 Module Solved": 71301101,
    "5.4 Stroboscopic - 2 Modules Solved": 71301102,
    "5.4 Stroboscopic - 3 Modules Solved": 71301103,
    "5.4 Stroboscopic - 4 Modules Solved": 71301104,
    "5.4 Stroboscopic - 5 Modules Solved": 71301105,
    "5.4 Stroboscopic - 6 Modules Solved": 71301106,
    "5.5 Attention Needed - 1 Module Solved": 71301107,
    "5.5 Attention Needed - 2 Modules Solved": 71301108,
    "5.5 Attention Needed - 3 Modules Solved": 71301109,
    "5.5 Attention Needed - 4 Modules Solved": 71301110,
    "5.5 Attention Needed - 5 Modules Solved": 71301111,
    "5.6 Speedster IV - 1 Module Solved": 71301112,
    "5.6 Speedster IV - 2 Modules Solved": 71301113,
    "5.6 Speedster IV - 3 Modules Solved": 71301114,
    "5.6 Speedster IV - 4 Modules Solved": 71301115,
    "Section 5 Completed": 71301116
}

location_table = {
    **section1_table, **section2_table, **section3_table, **section4_table, **section5_table
}
