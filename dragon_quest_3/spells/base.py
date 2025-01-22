from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

from enum import Enum

class SpellType(str, Enum):
    # Attack spells
    BLAZEMORE = "メラ系"  # Blaze, Blazemore, Blazemost
    FIREBAL = "ギラ系"   # Firebal, Firebane, Firevolt
    ICEBOLT = "ヒャド系"  # Icebolt, Snowblast, Blizzard
    BANG = "バギ系"      # Bang, Boom, Explodet
    DEFEAT = "ザキ系"    # Defeat, Beat
    DYNE = "デイン系"     # Dyne, MegaDyne
    
    # Healing spells
    HEAL = "ホイミ系"     # Heal, Healmore, Healall
    HEALUS = "ベホマラー系"  # Healus
    VIVIFY = "ザオリク系"   # Vivify
    
    # Support spells
    UPPER = "スカラ系"     # Upper, Increase
    BOUNCE = "マホカンタ系"  # Bounce
    STOPSPELL = "マホトーン系"  # Stopspell
    
    # Status effect spells
    SLEEP = "ラリホー系"    # Sleep, Sleepmore
    SURROUND = "マヌーサ系"  # Surround
    ROBMAGIC = "マホトラ系"  # RobMagic
    
    # Special spells
    RETURN = "リレミト"     # Return
    OUTSIDE = "トヘロス"    # Outside
    REPEL = "リレミト"      # Repel

class Spell(BaseModel):
    name: str
    damage: int
    english_name: Optional[str] = None
    mp_cost: int
    effect: str
    type: SpellType

if __name__ == "__main__":
    spell = Spell(name="メラ", mp_cost=2, effect="deals fire damage", type=SpellType.BLAZEMORE)
    print(spell)
    """
    name='メラ', english_name=None, mp_cost=2, effect='deals fire damage', type=<SpellType.BLAZEMORE: 'メラ系'>
    """

