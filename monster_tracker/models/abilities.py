from sqlalchemy import Column, Integer, Text

from monster_tracker.models import Base


class SpecialAbilities(Base):
    __tablename__ = 'special_abilities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    desc = Column(Text)
    attack_bonus = Column(Integer)
    damage_dice = Column(Text)