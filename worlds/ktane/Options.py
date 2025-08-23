from dataclasses import dataclass
from Options import Option, Range, DefaultOnToggle, Toggle, Choice, PerGameCommonOptions, DeathLink
from BaseClasses import MultiWorld
from typing import Dict, Union, List


class UseRandomRuleSeed(DefaultOnToggle):
    """Use random puzzle solutions for the modules."""
    display_name = "Use Random Rule Seed"


class RuleSeed(Range):
    """If "Use Random Rule Seed" is set to false, define the custom rule seed used to solve the modules.
    Set to 1 to use vanilla rules."""
    display_name = "Rule Seed Number"
    range_start = 1
    range_end = 10000
    default = 1


class HardlockModules(Toggle):
    """Bombs that can't be finished will not be accessible. Only when all the modules that can be on a bomb are unlocked
     that the bomb is unlocked. Strongly recommended if "Use Random Rule Seed" is disabled."""
    display_name = "Hardlock Modules"

class OHKOMode(Toggle):
    """One mistake and it's over. Only activate if you are hardcore."""
    display_name = "OHKO Mode"


#class ManualsLanguage(Choice):
#    """Language code that the manuals pages should be. Should be the same language of the game. Available options are:
#    en, cs, es, fr, ja, nl, pl, ru"""
#    display_name = "Manuals Language"
#    option_en = 0
#    option_cs = 1
#    option_es = 2
#    option_fr = 3
#    option_ja = 4
#    option_nl = 5
#    option_pl = 6
#    option_ru = 7

class DeathLinkBehaviour(Choice):
    """Manages how Death Links are sent and received."""
    display_name = "Death Link Behaviour"
    option_explosion = 0
    option_strike = 1


@dataclass
class KTANEOptions(PerGameCommonOptions):
    random_rule_seed: UseRandomRuleSeed
    rule_seed: RuleSeed
    hardlock_modules: HardlockModules
    ohko_mode: OHKOMode
    #manuals_language: ManualsLanguage
    death_link: DeathLink
    death_link_behaviour: DeathLinkBehaviour


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
