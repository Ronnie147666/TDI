import LogNColor
import StatsNDice

class HotNDot(object):
    def __init__(self, hp=0, time=0, name= ""):
     self.hp=hp
     self.time=time
     self.name=name


def getHotsNDots(character):
    for dot in character.dots:
        character.hp-=int(round(dot.hp))
        dot.time-=1
        LogNColor.Printer(str("Enemy got "+str(int(round(dot.hp)))+" damage from "+dot.name))
    for hot in character.hots:
        if character.hp+hot.hp>StatsNDice.calculateHpWBuffs(character):
            LogNColor.Printer(str("You heal "+str(StatsNDice.calculateHpWBuffs(character)-character.hp)+" HP from "+hot.name))
            character.hp=StatsNDice.calculateHpWBuffs(character)
            return character
        character.hp+=int(round(hot.hp))
        hot.time-=1
        LogNColor.Printer(str("You heal "+str(int(round(hot.hp)))+" HP from "+hot.name))

    



def clearBuffs(character):
    character.dots = [dot for dot in character.dots if dot.time > 0]
    character.hots = [hot for hot in character.hots if hot.time > 0]








    
