"""
Field
"""
import random

class Field:
    def __init__(self, name):
        self.__name = name
        self.field = None
        self.types = ["Toxic Wasteland","Healing Meadows","Castle Walls"]
        self.changeField()
    def fieldEffect(self, combatant1, combatant2):
        if self.field == "Toxic Wasteland":
            damage = 5
            combatant1.__health = combatant1.getHealth()
            combatant2.__health = combatant2.getHealth()
            combatant1.__health -= damage
            combatant2.__health -= damage
        if self.field == "Healing Meadows":
            heal_amount = 5
            combatant1.__health = combatant1.getHealth()
            combatant2.__health = combatant2.getHealth()
            combatant1.__health += heal_amount
            combatant2.__health += heal_amount
        if self.field == "Castle_walls":
            pass

 
    def changeField(self):
        self.field = random.choice(self.types)
    def getName(self):
        return self.field
    

"""
Arena

"""
class Arena:
    def __init__(self,name):
        self.name = name
        f = Field("fff")
        f.changeField()
        self.field = f
        self.combatants =[]
        
    # 加入战士  
    def addCombatant(self, combatant):
        if combatant not in self.combatants:  # 如果列表中没有这个战士
            self.combatants.append(combatant)
        else:
            raise ValueError("Alreally exists.")    
    # 移除战士    
    def removeCombatant(self, combatant):
        if combatant not in self.combatants:
            print(f"Combatant {combatant} is not in the list to be removed.")
        self.combatants.remove(combatant)
     # 并确保仅能移除一个   
    # 战士出场
    def listCombatants(self):
        for combatant in self.combatants:
            print(combatant)
    # 恢复战士生命
    def restoreCombatants(self):
        for combatant in self.combatants:
            combatant.resetValues()
    #验证战士完整性
    def checkVaildCombatant(self, combatant):
        if combatant in self.combatants:
            if combatant.health >= 0:
                print(f"{combatant} have the strength to fight in a war..")
                return True
            else:
                print(f"Combatant {combatant} can't fight any more.")
                return False
            
    # 决斗
    def duel(self, combatant1, combatant2):
        
        if combatant1 in self.combatants: 
            if combatant2 in self.combatants:
                if combatant1.getHealth() > 0 and combatant2.getHealth() > 0:
                    print(f"Duel between {combatant1.name} and {combatant2.name} in Arena {self.name}:")
                    print(f"{combatant1.name} is a {type(combatant1).__name__} and has the following stats:\nHealth:{combatant1.getHealth()} \nStrength:{combatant1.getStrength()}\nDefense:{combatant1.getDefense()}\nRanged:{combatant1.getRanged()}\nMagic:{combatant1.getMagic()} ")
                    print(f"{combatant2.name} is a {type(combatant2).__name__} and has the following stats:\nHealth:{combatant2.getHealth()} \nStrength:{combatant2.getStrength()}\nDefense:{combatant2.getDefense()}\nRanged:{combatant2.getRanged()}\nMagic:{combatant2.getMagic()} ")
                    self.field.fieldEffect(combatant1, combatant2)
                    round_number = 1
                    while combatant1.getHealth() > 0 and combatant2.getHealth() > 0 and round_number <= 10: 
                        print(f"Round { round_number}")
                        combatant1.attackEnemy(combatant2)
                        combatant2.attackEnemy(combatant1)
                        round_number += 1 
                        if combatant1.getHealth() <= 0:
                                winner = combatant2.name
                        elif combatant2.getHealth() <= 0:
                                winner = combatant1.name
                        else:
                            winner = combatant1.name if combatant1.getHealth() >= combatant2.getHealth() else combatant2.name
                
                    combatant1_health = combatant1.getHealth()
                    combatant2_health = combatant2.getHealth()    
                    print(f"{winner} is the winner")
                    print("---------- END BATTLE ----------")
                    
            else: print(f"{combatant2.name} was not found in Falador's list of fighters")
        else:print(f"{combatant1.name} was not found in Falador's list of fighters")

"""
Combatant

"""
from abc import ABC

class Combatant(ABC):
    def __init__(self,name, maxHealth,strength,defense,magic,ranged):
        self.name =name
        self.__maxHealth = maxHealth
        self.__health = maxHealth
        self.__strength = strength
        self.__defense =defense
        self.__magic = magic
        self.__ranged = ranged
        
    #战斗统计数据
    def calculatePower(self):
        pass
        
    #攻击敌人
    def attackEnemy(self, enemy):
        if self.__health <= 0:
            print(f"{self.name} is dead and cannot attack.")
            return   
        print(f"{self.name} attacks for {self.calculatePower()}.") 
        enemy.takeDamage(self.calculatePower())
        print(f"{enemy.name}'s defence level blocked {enemy.takeDamage(self.calculatePower())} damage")
    def takeDamage(self, damage):
        self.damage = self.calculatePower()
        self.__health -= self.damage
        
        
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
            print("Health cannot be negative.")
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
        return f"{self.name}, Class: {self.__class__.__name__}, Stats: Health={self.__health}, Strength={self.__strength}, Defence={self.__defense}"


"""
Mage
"""

class Mage(Combatant,ABC):
    def __init__(self, name, maxHealth, strength, defense, magic,ranged):
        super().__init__(name, maxHealth, strength, defense, magic,ranged)
        self.__health = maxHealth
        self._mana = magic
        self._regenRate = self._mana//4       
    def castSpell(self):
        pass
    def calculatePower(self):
        self.castSpell()
    def resetValues(self):
        self._mana = self.__magic
        self.regenRate = self._mana / 4
        return super().resetValues() 
