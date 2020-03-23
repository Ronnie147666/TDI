import random
import BuffNDebuff
import LogNColor


def calculateStats(character):
    totalStg = character.stg + BuffNDebuff.getStrBuffNDebuff(character)
    totalAgi = character.agi + BuffNDebuff.getAgiBuffNDebuff(character)
    totalInl = character.inl + BuffNDebuff.getIntBuffNDebuff(character)
    character.hp = totalStg * 10
    character.dmg = totalStg * 5
    character.arm = totalAgi * 3
    character.crit = round(totalAgi * 0.1, 1)
    character.spell = totalInl * 5
    character.res = totalInl * 2


def calculateStatsWithoutHp(character):
    totalStg = character.stg + BuffNDebuff.getStrBuffNDebuff(character)
    totalAgi = character.agi + BuffNDebuff.getAgiBuffNDebuff(character)
    totalInl = character.inl + BuffNDebuff.getIntBuffNDebuff(character)
    character.dmg = totalStg * 5
    character.arm = totalAgi * 3
    character.crit = round(totalAgi * 0.1, 1)
    character.spell = totalInl * 5
    character.res = totalInl * 2


def calculateHpWBuffs(character):
    totalStg = character.stg + BuffNDebuff.getStrBuffNDebuff(character)
    return totalStg * 10


def calculateHp(character):
    character.hp = character.stg * 10


def levelUp(character, floor):
    points = random.randint(1, floor)
    LogNColor.Printer("You got " + str(points) + " Floor Points!")
    while points > 0:
        try:
            LogNColor.Printer("Where you wanna spend them?")
            c = input()
            amount = int(list(filter(str.isdigit, c))[0])
            if amount <= points:
                if "strength" in c:
                    character.stg += amount
                    points -= amount
                    LogNColor.Printer("You got " + str(amount) + " Strength")
                elif "agility" in c:
                    character.agi += amount
                    points -= amount
                    LogNColor.Printer("You got " + str(amount) + " Agility")
                elif "intellect" in c:
                    character.inl += amount
                    points -= amount
                    LogNColor.Printer("You got " + str(amount) + " Intellect")
                else:
                    LogNColor.Printer("Wrong command")
            elif ("strength" not in c) and ("agility" not in c) and ("intellect" not in c):
                LogNColor.Printer("Wrong command")
            else:
                LogNColor.Printer("You don't got that many points")
        except:
            LogNColor.Printer("Wrong command")


def enemyLevelUp(enemy, floor):
    # while floor > 0:
        newStg = enemy.stg * (1 + 0.5 * floor)
        newAgi = enemy.agi * (1 + 0.5 * floor)
        newInl = enemy.inl * (1 + 0.5 * floor)
        newFireRes = enemy.fireRes * (1 + 0.5 * floor)
        newFrostRes = enemy.frostRes * (1 + 0.5 * floor)
        newShadowRes = enemy.shadowRes * (1 + 0.5 * floor)
        newNatureRes = enemy.natureRes * (1 + 0.5 * floor)
        enemy.stg = int(round(newStg))
        enemy.agi = int(round(newAgi))
        enemy.inl = int(round(newInl))
        enemy.fireRes = int(round(newFireRes))
        enemy.frostRes = int(round(newFrostRes))
        enemy.shadowRes = int(round(newShadowRes))
        enemy.natureRes = int(round(newNatureRes))


def itemLevelUp(item, floor):
    ##  while floor>0:
    newStg = item.stg * (1 + 0.05 * floor)
    newAgi = item.agi * (1 + 0.05 * floor)
    newInl = item.inl * (1 + 0.05 * floor)
    newFireRes = item.fireRes * (1 + 0.05 * floor)
    newFrostRes = item.frostRes * (1 + 0.05 * floor)
    newShadowRes = item.shadowRes * (1 + 0.05 * floor)
    newNatureRes = item.natureRes * (1 + 0.05 * floor)
    item.stg = int(round(newStg))
    item.agi = int(round(newAgi))
    item.inl = int(round(newInl))
    item.fireRes = int(round(newFireRes))
    item.frostRes = int(round(newFrostRes))
    item.shadowRes = int(round(newShadowRes))
    item.natureRes = int(round(newNatureRes))


def isCritical(crit):
    chance = random.randint(0, 100) + crit
    if chance >= 100:
        LogNColor.Printer(str("You got a critical"))
        return True
    return False


def roll(x1, x2):
    return random.randint(x1, x2)


def range_dict(*args):
    return_val = {}
    for k, v in args:
        for i in k:
            return_val[i] = v
    return return_val
