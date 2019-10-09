import Class
import LogNColor


class Item(object):
    def __init__(self, stg=0, agi=0, inl=0, name=""):
        self.stg = stg
        self.agi = agi
        self.inl = inl
        self.name = name

        self.fireRes = 0
        self.frostRes = 0
        self.shadowRes = 0
        self.poisonRes = 0


def equipItem(player, item):
    if (len(player.items)) >= 6:
        LogNColor.Printer("Your inventory is full.Unequip an item first")
        LogNColor.Printer("Your inventory:")
        for idx, i in enumerate(player.items):
            LogNColor.Printer(
                str(idx + 1) + ": " + str(i.name) + " STR: " + str(i.stg) + " AGI: " + str(i.agi) + " INT: " + str(
                    i.inl))
        return
    player.items.append(item)
    player.stg += item.stg
    player.agi += item.agi
    player.inl += item.inl
    return True


def unequipItem(player, itemIndex):
    player.stg -= player.items[itemIndex].stg
    player.agi -= player.items[itemIndex].agi
    player.inl -= player.items[itemIndex].inl
    LogNColor.Printer("You unequipped " + player.items[itemIndex].name)
    player.items.pop(itemIndex)

def createItem(item):
    newItem = Item()
    newItem.stg = item.stg
    newItem.agi = item.agi
    newItem.inl = item.inl
    newItem.name = item.name
    return newItem

def createItemWStats(stg,agi,inl,name):
    newItem = Item()
    newItem.stg = stg
    newItem.agi = agi
    newItem.inl = inl
    newItem.name = name
    return newItem