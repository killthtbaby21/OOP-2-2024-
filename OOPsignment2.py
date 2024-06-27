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


"""
Arena

"""
class Arena(Field):
    def __init__(self, name):
        self.name = name
        self.combatants = []
        self.field = Field(name)
        self.combatants = []
    # 加入战士  
    def add_combatant(self, combatant):
        self.combatants.append(combatant)
        # 加入战士，限制只能添加一个
    def add_combatant(self, combatant):
        if not self.combatants:  # 如果列表中没有这个战士
            self.combatants.append(combatant)
        else:
            raise ValueError("只能添加一个战士！")    
    # 移除战士    
    def removeCombatant(self, combatant):
        if combatant not in self.combatants:
            raise ValueError(f"Combatant {combatant} is not in the list to be removed.")
        self.combatants.remove(combatant)
     # 并确保仅能移除一个   
    # 战士出场
    def listCombatants(self):
        for combatant in self.combatants:
            print(combatant)
    # 恢复战士生命
    def restoreCombatants(self):
        for combatant in self.combatants:
            combatant.health = combatant.max_health
    #验证战士完整性
    def checkVaildCombatant(self, combatant):
        if combatant in self.combatants:
            if combatant.health >= 0:
                print(f"{combatant} have the strength to fight in a war..")
            return True
        else:
            raise ValueError(f"Combatant {combatant} can't fight any more.")
            
    # 决斗
    def duel(self, combatant1, combatant2):
        
        while combatant1.health > 0 and combatant2.health > 0:
            combatant1.attackEnemy(combatant2)
            combatant2.attackEnemy(combatant1)
            self.field.fieldEffect(combatant1, combatant2)
