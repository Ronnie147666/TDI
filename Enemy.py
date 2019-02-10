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
     




class Dragon(Enemy):
    def __init__(self):
        super(Dragon, self).__init__()          
        self.stg=50
        self.agi=50
        self.inl=50

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

    movesList = {
    1:SpellsList.soulsteal,
    2:SpellsList.dragonbreath
}  

def createEnemy(enemyChoice):
    if (enemyChoice == 1):
        return Ghoul()
    elif (enemyChoice == 2):
        return Dragon()

##    movesList = {
##    1:SpellsList.enemyAttack,
##    2:SpellsList.drain
##}
