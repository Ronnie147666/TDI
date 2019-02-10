import SpellsList


class Player(object):
    def __init__(self):
     self.stg=60
     self.agi=50
     self.inl=50
     self.bonusStg=0
     self.bonusAgi=0
     self.bonusInl=0     

     self.hp=0
     self.dmg=0
     self.arm=0
     self.crit=0     
     self.spell=0
     self.moveCount=1

     self.items=[]
     self.buffs=[]
     self.debuffs=[]
     self.dots=[]
     self.hots=[]
     self.curse=0
     


  
class Paladin(Player):
    def __init__(self):
        super(Paladin, self).__init__()
        self.hp=100
    @staticmethod   
    def createPaladin():
        paladin = Paladin()
        return paladin
    
    movesList = {
    'heal':SpellsList.heal,
    'slam':SpellsList.slam,
    'growth':SpellsList.growth,
    'immolate':SpellsList.immolate,    
    'shieldblock':SpellsList.shieldblock
}

###############
   
class Warrior(Player):
    def __init__(self):
        super(Warrior, self).__init__()
        self.hp=100

    @staticmethod   
    def createWarrior():
        warrior = Warrior()
        return warrior

    movesList = {
    'heal':SpellsList.heal,
    'growth':SpellsList.growth,
    'immolate':SpellsList.immolate,    
    'shieldblock':SpellsList.shieldblock
}

###############

class Warlock(Player):
    def __init__(self):
        super(Warlock, self).__init__()
        self.hp=100

    @staticmethod   
    def createWarlock():
        warlock = Warlock()
        return warlock

    movesList = {
    'heal':SpellsList.heal,
    'growth':SpellsList.growth,
    'immolate':SpellsList.immolate,    
    'shieldblock':SpellsList.shieldblock
}

################

class Druid(Player):
    def __init__(self):
        super(Druid, self).__init__()
        self.hp=100

    @staticmethod   
    def createDruid():
        druid = Druid()
        return druid

    movesList = {
    'heal':SpellsList.heal,
    'growth':SpellsList.growth,
    'immolate':SpellsList.immolate,    
    'shieldblock':SpellsList.shieldblock
}


################

class Rogue(Player):
    def __init__(self):
        super(Rogue, self).__init__()
        self.hp=100

    @staticmethod   
    def createRogue():
        rogue = Rogue()
        return rogue

    movesList = {
    'heal':SpellsList.heal,
    'growth':SpellsList.growth,
    'immolate':SpellsList.immolate,    
    'shieldblock':SpellsList.shieldblock
}



################

class Mage(Player):
    def __init__(self):
        super(Mage, self).__init__()
        self.hp=100

    @staticmethod   
    def createMage():
        mage = Mage()
        return mage

    movesList = {
    'heal':SpellsList.heal,
    'growth':SpellsList.growth,
    'immolate':SpellsList.immolate,    
    'shieldblock':SpellsList.shieldblock
}



classList = {

    'paladin': Paladin.createPaladin,
    'warlock': Warlock.createWarlock,
    'druid': Druid.createDruid,
    'rogue': Rogue.createRogue,
    'mage': Mage.createMage,
    'warrior': Warrior.createWarrior
    


    }
