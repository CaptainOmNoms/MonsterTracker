from marshmallow_sqlalchemy import ModelSchema
from .character import Character
from .monster import Monster
from .hero import Hero
from .models import Encounter


class EncounterSchema(ModelSchema):
    class Meta:
        model = Encounter


class EncounterOld(object):
    def __init__(self):
        self.creatures = {}

    def add_player(self, name, health, ac, initiative, speed, played_by):
        player = Hero(name, health, ac, initiative, speed, played_by)
        self.creatures[name] = player

    def add_monster(self, name, health, ac, initiative, speed, xp):
        monster = Monster(name, health, ac, initiative, speed, xp)
        self.creatures[name] = monster

    def add_npc(self, name, health, ac, initiative, speed):
        npc = Hero(name, health, ac, initiative, speed, '')
        self.creatures[name] = npc
