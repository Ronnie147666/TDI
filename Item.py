import Class
import LogNColor


class Item(object):
    def __init__(self, stg=0, agi=0, inl=0, fireRes=0, frostRes=0, shadowRes=0, natureRes=0, name=""):
        self.stg = stg
        self.agi = agi
        self.inl = inl
        self.name = name

        self.fireRes = fireRes
        self.frostRes = frostRes
        self.shadowRes = shadowRes
        self.natureRes = natureRes


def equipItem(player, item):
    if (len(player.items)) >= 6:
        LogNColor.Printer("Your inventory is full.Unequip an item first")
        LogNColor.Printer("Your inventory:")
        for idx, i in enumerate(player.items):
            LogNColor.Printer(
                str(idx + 1) + ": " + str(i.name) + " STR: " + str(i.stg) + " AGI: " + str(i.agi) + " INT: " + str(
                    i.inl) + " FIRE RES: " + str(i.fireRes) + " FROST RES: " + str(i.frostRes) + " NATURE RES: " + str(
                    i.natureRes)+ " SHADOW RES: " + str(i.shadowRes))
        return
    player.items.append(item)
    player.stg += item.stg
    player.agi += item.agi
    player.inl += item.inl
    player.fireRes = item.fireRes
    player.frostRes = item.frostRes
    player.shadowRes = item.shadowRes
    player.natureRes = item.natureRes
    return True


def unequipItem(player, itemIndex):
    player.stg -= player.items[itemIndex].stg
    player.agi -= player.items[itemIndex].agi
    player.inl -= player.items[itemIndex].inl
    player.fireRes -= player.items[itemIndex].fireRes
    player.frostRes -= player.items[itemIndex].frostRes
    player.shadowRes -= player.items[itemIndex].shadowRes
    player.natureRes -= player.items[itemIndex].natureRes

    LogNColor.Printer("You unequipped " + player.items[itemIndex].name)
    player.items.pop(itemIndex)

def createItem(item):
    newItem = Item()
    newItem.stg = item.stg
    newItem.agi = item.agi
    newItem.inl = item.inl
    newItem.name = item.name
    newItem.fireRes = item.fireRes
    newItem.frostRes = item.frostRes
    newItem.shadowRes = item.shadowRes
    newItem.natureRes = item.natureRes
    return newItem

# def createItemWStats(stg,agi,inl,name,fireRes,frostRes,shadowRes,natureRes):
#     newItem = Item()
#     newItem.stg = stg
#     newItem.agi = agi
#     newItem.inl = inl
#     newItem.name = name
#     newItem.fireRes = fireRes
#     newItem.frostRes = frostRes
#     newItem.shadowRes = shadowRes
#     newItem.natureRes = natureRes
#     return newItem