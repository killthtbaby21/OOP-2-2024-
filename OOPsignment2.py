"""
Field
"""
import random

class Field:
    def __init__(self, name):
        self.__name = name
        self.field_type = None
        self.types = {"Toxic Wasteland","Healing Meadows","Castle Walls"}
        self.changeField()
    def fieldEffect(self, combatant1, combatant2):
        if self.field_type == "Toxic Wasteland":
            damage = 5
            combatant1.health -= damage
            combatant2.health -= damage
        if self.field_type == "Healing Meadows":
            heal_amount = 5
            combatant1.health += heal_amount
            combatant2.health += heal_amount
        if self.field_type == "Castle_walls":
            pass

 
    def changeField(self):
        self.field_type = random.choice(list(self.types()))
    def getName(self):
        return self.field_type
    

"""
Arena

"""
class Arena(Field):
    def __init__(self,combatants,field):
        self.field = Field(self.field_type)
        self.combatants =[]
        
    # 加入战士  
    def add_combatant(self, combatant):
        if combatant not in self.combatants:  # 如果列表中没有这个战士
            self.combatants.append(combatant)
        else:
            raise ValueError("Alreally exists.")    
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
        Combatant.resetValues()
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
                    continue
            self.restoreCombatants()
            print(f"Noticed：{self.name} ：Health：{self.health} \nStrength： {self.strength}\nDefense:{self.defense}\nRanged:{self.ranged}\n Magic:{self.magic} ")
        else:
            print("Invalid duel: Ensure both combatants are in the arena and have health.")

"""
Combatant

"""

class Combatant:
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
        return f"{self.name}, Class: {self.__class__.__name__}, Stats: Health={self.health}, Strength={self.strength}, Defence={self.defence}"


"""
Mage
"""

class Mage(Combatant):
    def __init__(self, name, maxHealth, strength, defense, ranged,magic,regenRate):
        super().__init__(name, maxHealth, strength, defense, ranged)
        self.__max_health = maxHealth
        self.__health = maxHealth
        self.__strength = strength
        self.__defense = defense
        self.__ranged = ranged
        self.__magic = magic
        if not isinstance(mana,regenRate(int, float)):
            raise TypeError
        self._mana = self.__magic
        self._regenRate = self._mana/4
        
    def castSpell(self):
        pass

    def calculatePower(self):
        
        return damage
    def resetValues(self):
        self._mana = self.__magic
        self.regenRate = self._mana / 4
        return super().resetValues() 
#火焰法师   
class PyroMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic, regenRate,flameBoost):
        super().__init__(name, maxHealth, strength, defense, ranged, magic, regenRate)
        self.__flameBoost = flameBoost
        self.__mana = self.__magic
        self.__flameBoost = 0
        self.__bonus_damage = 0 
    def castSpell(self):
        if 40 > self._mana > 10:
            PyroMage.castFireBlast()
        elif self._mana >= 40:
            PyroMage.castSuperHeat()
        self._mana += self.regenRate
    def castFireBlast(self):
            self._mana-=10
            self.__bonus_damage += 10 
            return self.__bonus_damage
    def castSuperHeat(self):
            self._mana-=40
            self.__flameBoost+=1
            return self.__flameBoost
    
    
        

#霜冻法师
class FrostMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic, regenRate,iceBlock):
        super().__init__(name, maxHealth,strength, defense, ranged, magic, regenRate)
        self.__iceBlock = iceBlock
        self.__mana = self.__magic 
        self.iceBlock = False
        self.__bonus_damage = 0
    def takeDamage(self,damage):
        if self.iceBlock:
            print(f"Ice Block absorbs the attack!")
            self.iceBlock = False
        else:
            super().takeDamage(damage)
    def castSpell(self):
        if 50 > self._mana >10:
            FrostMage.iceBarrage()
        elif self._mana >= 50:
            FrostMage.iceBolck()
        self._mana += self._regenRate
    def iceBarrage(self):
            self.__bonus_damage +=30
            return self.__bonus_damage
    def iceBolck(self):        
            self.iceBlock = True
            self._mana -= 50
            return self.iceBlock
"""
Ranger
"""
class Ranger(Combatant):
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
            if self.arrows > 0:
                self.arrows -= 1
                print(f"{self.name} fires an arrow!")
                return self.ranged
            else:
                print(f"{self.name} has no arrows left!")
                return self.strength


    def resetValues(self):
        self.__arrow = 3
        return super().resetValues()


        
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
        actual_damage = max(damage - self.__defense - self.armourValue, 0)
        self.__health -= actual_damage
        if damage >5:
            n = damage //5
            self.armourValue -= 1*n  
        if self.armourValue <= 0:
            print(f"{self.name}'s armour has shattered!")
            self.armourValue = 0
        
        
        return super().takeDamage(damage)
    
    def calculatePower(self):
        return self.__strength
    def resetValues(self):
        self.__armourValue = 10
        return super().resetValues()

#Dharok
class Dharok(Warroir):
    def __init__(self, name, maxHealth,strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic,armourValue)
        
    def calculatePower(self):
        bonus_damage =self.__maxHealth -self.__health
        return super().calculatePower() + bonus_damage
    

#Guthans
class Guthans(Warroir):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth,  strength, defense, ranged, magic,armourValue)
        
    def calculatePower(self):
        if self.__health<self.__maxHealth:
            self.__health += self.__strength // 5
        self.__health = min(self.__health , self.__maxHealth)
        return super().calculatePower()


        

#Karil
class Karil(Warroir):
    def __init__(self, name, maxHealth, strength, defense, ranged, magic,armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic,armourValue)
        
    def calculatePower(self):
        return super().calculatePower() + self.__ranged 