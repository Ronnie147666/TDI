import Class
import LogNColor

class Item(object):
    def __init__(self, strg=0, agi=0, intl=0, name=""):
     self.strg=strg
     self.agi=agi
     self.intl=intl
     self.name=name

 
def equipItem(player,item):
    if (len(player.items))>=6:
        LogNColor.Printer("Your inventory is full.Unequip an item first")
        LogNColor.Printer("Your inventory:")
        for idx,i in enumerate(player.items):
            LogNColor.Printer(str(idx+1)+": "+str(i.name)+" STR: "+str(i.strg)+" AGI: "+str(i.agi)+" INT: "+str(i.intl))
        return
    player.items.append(item)
    player.stg+=item.strg
    player.agi+=item.agi
    player.inl+=item.intl



def unequipItem(player,itemIndex):
            player.stg-=player.items[itemIndex].strg
            player.agi-=player.items[itemIndex].agi
            player.inl-=player.items[itemIndex].intl
            LogNColor.Printer("You unequipped "+player.items[itemIndex].name)
            player.items.pop(itemIndex)        



