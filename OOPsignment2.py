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
        
        if combatant1 in self.combatants and combatant2 in self.combatants and combatant1.health > 0 and combatant2.health > 0:
            print(f"Duel between {combatant1} and {combatant2} in Arena {self.name}:")
            for i in range(10):  # Maximum of 10 rounds
                self.field.fieldEffect([combatant1, combatant2])
                if combatant1.health <= 0:
                    winner = combatant2
                else:
                    winner = combatant1
                    print(f"{winner} is the winner")
                    break
            self.restoreCombatants()  # Restore health after duel
        else:
            print("Invalid duel: Ensure both combatants are in the arena and have health.")

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
        pass
        
    #攻击敌人
    def attackEnemy(self, enemy):
         if not isinstance(enemy, Combatant):
            print(f"Invalid enemy: {enemy}. It must be a Combatant instance.")
            return
         if self._health <= 0:
            print(f"{self.name} is dead and cannot attack.")
            return   
         print(f"{self.name} attacks {enemy.name}.") 
    def takeDamage(self, damage):
        self.damage = self.calculatePower()
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
        damage= self.mana
        return damage
    def resetValues(self):
        self.mana = self.__magic
        self.regenRate = self.mana / 4
        return super().resetValues() 
#火焰法师   
class PyroMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, ranged, mana, regenRate,flameBoost):
        super().__init__(name, maxHealth, strength, defense, ranged, mana, regenRate)
        self.__flameBoost = flameBoost
        self.__magic = mana
        self.__flameBoost = 0
        self.__bonus_damage = 0 

    def castSpell(self):
        pass
    def castFireBlast(self):
        if 40 > self.mana > 10:
            self.mana-=10
            self.__bonus_damage += 10 
            return self.__bonus_damage
    def castSuperHeat(self):
        if self.mana >= 40:
            self.mana-=40
            self.__flameBoost+=1
            return self.__flameBoost
    def calculatePower(self):
        damage =(self.strength*self.__flameBoost)+self.__bonus_damage
        return damage
    
        

#霜冻法师
class FrostMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic, mana, regenRate,iceBlock):
        super().__init__(name, maxHealth,strength, defense, ranged, mana, regenRate)
        self.__iceBlock = iceBlock
        self.__magic = mana 
        self.iceBlock = False
        self.__bonus_damage = 0
    def takeDamage(self):
        pass
    def castSpell(self):
        pass


    def iceBarrage(self):
        if 50 > self.mana >10:
            self.__bonus_damage +=30
            return self.__bonus_damage


    def iceBolck(self):
        if self.mana >= 50:
            self.iceBlock = True
            self.mana -= 50
            return self.iceBlock
"""
Ranger
"""
class Mage(Combatant):
    def __init__(self, name, maxHealth, health, strength, defense, ranged, magic,arrow):
        super().__init__(name, maxHealth, health, strength, defense, ranged, magic)
        self.__max_health = maxHealth
        self.__health = health
        self.__strength = strength
        self.__defense = defense
        self.ranged = ranged
        self.__magic = magic
        self.__arrow = 3

    def calculatePower(self):
        damage = self.ranged


    def resetValues(self):
        def fireArrow(self):
            if self.arrows > 0:
                self.arrows -= 1
                print(f"{self.name} fires an arrow!")
                return self.ranged
            else:
                self.__arrow = 3
                print(f"{self.name} has no arrows left!")
                return self.strength
"""
Warrior
"""
class Warroir(Combatant):
    def __init__(self, name, maxHealth,strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic)
        self.__max_health = maxHealth
        self.__health = maxHealth
        self.__strength = strength
        self.__defense = defense
        self.__ranged = ranged
        self.__magic = magic
        if not isinstance(armourValue(int, float)):
            raise TypeError
        self.__armourValue = armourValue

    def takeDamage(self, damage):
        damage = damage - self.__armourValue
        if damage >= 5:
            self.__armourValue -= 1
        
        return super().takeDamage(damage)
    
    def calculatePower(self):
        pass
    def resetValues(self):
        self.__armourValue = 10
        return super().resetValues()

#Dharok
class Dharok(Warroir):
    def __init__(self, name, maxHealth,strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic,armourValue)
        self.health = maxHealth
    def calculatePower(self):
        self.damage = self.__strength +(self.__maxHealth -self.__health)
        return
    

#Guthans
class Guthans(Warroir):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth,  strength, defense, ranged, magic,armourValue)
        self.__health = maxHealth
    def calculatePower(self):
        if self.__health<self.__maxHealth:
            self.__health += self.__strength/5
        self.__health = min(self.__health , self.__maxHealth)
        return 


        

#Karil
class Karil(Warroir):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic,armourValue)
        self.__health = maxHealth
    def calculatePower(self,damage):
        damage = self.__strength + self.__ranged
        return damage  