import random
import BuffNDebuff
import LogNColor

def calculateStats(character):
     totalStg=character.stg+BuffNDebuff.getStrBuffNDebuff(character)
     totalAgi=character.agi+BuffNDebuff.getAgiBuffNDebuff(character)
     totalInl=character.inl+BuffNDebuff.getIntBuffNDebuff(character)
     character.hp= totalStg*10
     character.dmg= totalStg*5
     character.arm= totalAgi*3
     character.crit= totalAgi*0.1     
     character.spell= totalInl*5

def calculateStatsWithoutHp(character):
     
     totalStg=character.stg+BuffNDebuff.getStrBuffNDebuff(character)
     totalAgi=character.agi+BuffNDebuff.getAgiBuffNDebuff(character)
     totalInl=character.inl+BuffNDebuff.getIntBuffNDebuff(character)
     character.dmg= totalStg*5
     character.arm= totalAgi*3
     character.crit= totalAgi*0.1     
     character.spell= totalInl*5

def calculateHpWBuffs(character):
     totalStg=character.stg+BuffNDebuff.getStrBuffNDebuff(character)
     return totalStg*10     

def calculateHp(character):
     character.hp= character.stg*10     

def levelUp(character,floor):
     points = random.randint(1,floor)
     LogNColor.Printer("You got "+str(points)+" Floor Points!")
     while points>0:
          try:
               LogNColor.Printer("Where you wanna spend them?")
               c = raw_input()
               amount = int(filter(str.isdigit, c))
               if amount<=points:
                    if "strength" in c:
                         character.stg+=amount
                         points-=amount
                         LogNColor.Printer("You got "+str(amount)+" Strength")
                    elif "agility" in c:
                         character.agi+=amount
                         points-=amount
                         LogNColor.Printer("You got "+str(amount)+" Agility")
                    elif "intellect" in c:
                         character.inl+=amount
                         points-=amount
                         LogNColor.Printer("You got "+str(amount)+" Intellect")
                    else:
                          LogNColor.Printer("Wrong command")
               elif ("strength" not in c) and ("agility" not in c) and ("intellect" not in c):
                    LogNColor.Printer("Wrong command")
               else:
                    LogNColor.Printer("You don't got that many points")
          except:
                LogNColor.Printer("Wrong command")
               

def enemyLevelUp(enemy,floor):
     while floor>0:
          newStg=enemy.stg*(1+0.1*floor)
          newAgi=enemy.agi*(1+0.1*floor)
          newInl=enemy.inl*(1+0.1*floor)
          enemy.stg=int(round(newStg))
          enemy.agi=int(round(newAgi))
          enemy.inl=int(round(newInl))
          floor-=1
     

def roll(x):
    return random.randint(1,x)

def range_dict(*args):
    return_val = {}
    for k,v in args:
        for i in k:
            return_val[i] = v
    return return_val
