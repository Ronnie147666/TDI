import EnemySpellsList
import StatsNDice

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
    def create():
        dragon = Dragon()
        return dragon

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}    

class DarkKnight(Enemy):
    def __init__(self):
        super(DarkKnight, self).__init__()          
        self.stg=30
        self.agi=25
        self.inl=20

    @staticmethod   
    def create():
        darkKnight = DarkKnight()
        return darkKnight

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}    

class Lich(Enemy):
    def __init__(self):
        super(Lich, self).__init__()
        self.stg=15
        self.agi=20
        self.inl=35

    @staticmethod   
    def create():
        lich = Lich()
        return lich

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}  

class Archmage(Enemy):
    def __init__(self):
        super(Archmage, self).__init__()
        self.stg=15
        self.agi=25
        self.inl=35

    @staticmethod   
    def create():
        archmage = Archmage()
        return archmage     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}

class Demon(Enemy):
    def __init__(self):
        super(Demon, self).__init__()
        self.stg=35
        self.agi=25
        self.inl=25

    @staticmethod   
    def create():
        demon = Demon()
        return demon     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}

class UnholyGladiator(Enemy):
    def __init__(self):
        super(UnholyGladiator, self).__init__()
        self.stg=35
        self.agi=30
        self.inl=15

    @staticmethod   
    def create():
        unholyGladiator = UnholyGladiator()
        return unholyGladiator     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}
       
class DarkWizard(Enemy):
    def __init__(self):
        super(DarkWizard, self).__init__()
        self.stg=15
        self.agi=20
        self.inl=45

    @staticmethod   
    def create():
        darkWizard = DarkWizard()
        return darkWizard     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}

class Dreadlord(Enemy):
    def __init__(self):
        super(Dreadlord, self).__init__()
        self.stg=15
        self.agi=25
        self.inl=30

    @staticmethod   
    def create():
        dreadlord = Dreadlord()
        return dreadlord     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}   

class CursedDjinni(Enemy):
    def __init__(self):
        super(CursedDjinni, self).__init__()
        self.stg=25
        self.agi=30
        self.inl=35

    @staticmethod   
    def create():
        cursedDjinni = CursedDjinni()
        return cursedDjinni     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}  

class DrowRanger(Enemy):
    def __init__(self):
        super(DrowRanger, self).__init__()
        self.stg=25
        self.agi=40
        self.inl=25

    @staticmethod   
    def create():
        drowRanger = DrowRanger()
        return drowRanger     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}  

class FireElemental(Enemy):
    def __init__(self):
        super(FireElemental, self).__init__()
        self.stg=30
        self.agi=25
        self.inl=25

    @staticmethod   
    def create():
        fireElemental = FireElemental()
        return fireElemental     

    movesList = {
    1:EnemySpellsList.firestrike,
    2:EnemySpellsList.fireinvocation,
    3:EnemySpellsList.firestorm
}  

class WindElemental(Enemy):
    def __init__(self):
        super(WindElemental, self).__init__()
        self.stg=25
        self.agi=30
        self.inl=25

    @staticmethod   
    def create():
        windElemental = WindElemental()
        return windElemental     

    movesList = {
    1:EnemySpellsList.windstrike,
    2:EnemySpellsList.windinvocation,
    3:EnemySpellsList.windstorm
}  

class WaterElemental(Enemy):
    def __init__(self):
        super(WaterElemental, self).__init__()
        self.stg=25
        self.agi=25
        self.inl=30

    @staticmethod   
    def create():
        waterElemental = WaterElemental()
        return waterElemental     

    movesList = {
    1:EnemySpellsList.waterstrike,
    2:EnemySpellsList.waterinvocation,
    3:EnemySpellsList.waterstorm
}  

class Ghost(Enemy):
    def __init__(self):
        super(Ghost, self).__init__()
        self.stg=10
        self.agi=30
        self.inl=30

    @staticmethod   
    def create():
        ghost = Ghost()
        return ghost     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}  

class MercilessGladiator(Enemy):
    def __init__(self):
        super(MercilessGladiator, self).__init__()
        self.stg=25
        self.agi=40
        self.inl=10

    @staticmethod   
    def create():
        mercilessGladiator = MercilessGladiator()
        return mercilessGladiator     

    movesList = {
    1:EnemySpellsList.soulsteal,
    2:EnemySpellsList.dragonbreath
}  
                        
    
###################################
    
##enemyList = {
##    1:Dragon.create,
##    2:FireElemental.create,
##    3:WindElemental.create,
##    4:WaterElemental.create,
##    5:Archmage.create
##
##    }


enemyList = StatsNDice.range_dict(
                     (range(0,10), Dragon.create),
                     (range(10,20), FireElemental.create),
                     (range(20,30), WindElemental.create),
                     (range(30,40), WaterElemental.create),
                     (range(40,45), Archmage.create))





