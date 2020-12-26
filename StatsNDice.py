import random
import BuffNDebuff
import LogNColor


def calculateStats(character):
    totalStg = character.stg + BuffNDebuff.getStrBuffNDebuff(character)
    totalAgi = character.agi + BuffNDebuff.getAgiBuffNDebuff(character)
    totalInl = character.inl + BuffNDebuff.getIntBuffNDebuff(character)
    character.hp = totalStg * 10
    character.dmg = totalStg * 5
    character.spell = totalInl * 5
    character.crit = round(totalAgi * 0.1, 1)
    character.armor = round(setArmor(totalAgi + character.armorRating), 1)
    character.arcaneRes = round(setResistance(character.inl + character.arcaneResRating), 1)
    character.fireRes = round(setResistance(character.inl + character.fireResRating), 1)
    character.frostRes = round(setResistance(character.inl + character.frostResRating), 1)
    character.shadowRes = round(setResistance(character.inl + character.shadowResRating), 1)
    character.natureRes = round(setResistance(character.inl + character.natureResRating), 1)


def calculateStatsWithoutHp(character):
    totalStg = character.stg + BuffNDebuff.getStrBuffNDebuff(character)
    totalAgi = character.agi + BuffNDebuff.getAgiBuffNDebuff(character)
    totalInl = character.inl + BuffNDebuff.getIntBuffNDebuff(character)
    character.dmg = totalStg * 5
    character.spell = totalInl * 5
    character.crit = round(totalAgi * 0.1, 1)
    character.armor = round(setArmor(totalAgi + character.armorRating), 1)
    character.arcaneRes = round(setResistance(character.inl + character.arcaneResRating), 1)
    character.fireRes = round(setResistance(character.inl + character.fireResRating), 1)
    character.frostRes = round(setResistance(character.inl + character.frostResRating), 1)
    character.shadowRes = round(setResistance(character.inl + character.shadowResRating), 1)
    character.natureRes = round(setResistance(character.inl + character.natureResRating), 1)


def calculateHpWithBuffs(character):
    totalStg = character.stg + BuffNDebuff.getStrBuffNDebuff(character)
    return totalStg * 10


def calculateHp(character):
    character.hp = character.stg * 10


    # Stat formulas

def setCritical(criticalRating):
    return ((min(criticalRating, 500) * 0.1) +
            ((min(criticalRating - 500, 200) if not criticalRating < 500 else 0) * 0.05) +
            ((min(criticalRating - 700, 200) if not criticalRating < 700 else 0) * 0.01) +
            ((min(criticalRating - 900, 200) if not criticalRating < 900 else 0) * 0.005))

def setArmor(armorRating):
    return ((min(armorRating, 500) * 0.1) +
            ((min(armorRating - 500, 200) if not armorRating < 500 else 0) * 0.05) +
            ((min(armorRating - 700, 200) if not armorRating < 700 else 0) * 0.01) +
            ((min(armorRating - 900, 200) if not armorRating < 900 else 0) * 0.005))

def setResistance(resistanceRating):
    return ((min(resistanceRating, 500) * 0.05) +
            ((min(resistanceRating - 500, 200) if not resistanceRating < 500 else 0) * 0.01) +
            ((min(resistanceRating - 700, 200) if not resistanceRating < 700 else 0) * 0.005) +
            ((min(resistanceRating - 900, 200) if not resistanceRating < 900 else 0) * 0.001))

    #

def levelUp(character, floor):
    points = random.randint(1, floor)
    LogNColor.Printer("You got " + str(points) + " Floor Points!")
    while points > 0:
        try:
            LogNColor.Printer("Where you wanna spend them?")
            c = input()
            amount = int(list(filter(str.isdigit, c))[0])
            if amount <= points:
                if "s" in c:
                    character.stg += amount
                    points -= amount
                    LogNColor.Printer("You got " + str(amount) + " Strength")
                elif "a" in c:
                    character.agi += amount
                    points -= amount
                    LogNColor.Printer("You got " + str(amount) + " Agility")
                elif "i" in c:
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
    newArmorRes = enemy.armor * (1 + 0.5 * floor)
    newFireRes = enemy.fireRes * (1 + 0.5 * floor)
    newFrostRes = enemy.frostRes * (1 + 0.5 * floor)
    newShadowRes = enemy.shadowRes * (1 + 0.5 * floor)
    newNatureRes = enemy.natureRes * (1 + 0.5 * floor)
    enemy.stg = int(round(newStg))
    enemy.agi = int(round(newAgi))
    enemy.inl = int(round(newInl))
    enemy.armor = int(round(newArmorRes))
    enemy.fireRes = int(round(newFireRes))
    enemy.frostRes = int(round(newFrostRes))
    enemy.shadowRes = int(round(newShadowRes))
    enemy.natureRes = int(round(newNatureRes))


def itemLevelUp(item, floor):
    newStg = item.stg * (1 + 0.05 * floor)
    newAgi = item.agi * (1 + 0.05 * floor)
    newInl = item.inl * (1 + 0.05 * floor)
    newArmorRating = item.armorRating * (1 + 0.05 * floor)
    newFireResRating = item.fireResRating * (1 + 0.05 * floor)
    newFrostResRating = item.frostResRating * (1 + 0.05 * floor)
    newShadowResRating = item.shadowResRating * (1 + 0.05 * floor)
    newNatureResRating = item.natureResRating * (1 + 0.05 * floor)
    item.stg = int(round(newStg))
    item.agi = int(round(newAgi))
    item.inl = int(round(newInl))
    item.armorRating = int(round(newArmorRating))
    item.fireResRating = int(round(newFireResRating))
    item.frostResRating = int(round(newFrostResRating))
    item.shadowResRating = int(round(newShadowResRating))
    item.natureResRating = int(round(newNatureResRating))


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
