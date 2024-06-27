"""
Field
"""
import random

class Field:
    def __init__(self, name):
        self.__name = name
        self.field_type = None
        self.types = {
            "Toxic Wasteland": self.toxic_wasteland,
            "Healing Meadows": self.healing_meadows,
            "Castle Walls": self.castle_walls
        }
        self.changeField()
    def fieldEffect(self, combatant1, combatant2):
        self.types[self.field_type](combatant1, combatant2)
 
    def changeField(self):
        self.field_type = random.choice(list(self.types.keys()))
    def getName(self):
        return self.__name
    
