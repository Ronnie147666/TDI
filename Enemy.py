import SpellsList

class Enemy(object):   
    def __init__(self):
     self.stg=50
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
     self.res=0
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
        self.stg=35
        self.agi=30
        self.inl=25

    @staticmethod   
    def createDragon():
        dragon = Dragon()
        return dragon

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}    

class DarkKnight(Enemy):
    def __init__(self):
        super(DarkKnight, self).__init__()          
        self.stg=30
        self.agi=25
        self.inl=20

    @staticmethod   
    def createDarkKnight():
        darkKnight = DarkKnight()
        return darkKnight

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}    

class Lich(Enemy):
    def __init__(self):
        super(Lich, self).__init__()
        self.stg=15
        self.agi=20
        self.inl=35

    @staticmethod   
    def createLich():
        lich = Lich()
        return lich

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

class Archmage(Enemy):
    def __init__(self):
        super(Archmage, self).__init__()
        self.stg=15
        self.agi=25
        self.inl=35

    @staticmethod   
    def createArchmage():
        archmage = Archmage()
        return archmage     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}

class Demon(Enemy):
    def __init__(self):
        super(Demon, self).__init__()
        self.stg=35
        self.agi=25
        self.inl=25

    @staticmethod   
    def createDemon():
        demon = Demon()
        return demon     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}

 class UnholyGladiator(Enemy):
    def __init__(self):
        super(UnholyGladiator, self).__init__()
        self.stg=35
        self.agi=30
        self.inl=15

    @staticmethod   
    def createUnholyGladiator():
        unholyGladiator = UnholyGladiator()
        return unholyGladiator     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}
       
 class DarkWizard(Enemy):
    def __init__(self):
        super(DarkWizard, self).__init__()
        self.stg=15
        self.agi=20
        self.inl=45

    @staticmethod   
    def createDarkWizard():
        darkWizard = DarkWizard()
        return darkWizard     

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}

 class DarkCultist(Enemy):
    def __init__(self):
        super(DarkCultist, self).__init__()
        self.stg=15
        self.agi=25
        self.inl=30

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
        self.stg=25
        self.agi=30
        self.inl=35

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
        self.stg=25
        self.agi=40
        self.inl=25

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
        self.agi=25
        self.inl=25

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
        self.stg=25
        self.agi=30
        self.inl=25

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
        self.stg=25
        self.agi=25
        self.inl=30

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
        self.stg=10
        self.agi=30
        self.inl=30

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
        self.stg=25
        self.agi=40
        self.inl=10

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
