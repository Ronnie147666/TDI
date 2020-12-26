import random
import StatsNDice
import ItemList
import Item
import BuffNDebuff
import HotsNDots
import LogNColor


def battle(player, enemy, floor):
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
            # try:
            for t in range(0, player.moveCount):
                LogNColor.Printer("What will you do: ")
                showCharacterSpells(player)
                s = int(input())
                resolveAction(player, enemy, s - 1)
            if enemy.hp > 0:
                resolveAction(enemy, player, random.randint(1, 2))
            else:
                lootPhase(player, enemy, floor)
                StatsNDice.levelUp(player, floor)
                StatsNDice.calculateStats(player)
            if player.hp <= 0:
                LogNColor.Printer("You lost!")
                Rpg.startGame()
            BuffNDebuff.reduceBuffsNDebuffs(player)
            BuffNDebuff.reduceBuffsNDebuffs(enemy)
            statsCalculated = False
            # except:
            if s == 'quit':
                Rpg.quitGame()
            LogNColor.Printer("Wrong command1")


def lootPhase(player, enemy, floor):
    if enemy.items:
        loot = enemy.items
    else:
        LogNColor.Printer('\n'"You dropped nothing!")
        return
    LogNColor.Printer('\n'"You dropped:")
    LogNColor.printItemStats(loot)
    while True:
        LogNColor.Printer("Would you like to equip or unequip an item?")
        c = str(input())
        try:
            if c == "continue":
                return
            elif c[0] == "e" and canEquip(c, loot):
                Item.equipItem(player, loot[filterNumberFromString(c) - 1])
                return
            elif c[0] == "u" and canUnequip(c, player):
                Item.unequipItem(player, filterNumberFromString(c) - 1)
            else:
                LogNColor.Printer("Wrong command2")
        except:
            LogNColor.Printer("Wrong command3")


def filterNumberFromString(c):
    return int(list(filter(str.isdigit, c))[0])


def resolveAction(attacker, defender, move):
    attacker.movesList[list(attacker.movesList.keys())[move]](attacker, defender)


def findItemIndex(loot, choice):
    for idx, i in enumerate(loot):
        if i.name == choice.title():
            return idx


def showCharacterSpells(character):
    for idx, val in enumerate(character.movesList):
        LogNColor.Printer(str(idx + 1) + "." + val.title())


def canEquip(c, loot):
    # check if number given is in range of loot's max index
    return filterNumberFromString(c) in range(1, len(loot) + 1)


def canUnequip(c, player):
    # check if number given is in range of player's inventory max index
    return filterNumberFromString(c) in range(1, len(player.items) + 1)
