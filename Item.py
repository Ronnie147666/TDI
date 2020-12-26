import random

import Class
import ItemList
import LogNColor
import StatsNDice


class Item(object):
    def __init__(self,
                 stg=0, agi=0, inl=0,
                 armorRating=0, fireResRating=0, arcaneResRating=0,
                 frostResRating=0, shadowResRating=0, natureResRating=0,
                 name=""):
        self.stg = stg
        self.agi = agi
        self.inl = inl
        self.name = name

        self.armorRating = armorRating
        self.arcaneResRating = arcaneResRating
        self.fireResRating = fireResRating
        self.frostResRating = frostResRating
        self.shadowResRating = shadowResRating
        self.natureResRating = natureResRating


def equipItem(player, item):
    if (len(player.items)) >= 6:
        LogNColor.Printer("Your inventory is full.Unequip an item first")
        LogNColor.Printer("Your inventory:")
        LogNColor.printItemStats(player.items)
        return
    player.items.append(item)
    player.stg += item.stg
    player.agi += item.agi
    player.inl += item.inl
    player.armorRating += item.armorRating
    player.arcaneResRating += item.arcaneResRating
    player.fireResRating += item.fireResRating
    player.frostResRating += item.frostResRating
    player.shadowResRating += item.shadowResRating
    player.natureResRating += item.natureResRating
    return True


def unequipItem(player, itemIndex):
    player.stg -= player.items[itemIndex].stg
    player.agi -= player.items[itemIndex].agi
    player.inl -= player.items[itemIndex].inl
    player.armorRating -= player.items[itemIndex].armorRating
    player.arcaneResRating -= player.items[itemIndex].arcaneResRating
    player.fireResRating -= player.items[itemIndex].fireResRating
    player.frostResRating -= player.items[itemIndex].frostResRating
    player.shadowResRating -= player.items[itemIndex].shadowResRating
    player.natureResRating -= player.items[itemIndex].natureResRating

    LogNColor.Printer("You unequipped " + player.items[itemIndex].name)
    player.items.pop(itemIndex)

def createItem(item):
    newItem = Item()
    newItem.stg = item.stg
    newItem.agi = item.agi
    newItem.inl = item.inl
    newItem.name = item.name
    newItem.armorRating = item.armorRating
    newItem.arcaneResRating = item.arcaneResRating
    newItem.fireResRating = item.fireResRating
    newItem.frostResRating = item.frostResRating
    newItem.shadowResRating = item.shadowResRating
    newItem.natureResRating = item.natureResRating
    return newItem

def enemyGearUp(enemy):
    for i in range(0, StatsNDice.roll(0, 6)):
        dice = random.randint(0, 120)
        newItem = ItemList.itemChance()[dice]
        enemy.items.append(createItem(newItem))

def adjustItemLevel(loot, floor):
    for l in loot:
        StatsNDice.itemLevelUp(l, floor)

def calculateEnemyStatsWithItems(character):
    for item in character.items:
        character.stg += item.stg
        character.agi += item.agi
        character.inl += item.inl
        character.armorRating += item.armorRating
        character.arcaneResRating += item.arcaneResRating
        character.fireResRating += item.fireResRating
        character.frostResRating += item.frostResRating
        character.shadowResRating += item.shadowResRating
        character.natureResRating += item.natureResRating


