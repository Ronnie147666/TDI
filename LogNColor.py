import platform
import re
import math

from colorama import init, Fore, Style

if platform.system() == "Windows":
    init(convert=True)


def setColor(color):
    print(colors[color])


def Printer(output):
    print(Style.BRIGHT + output)


colors = {

    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE

}


def splitWords(word):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", word)


##Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
##Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
##Style: DIM, NORMAL, BRIGHT, RESET_ALL

# In-Game Logging

def printNextFloor(e, floor):
    Printer('\n'"       ---------------------------------------                  ")
    Printer('\n'"Floor: " + str(floor))
    Printer(str("Your next fight will be a " + str(splitWords(type(e).__name__)) + '\n'))


def printClassSpells(c):
    Printer('\n' + str(type(c).__name__) + str(" Spells:"))
    for key in c.movesList.keys():
        print(key.title())


def printClassChoicePrompt():
    Printer(str("What class do you choose:"))


# NOT USED
def getItemNameDigitMaxOffset(items):
    itemNames = [i.name for i in items]
    return len(max(itemNames, key=len))


def getItemNameDigitOffset(itemName, maxOffset):
    return maxOffset - len(itemName)


def getNumberDigitLength(number):
    if number <= 0:
        return 0
    else:
        return int(math.log10(number)) + 1


def printCharacterItems(c):
    Printer(type(c).__name__ + " items:")
    printItemStats(c.items)
    Printer("")


def printItemStats(items):
    maxOffset = getItemNameDigitMaxOffset(items)
    for idx, i in enumerate(items):
        Printer(
            str(idx + 1) + "." +
            str(i.name).ljust(20)
            + " STR: " + str(i.stg).ljust(5)
            + " AGI: " + str(i.agi).ljust(5)
            + " INT: " + str(i.inl).ljust(5)
            + " ARMOR RATING: " + str(i.armorRating).ljust(5)
            + " FIRE RES: " + str(i.fireResRating).ljust(5)
            + " FROST RES: " + str(i.frostResRating).ljust(5)
            + " NATURE RES: " + str(i.natureResRating).ljust(5)
            + " SHADOW RES: " + str(i.shadowResRating).ljust(5))

def printCharacterStats(character):
    Printer(splitWords(type(character).__name__) + str(" Stats:"'\n'))
    Printer(
        "Hp: " + str(character.hp) +
        "\nStrength: " + str(character.stg).ljust(17) +
        "Dmg: " + str(character.dmg).ljust(19) +
        "Armor: " + str(character.armor).ljust(20) +
        "Shadow Res: " + str(character.shadowRes) +

        "\nAgility: " + str(character.agi).ljust(18) +
        "Spell: " + str(character.spell).ljust(17) +
        "Fire Res: " + str(character.fireRes).ljust(17) +
        "Nature Res: " + str(character.natureRes) +

        "\nIntellect: " + str(character.inl).ljust(16) +
        "Crit: " + str(character.crit).ljust(18) +
        "Ice Res: " + str(character.frostRes).ljust(17) + "\n")


# NOT USED
# def getItemNameDigitMaxOffset(items):
#     itemNames = [i.name for i in items]
#     return len(max(itemNames, key=len))
#
# def getItemNameDigitOffset(itemName, maxOffset):
#     return maxOffset - len(itemName)
#
# def getNumberDigitLength(number):
#     if number <= 0:
#         return 0
#     else:
#         return int(math.log10(number)) + 1
