import SpellsList

class Enemy(object):   
    def __init__(self):
     self.stg=20
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

     self.buffs=[]
     self.debuffs=[]
     self.dots=[]
     self.hots=[]
     self.curse=0
     

###################################


class Dragon(Enemy):
    def __init__(self):
        super(Dragon, self).__init__()          
        self.stg=50
        self.agi=50
        self.inl=50

    @staticmethod   
    def createDragon():
        dragon = Dragon()
        return dragon

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}    

class Ghoul(Enemy):
    def __init__(self):
        super(Ghoul, self).__init__()
        self.stg=30
        self.agi=30
        self.inl=30

    @staticmethod   
    def createGhoul():
        ghoul = Ghoul()
        return ghoul

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

class Archmage(Enemy):
    def __init__(self):
        super(Archmage, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createArchmage():
        archmage = Archmage()
        return archmage     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}

class Basilisk(Enemy):
    def __init__(self):
        super(Basilisk, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createBasilisk():
        basilisk = Basilisk()
        return basilisk     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}

 class Berserker(Enemy):
    def __init__(self):
        super(Berserker, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createBerserker():
        berserker = Berserker()
        return berserker     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}
       
 class FireGolem(Enemy):
    def __init__(self):
        super(FireGolem, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createFireGolem():
        fireGolem = FireGolem()
        return fireGolem     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}

 class DarkCultist(Enemy):
    def __init__(self):
        super(DarkCultist, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createDarkCultist():
        darkCultist = DarkCultist()
        return darkCultist     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}   

 class CursedDjinni(Enemy):
    def __init__(self):
        super(CursedDjinni, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createCursedDjinni():
        cursedDjinni = CursedDjinni()
        return cursedDjinni     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

 class DrowRanger(Enemy):
    def __init__(self):
        super(DrowRanger, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createDrowRanger():
        drowRanger = DrowRanger()
        return drowRanger     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

 class FireElemental(Enemy):
    def __init__(self):
        super(FireElemental, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createElemental():
        fireElemental = FireElemental()
        return fireElemental     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

 class WindElemental(Enemy):
    def __init__(self):
        super(WindElemental, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createWindElemental():
        windElemental = WindElemental()
        return windElemental     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

 class WaterElemental(Enemy):
    def __init__(self):
        super(WaterElemental, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createWaterElemental():
        waterElemental = WaterElemental()
        return waterElemental     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

 class Ghost(Enemy):
    def __init__(self):
        super(Ghost, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createGhost():
        ghost = Ghost()
        return ghost     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

 class MercilessGladiator(Enemy):
    def __init__(self):
        super(MercilessGladiator, self).__init__()
        self.stg=30
        self.agi=50
        self.inl=90

    @staticmethod   
    def createMercilessGladiator():
        mercilessGladiator = MercilessGladiator()
        return mercilessGladiator     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  
                        
    
###################################
    
enemyList = {
    1:Dragon.createDragon,
    2:Ghoul.createGhoul,
    3:Archmage.createArchmage

    }
