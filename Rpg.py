import random
import Class
import Enemy
import Item
import StatsNDice
import Battle
import LogNColor

def startGame():
    LogNColor.setColor("magenta")
    LogNColor.Printer(str("Welcome to the Colosseum!"))
    p = None
    floor = 0
    while p is None:
        p = classSelection(p)

    while True:
        resetCharacterBuffs(p)
        floor += 1
        StatsNDice.calculateStats(p)
        e = prepareEnemy(floor)
        LogNColor.printNextFloor(e, floor)

        LogNColor.printCharacterStats(p)

        if p.items:
            LogNColor.printCharacterItems(p)

        LogNColor.printCharacterStats(e)

        if e.items:
            LogNColor.printCharacterItems(e)

        Battle.battle(p, e, floor)

def resolveClassSelection(index):
    return Class.classList[list(Class.classList.keys())[index]]()


def resetCharacterBuffs(character):
    character.buffs = []
    character.debuffs = []
    character.hots = []
    character.dots = []

def prepareEnemy(floor):
    e = Enemy.enemyList[random.randint(0, 140)]()
    Item.enemyGearUp(e)
    Item.adjustItemLevel(e.items, floor)
    Item.calculateEnemyStatsWithItems(e)
    StatsNDice.enemyLevelUp(e, floor - 1)
    StatsNDice.calculateStats(e)
    return e


def classSelection(p):
    try:
        LogNColor.printClassChoicePrompt()
        for idx, val in enumerate(Class.classList):
            LogNColor.Printer(str(idx + 1) + "." + val.title())
        c = int(input())
        p = resolveClassSelection(c - 1)
        LogNColor.printClassSpells(p)
    except:
        LogNColor.Printer(str("Wrong class!"))
    return p


if __name__ == '__main__':
    startGame()


def quitGame():
    startGame()
