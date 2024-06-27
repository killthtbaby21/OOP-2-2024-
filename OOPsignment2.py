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

"""
Combatant

"""

class Combatant(Arena):
    def __init__(self,name, maxHealth,strength,defense,ranged,magic):
        self.name =name
        if not isinstance(maxHealth,strength,defense,ranged,magic (int, float)):
            raise TypeError
        self.__maxHealth = maxHealth
        self.__health = maxHealth
        self.__strength = strength
        self.__defense =defense
        self.__ranged = ranged
        self.__magic = magic
    #战斗统计数据
    def calculatePower(self):
        return self.__strength + self.__ranged + self.__magic -self.__defense
        
    #攻击敌人
    def attackEnemy(self, enemy):
        enemy = combatant




        if self.__health <= 0:
            print(f"{self.name} is dead and cannot attack.")
            return
    #受伤
    def takeDamage(self, damage):
        damage = calculatePower()
        self.__health -= damage


        if self.__health <= 0:
            print(f"{self.name} is dead and cannot take damage.")
            return
    #重生
    def resetValues(self):
        self.__health = self.__maxHealth
        return self.__health

    #战斗数据细节
    def getMAxHealth(self):

        return self.__maxHealth
    
    def getHealth(self):
        return self.__health
    def setHealth(self, health):
        if health < 0:
            raise ValueError("Health cannot be negative.")
        self.__health = health
    def getStrength(self):
        
        return self.__strength
    def getDefense(self):
        
        return self.__defense
    def getRanged(self): 
        
        return self.__ranged
    def getMagic(self): 
        return self.__magic
    
    #数据播报
    def details(self):
        print(f"Noticed：{self.name} ：Health：{self.health} \nStrength： {self.strength}\nDefense:{self.defense}\nRanged:{self.ranged}\n Magic:{self.magic} ")
        print()


"""
Mage
"""

class Mage(Combatant):
    def __init__(self, name, maxHealth, strength, defense, ranged,mana,regenRate):
        super().__init__(name, maxHealth, strength, defense, ranged)
        self.__max_health = maxHealth
        self.__health = maxHealth
        self.__strength = strength
        self.__defense = defense
        self.__ranged = ranged
        self.__magic = mana
        if not isinstance(mana,regenRate(int, float)):
            raise TypeError
        self.mana =mana
        self.regenRate = mana/4

    def calculatePower(self):
        pass
    def resetValues(self):
        self.mana = self.__class__.base_mana
        self.regenRate = self.mana / 4
        return super().resetValues()
#火焰法师   
class PyroMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, ranged, mana, regenRate,flameBoost):
        super().__init__(name, maxHealth, strength, defense, ranged, mana, regenRate)
        self.__flameBoost = flameBoost
        self.__magic = mana 

    def castSpell(self):
        pass
    def castFireBlast(self):
        pass
    def castSuperHeat(self):
        pass

#霜冻法师
class FrostMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic, mana, regenRate,iceBlock):
        super().__init__(name, maxHealth,strength, defense, ranged, mana, regenRate)
        self.__iceBlock = iceBlock
        self.__magic = mana 
    def takeDamage(self):
        pass
    def castSpell(self):
        pass
    def iceBarrage(self):
        pass
    def iceBolck(self):
        pass