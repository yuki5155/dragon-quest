from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from spells.dynes import dyne

class Monster(BaseModel):
    name: str
    english_name: Optional[str] = None
    drop_item: str
    weaks: Optional[List[str]] = None
    spells: Optional[List[str]] = None

Illusion_Shadow = Monster(name="あやしいかげ", english_name="Illusion Shadow", drop_item="random")
King_Frog = Monster(name="だいおうガマ", english_name="King Frog", drop_item="とげのむち", weaks=[dyne.name])