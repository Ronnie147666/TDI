import random
import Class
import Enemy
import StatsNDice
import Fight
import LogNColor

def printStats(character):
    LogNColor.Printer(LogNColor.splitWords(type(character).__name__)+str(" Stats:"'\n'))
    LogNColor.Printer("Strength:" + str(character.stg)+"   |"+"Hp:" + str(character.hp)+"    |"+"Crit:" + str(character.crit))
    LogNColor.Printer("Agility:" + str(character.agi)+"    |"+"Dmg:" + str(character.dmg)+"   |"+"Spell:" + str(character.spell))
    LogNColor.Printer("Intellect:" + str(character.inl)+"  |"+"Arm:" + str(character.arm)+"    |"+"Resistance:" + str(character.res))
    LogNColor.Printer("\nFire Res:" + str(character.fireRes)+"\nIce Res:" + str(character.frostRes))
    LogNColor.Printer("Shadow Res:" + str(character.shadowRes)+"\nNature Res:" + str(character.natureRes))
    LogNColor.Printer("")


def resetCharacterBuffs(character):
    character.buffs = []
    character.debuffs = []
    character.hots = []
    character.dots = []


def startGame():
    LogNColor.setColor("yellow")
    LogNColor.Printer(str("Welcome to the Colosseum!"))
    p = None
    floor = 0
    while p == None:
        try:
            LogNColor.Printer(str("What class do you choose:"))
            for key in Class.classList.keys():
                LogNColor.Printer(key.title())
            c = str(input())
            p = Class.classList[c]()
            LogNColor.Printer('\n' + str(type(p).__name__) + str(" Spells:"))
            Class.displayClassSpell(p)
        except:
            LogNColor.Printer(str("Wrong class!"))

    while (True):
        resetCharacterBuffs(p)
        floor += 1
        p.buffs = []
        p.debuffs = []
        p.hots = []
        p.dots = []
        StatsNDice.calculateStats(p)
        e = Enemy.enemyList[random.randint(0, 140)]()
        StatsNDice.enemyLevelUp(e, floor - 1)
        StatsNDice.calculateStats(e)
        LogNColor.Printer('\n'"       ---------------------------------------                  ")
        LogNColor.Printer('\n'"Floor: " + str(floor))
        LogNColor.Printer(str("Your next fight will be a " + str(LogNColor.splitWords(type(e).__name__)) + '\n'))

        printStats(p)

        if p.items:
            LogNColor.Printer("Your items:")
            for idx, i in enumerate(p.items):
                LogNColor.Printer(
                    str(idx + 1) + ": " + str(i.name) + " STR: " + str(i.stg) + " AGI: " + str(i.agi) + " INT: " + str(
                        i.inl))
            LogNColor.Printer("")

        printStats(e)

        Fight.fight(p, e, floor)


if __name__ == '__main__':
    startGame()


def quitGame():
    startGame()
