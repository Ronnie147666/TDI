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
                LogNColor.Printer('\n'+str(type(p).__name__)+str(" Spells:"))
                Class.displayClassSpell(p)
          except:
                LogNColor.Printer(str("Wrong class!"))


    while(True):
      floor+=1
      p.buffs=[]
      p.debuffs=[]
      p.hots=[]
      p.dots=[]      
      StatsNDice.calculateStats(p)
      e = Enemy.enemyList[random.randint(0,140)]()
      StatsNDice.enemyLevelUp(e,floor-1)
      StatsNDice.calculateStats(e)
      LogNColor.Printer('\n'"       ---------------------------------------                  ")
      LogNColor.Printer('\n'"Floor: "+str(floor))
      LogNColor.Printer(str("Your next fight will be a " +str(LogNColor.splitWords(type(e).__name__))+'\n'))

      LogNColor.Printer(str("Your stats:"'\n'))
      LogNColor.Printer("Strength:"+str(p.stg))
      LogNColor.Printer("Agility:"+str(p.agi))
      LogNColor.Printer("Intellect:"+str(p.inl))
      LogNColor.Printer("Hp:"+str(p.hp))
      LogNColor.Printer("Dmg:"+str(p.dmg))
      LogNColor.Printer("Arm:"+str(p.arm))
      LogNColor.Printer("Crit:"+str(p.crit))
      LogNColor.Printer("Spell:"+str(p.spell))
      LogNColor.Printer("Resistance:"+str(p.res))
      LogNColor.Printer("")
      
      if p.items:
          LogNColor.Printer("Your items:")
          for idx,i in enumerate(p.items):
              LogNColor.Printer(str(idx+1)+": "+str(i.name)+" STR: "+str(i.stg)+" AGI: "+str(i.agi)+" INT: "+str(i.inl))
          LogNColor.Printer("")    

      LogNColor.Printer(str("Enemy stats:"'\n'))
      LogNColor.Printer("Strength:"+str(e.stg))
      LogNColor.Printer("Agility:"+str(e.agi))
      LogNColor.Printer("Intellect:"+str(e.inl))
      LogNColor.Printer("Hp:"+str(e.hp))
      LogNColor.Printer("Dmg:"+str(e.dmg))
      LogNColor.Printer("Arm:"+str(e.arm))
      LogNColor.Printer("Crit:"+str(e.crit))
      LogNColor.Printer("Spell:"+str(e.spell))
      LogNColor.Printer("Resistance:"+str(e.res))
      LogNColor.Printer("")
      
      
      Fight.fight(p,e,floor)

if __name__ == '__main__':
    startGame()  

def quitGame():
      startGame()

def resetCharacterBuffs(character):
      p.buffs=[]
      p.debuffs=[]
    
    

   
  
  
