import random
import StatsNDice
import ItemList
import Item
import BuffNDebuff
import HotsNDots
import LogNColor


def fight(player, enemy, floor):
    import Rpg
    statsCalculated = False
    while player.hp > 0 and enemy.hp > 0:
        if not statsCalculated:
            HotsNDots.getHotsNDots(player)
            HotsNDots.getHotsNDots(enemy)
            StatsNDice.calculateStatsWithoutHp(player)
            StatsNDice.calculateStatsWithoutHp(enemy)
            BuffNDebuff.clearBuffsNDebuffs(player)
            BuffNDebuff.clearBuffsNDebuffs(enemy)
            statsCalculated = True
            ##try:
            for t in range(0, player.moveCount):
                LogNColor.Printer("What will you do: ")
                s = str(input())
                resolveAction(player, enemy, s)
            if enemy.hp > 0:
                resolveAction(enemy, player, random.randint(1, 2))
            else:
                lootPhase(player, floor)
                StatsNDice.levelUp(player, floor)
                StatsNDice.calculateStats(player)
            if (player.hp <= 0):
                LogNColor.Printer("You lost!")
                Rpg.startGame()
            BuffNDebuff.reduceBuffsNDebuffs(player)
            BuffNDebuff.reduceBuffsNDebuffs(enemy)
            statsCalculated = False
            ##except:
            if s == 'quit':
                Rpg.quitGame()
            LogNColor.Printer("Wrong command1")


def getLoot(floor):
    loot = []
    for i in range(0, floor):
        dice = random.randint(0, 9)
        newItem= ItemList.itemChance()[dice]
        loot.append(Item.createItem(newItem))
    return loot


def lootPhase(player, floor):
    loot = getLoot(floor)
    adjustItemLevel(floor, loot)
    LogNColor.Printer('\n'"You dropped:")
    StatsNDice.printItemStats(loot)
    while True:
        LogNColor.Printer("Would you like to equip or unequip an item?")
        c = str(input())
        try:
            if c == "continue":
                return
            elif canUnequip(c, player):
                Item.unequipItem(player, filterNumberFromString(c) - 1)
            elif canEquip(c, floor):
                if Item.equipItem(player, loot[filterNumberFromString(c) - 1]):
                    return
            else:
                LogNColor.Printer("Wrong command2")
        except:
            LogNColor.Printer("Wrong command3")


def adjustItemLevel(floor, loot):
    for l in loot:
        StatsNDice.itemLevelUp(l, floor)


def filterNumberFromString(c):
    return int(list(filter(str.isdigit, c))[0])

def resolveAction(attacker, defender, move):
    attacker.movesList[move](attacker, defender)


def findItemIndex(loot, choice):
    for idx, i in enumerate(loot):
        if i.name == choice.title():
            return idx


def canEquip(c, floor):
    # in range of floor max items
    return ("equip" in c) and (filterNumberFromString(c) in range(1, floor + 1))


def canUnequip(c, player):
    # in range of player max items
    return ("unequip" in c) and (filterNumberFromString(c) in range(1, len(player.items) + 1))
