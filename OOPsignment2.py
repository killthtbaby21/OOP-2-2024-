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
    
    # Types of fields and their effects:
    
    def toxic_wasteland(self, combatant1, combatant2):
        """ damages both combatants for 5 health each, ignoring any defence"""
        damage = 5
        combatant1.health -= damage
        combatant2.health -= damage

    def healing_meadows(self, combatant1, combatant2):
        """heals both combatants for 5 health each (this can go over their max health"""
        heal_amount = 5
        combatant1.health += heal_amount
        combatant2.health += heal_amount

    def castle_walls(self, combatant1, combatant2):
        """No effect, representing Castle Walls."""
        pass

    def apply_effect(self, combatant1, combatant2):
        """Applies the current field's effect on both combatants based on field type."""
        if self.field_type == "Toxic Wasteland":
            self.toxic_wasteland(combatant1, combatant2)
        elif self.field_type == "Healing Meadows":
            self.healing_meadows(combatant1, combatant2)
        elif self.field_type == "Castle Walls":
            self.castle_walls(combatant1, combatant2)