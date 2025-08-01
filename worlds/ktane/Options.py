from dataclasses import dataclass
from Options import Option, Range, DefaultOnToggle, Toggle, Choice, PerGameCommonOptions
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
     that the bomb is unlocked. Would strongly recommend if "Use Random Rule Seed" is disabled."""
    display_name = "Hardlock Modules"


class ManualsLanguage(Choice):
    """Language code that the manuals pages should be. Should be the same language of the game. Available options are:
    en, cs, es, fr, ja, nl, pl, ru"""
    display_name = "Manuals Language"
    option_en = 0
    option_cs = 1
    option_es = 2
    option_fr = 3
    option_ja = 4
    option_nl = 5
    option_pl = 6
    option_ru = 7


@dataclass
class KTANEOptions(PerGameCommonOptions):
    random_rule_seed: UseRandomRuleSeed
    rule_seed: RuleSeed
    hardlock_modules: HardlockModules
    manuals_language: ManualsLanguage


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
