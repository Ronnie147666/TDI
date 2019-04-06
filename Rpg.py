import random
import Class
import Enemy
import StatsNDice
import Fight
import LogNColor



def startGame():
    LogNColor.setColor("yellow")
    LogNColor.Printer(str("Welcome to the Colosseum!"))
    p = None
    floor = 0
    while p == None:
          try:
                LogNColor.Printer(str("What class do you choose:"))
                for key in Class.classList.keys():
                    LogNColor.Printer(key.title())
                c = str(raw_input())                
                p = Class.classList[c]()
          except:
                LogNColor.Printer(str("Wrong class!"))


    while(True):
      floor+=1
      p.buffs=[]
      p.debuffs=[]
      p.hots=[]
      p.dots=[]      
      StatsNDice.calculateStats(p)
      e = Enemy.enemyList[random.randint(1,45)]()
      StatsNDice.enemyLevelUp(e,floor-1)
      StatsNDice.calculateStats(e)
      LogNColor.Printer("Floor: "+str(floor))
      LogNColor.Printer(str("Your next fight will be a " +str(type(e).__name__)+'\n'))

      LogNColor.Printer(str("You stats:"'\n'))
      LogNColor.Printer("Hp:"+str(p.hp))
      LogNColor.Printer("Dmg:"+str(p.dmg))
      LogNColor.Printer("Arm:"+str(p.arm))
      LogNColor.Printer("Crit:"+str(p.crit))
      LogNColor.Printer("Spell:"+str(p.spell))
      LogNColor.Printer("Strength:"+str(p.stg))
      LogNColor.Printer("Agility:"+str(p.agi))
      LogNColor.Printer("")
      
      if p.items:
          LogNColor.Printer("Your items:")
          for idx,i in enumerate(p.items):
              LogNColor.Printer(str(idx+1)+": "+str(i.name)+" STR: "+str(i.strg)+" AGI: "+str(i.agi)+" INT: "+str(i.intl))
          LogNColor.Printer("")    

      LogNColor.Printer(str("Your enemy stats:"'\n'))
      LogNColor.Printer("Hp:"+str(e.hp))
      LogNColor.Printer("Dmg:"+str(e.dmg))
      LogNColor.Printer("Arm:"+str(e.arm))
      LogNColor.Printer("Crit:"+str(e.crit))
      LogNColor.Printer("Spell:"+str(e.spell))
      LogNColor.Printer("Strength:"+str(e.stg))
      LogNColor.Printer("Strength:"+str(e.agi))
      LogNColor.Printer("")
      
      
      Fight.fight(p,e,floor)

if __name__ == '__main__':
    startGame()  

def quitGame():
      startGame()

def resetCharacterBuffs(character):
      p.buffs=[]
      p.debuffs=[]
    
    

   
  
  
