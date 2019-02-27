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
     

#################
  
class Paladin(Player):
    def __init__(self):
        super(Paladin, self).__init__()
        self.hp=100
    @staticmethod   
    def createPaladin():
        paladin = Paladin()
        return paladin
    
    movesList = {
    'heal':SpellsList.heal
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
    'slam':SpellsList.slam,
    'shieldblock':SpellsList.shieldblock,
    'taunt':SpellsList.taunt
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
    'shadowbolt':SpellsList.shadowbolt,
    'lifedrain':SpellsList.lifedrain,    
    'immolate':SpellsList.immolate
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
    'lunarstrike':SpellsList.lunarstrike,
    'growth':SpellsList.growth,    
    'spirituality':SpellsList.spirituality
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
    'preparation':SpellsList.preparation,
    'poison':SpellsList.poison,
    'backstab':SpellsList.backstab
}

################

class Priest(Player):
    def __init__(self):
        super(Priest, self).__init__()
        self.hp=100

    @staticmethod   
    def createPriest():
        priest = Priest()
        return priest

    movesList = {
    'prayer':SpellsList.prayer
}

################

class DeathKnight(Player):
    def __init__(self):
        super(DeathKnight, self).__init__()
        self.hp=100

    @staticmethod   
    def createDeathKnight():
        deathKnight = DeathKnight()
        return deathKnight

    movesList = {
    'deathstrike':SpellsList.deathstrike,
    'deathgrip':SpellsList.deathgrip
}

################

class Ranger(Player):
    def __init__(self):
        super(Ranger, self).__init__()
        self.hp=100

    @staticmethod   
    def createRanger():
        ranger = Ranger()
        return ranger

    movesList = {
    'deadlyshot':SpellsList.deathstrike
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
    'arcanebolt':SpellsList.arcanebolt
}



classList = {

    'paladin': Paladin.createPaladin,
    'warlock': Warlock.createWarlock,
    'druid': Druid.createDruid,
    'rogue': Rogue.createRogue,
    'mage': Mage.createMage,
    'warrior': Warrior.createWarrior,
    'priest': Priest.createPriest,
    'ranger': Ranger.createRanger,
    'death knight': DeathKnight.createDeathKnight

    }