#火焰法师   
class PyroMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, magic, ranged ):
        super().__init__(name, maxHealth, strength, defense, magic, ranged )
        self.__health = maxHealth
        self._mana = magic
        self.__flameBoost = 0
        self.__bonus_damage = 0 
    def castSpell(self):
        if 40 > self._mana > 10:
            PyroMage.castFireBlast()
        elif self._mana >= 40:
            PyroMage.castSuperHeat()
        self._mana += self.regenRate
        damage =(self.strength * self.flameBoost) + self.__bonus_damage
        return damage
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
    def __init__(self, name, maxHealth, strength, defense, magic,ranged):
        super().__init__(name, maxHealth,strength, defense, magic,ranged)
        self.__health = maxHealth
        self.__mana = magic 
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
        damage = (self._mana//4)+self.__bonus_damage
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
    def __init__(self, name, maxHealth, strength, defense, magic,ranged):
        super().__init__(name, maxHealth,strength, defense, magic,ranged )
        self.__strength = strength
        self.__ranged = ranged
        self.__arrow = 3
        self.__attacked_this_round = False
    def calculatePower(self):
        if self.__arrow > 0:
            self.__arrow -= 1
            return self.__ranged
            
        else:
            print(f"{self.name} has no arrows left!")
            return self.__strength
      
    def resetValues(self):
        self.__arrow = 3
        return super().resetValues()
        
"""
Warrior
"""
class Warrior(Combatant):
    def __init__(self, name, maxHealth,strength, defense,  magic,ranged,armourValue):
        super().__init__(name, maxHealth, strength, defense,  magic,ranged)
        self.__defense = defense
        self.__strength = strength
        self.__health = maxHealth
        self.__armourValue = armourValue

    def takeDamage(self, damage):
        if self.__armourValue <= 0:
            print(f"Armour shattered!")
            return super().takeDamage(damage)
        else:
            print(f"{self.name} 's armour blocked 5 damage.")
            actual_damage = max(damage - self.__defense - 5, 0)
        
            self.__health -= actual_damage
            if damage >5:
                n = damage //5
                self.__armourValue =min(self.__armourValue- 1*n ,self.__armourValue) 
        
            
        
        
        return super().takeDamage(damage)
    
    def calculatePower(self):
        return self.__strength
    def resetValues(self):
        self.__armourValue = 10
        return super().resetValues()

#Dharok
class Dharok(Warrior):
    def __init__(self, name, maxHealth,strength, defense,magic, ranged, armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic,armourValue)
        self.__health = maxHealth
        
    def calculatePower(self):
        bonus_damage =self.__maxHealth -self.__health
        return super().calculatePower() + bonus_damage
    

#Guthans
class Guthans(Warrior):
    def __init__(self, name, maxHealth, strength, defense, magic,ranged, armourValue):
        super().__init__(name, maxHealth,  strength, defense, ranged, magic,armourValue)
        self.__health = maxHealth
        
    def calculatePower(self):
        if self.__health<self.__maxHealth:
            self.__health += self.__strength // 5
        self.__health = min(self.__health , self.__maxHealth)
        return super().calculatePower()


#Karil
class Karil(Warrior):
    def __init__(self, name, maxHealth, strength, defense, magic,ranged, armourValue):
        super().__init__(name, maxHealth, strength, defense, ranged, magic,armourValue)
        self.__ranged = ranged
        self.__health = maxHealth
        
    def calculatePower(self):
        return super().calculatePower() + self.__ranged 












# Creating the different combatant objects
# name, maxHealth, strength, defence, mage, range and armourValue for warriors
tim = Ranger("Tim", 99, 10, 10, 1, 50)
jay = Warrior("Jay", 99, 1, 99, 1, 1, 1)
kevin = Dharok("Kevin", 99, 45, 25, 25, 25, 10)
zac = Guthans("Zac", 99, 45, 30, 1, 1, 10)
jeff = Karil("Jeff", 99, 50, 40, 1, 10, 5)
try:
    durial = Mage("Durial", 99, 99, 99, 99, 99)
except TypeError:
    print("Mages must be specialized!")
jaina = FrostMage("Jaina", 99, 10, 20, 94, 10)
zezima = PyroMage("Zezima", 99, 15, 20, 70, 1)
# setting up the first arena
falador = Arena("Falador")
falador.addCombatant(tim)
falador.addCombatant(jeff)
falador.listCombatants()
# duel between ranger and karil
falador.duel(tim, jeff)
# showcasing incorrect duels
falador.duel(tim, jeff)
falador.duel(jeff, zezima)
# showcasing restoring combatants
falador.listCombatants()
falador.restoreCombatants()
falador.listCombatants()
# showcasing removing from arena
falador.removeCombatant(jeff)
falador.removeCombatant(jeff)
# setting up the second arena
varrock = Arena("Varrock")
varrock.addCombatant(kevin)
varrock.addCombatant(zac)
# duel between guthans and dharok.. note guthans does not heal on the final round as Zac was KO'd
varrock.duel(kevin, zac)
# setting up the third arena
wilderness = Arena("Wilderness")
wilderness.addCombatant(jaina)
wilderness.addCombatant(zezima)
# duel between a pyro and frost mage... double ko?!?!?
wilderness.duel(jaina, zezima)
# setting up final arena
lumbridge = Arena("Lumbridge")
lumbridge.addCombatant(jaina)
lumbridge.addCombatant(jay)
lumbridge.addCombatant(tim)
# showcasing health carries over from arenas
lumbridge.duel(jaina, jay)
# showcasing a duel that takes too long...
# tims arrows should also be reset to 3 from the restoing at the falador arena above
lumbridge.duel(jay, tim)
