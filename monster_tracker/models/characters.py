from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from monster_tracker.models import Base, Status


class Character(Base):  # pylint: disable=too-many-instance-attributes
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    max_health = Column(Integer)
    temp_health = Column(Integer)
    current_health = Column(Integer)
    armor_class = Column(Integer)
    initiative_bonus = Column(Integer)
    initiative = Column(Integer)
    speed = Column(Integer)
    status = Column(Integer)
    type = Column(Text)
    encounter_id = Column(Integer, ForeignKey('encounter.id'))
    encounter = relationship('Encounter', back_populates='characters')

    __mapper_args__ = {'polymorphic_identity': 'character', 'polymorphic_on': type}

    def to_tuple(self):
        return (self.name, self.current_health, self.armor_class, self.initiative, self.speed)

    def alive(self):
        return self.current_health > 0

    def damage(self, dealt_damage):
        raise NotImplementedError('No death for generic character')

    def heal(self, healed_damage):
        self.current_health += healed_damage
        if self.current_health > self.max_health + self.temp_health:
            self.current_health = self.max_health + self.temp_health

    def adjust_max_health(self, health):
        self.max_health += health
        self.current_health += health

    def move(self, feet):
        if self.moved > 0:
            self.moved -= feet
        else:
            print('{} has already moved their full movement'.format(self.name))

    def act(self):
        pass

    def bonus(self):
        pass

    def turn(self):
        raise NotImplementedError('No turn for generic character')

    def death(self):
        raise NotImplementedError('No death for generic character')

    def __init__(
        self,
        name=None,
        max_health=None,
        ac=None,
        initiative_bonus=0,
        initiative=0,
        speed=None,
        temp_health=0,
        current_health=None
    ):
        self.name = name
        self.armor_class = ac
        self.initiative_bonus = initiative_bonus
        self.initiative = initiative
        self.speed = speed
        self.status = Status.ALIVE
        self.max_health = max_health
        self.temp_health = temp_health
        self.current_health = current_health or self.max_health
        self.moved = speed

    def __repr__(self):
        return '{}, Health: {} Initiative: {} AC: {} Speed: {}'.format(
            self.name, self.current_health, self.initiative, self.ac, self.speed
        )