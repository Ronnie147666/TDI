import random
import BuffNDebuff
import HotsNDots
import StatsNDice
import LogNColor

def isCritical(crit):
    chance = random.randint(0,100)+crit
    if chance>=100:
        LogNColor.Printer(str("You got a critical"))
        return True
    return False

###########################################

def preparation(player,placeHolder):
    agiBuff=int(round(player.agi/2))
    player.arm+= agiBuff*3
    player.crit+= agiBuff*0.1    
    player.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff,time=4))
    LogNColor.Printer(str("Preparation-Your Agility:%d" %(player.agi+agiBuff)))

def poison(player,target):
    dmg=int(round(player.spell/2))
    target.hp-=dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg,time=5,name="Poison"))
    LogNColor.Printer(str("Poison-Enemy HP:%d" %target.hp))
    
def backstab(player,target):
    target.hp-=(player.dmg*3)-target.arm*0.8 if not isCritical(player.crit) else (player.dmg*6)-target.arm*0.8
    LogNColor.Printer(str("Backstab-Enemy HP:%d" %target.hp))

###########################################

def shadowbolt(player,target):
    target.hp-=player.spell*2 if not isCritical(player.crit) else player.spell*4
    LogNColor.Printer(str("Shadowbolt-Enemy HP:%d" %target.hp))

def lifedrain(player,target):
    target.hp-=int(round(player.spell/2))
    player.hp+=player.spell
    LogNColor.Printer(str("Lifedrain-Enemy HP:%d" %target.hp))
    LogNColor.Printer(str("Lifedrain-Your HP:%d" %player.hp))

def immolate(player,target):
    dmg=int(round(player.spell/3))
    target.hp-=dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg,time=4,name="Immolate"))
    LogNColor.Printer(str("Immolate-Enemy HP:%d" %target.hp))


########################################
    
def lunarstrike(player,target):
    target.hp-=((player.spell*0.5)+(player.dmg*0.5))-target.arm if not isCritical(player.crit) else ((player.spell*0.5)+(player.dmg*0.5))*2-target.arm
    LogNColor.Printer(str("Lunar Strike-Enemy HP:%d" %target.hp))    


def growth(player,placeHolder):
    hpHeal=int(round(player.spell/4))
    if player.hp+hpHeal>StatsNDice.calculateHpWBuffs(player):
        player.hp = StatsNDice.calculateHpWBuffs(player)
    else:
        player.hp+=hpHeal
    player.hots.append(HotsNDots.HotNDot(hp=hpHeal,time=4,name="Growth"))
    LogNColor.Printer(str("Growth-Your HP:%d" %player.hp))

def spirituality(player,placeHolder):
    stgBuff=int(round(player.stg/2))
    agiBuff=int(round(player.agi/2))
    intBuff=int(round(player.inl/2))    
    player.dmg+= stgBuff*3
    player.arm+= agiBuff*0.1
    player.crit+= agiBuff*3
    player.spell+= intBuff*0.1 
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4))
    player.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff,time=4))
    player.buffs.append(BuffNDebuff.BuffNDebuff(inl=intBuff,time=4))
    LogNColor.Printer(str("Preparation-Your Agility:%d" %player.agi+agiBuff))

######################################

def slam(player, target):
    target.hp-=player.dmg*1.5-target.arm if not isCritical(player.crit) else player.dmg*1.5*2-target.arm
    LogNColor.Printer(str("Slam-Enemy HP: %d" %target.hp))    

def shieldblock(player,placeHolder):
    stgBuff=int(round(player.stg/4))
    player.hp+= stgBuff*10
    player.dmg+= stgBuff*5
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4))
    LogNColor.Printer(str("Shieldblock-Your Strength:%d" %player.stg+stgBuff))

def taunt(placeHolder,target):
    stgDebuff=-int(round(target.stg/4))
    target.hp+= stgDebuff*10
    target.dmg+= stgDebuff*5
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff,time=4))
    LogNColor.Printer(str("Taunt-Enemy Strength:%d" %(target.stg+stgDebuff)))
    

####################################




def heal(player,placeHolder):
    player.hp+=player.spell
    LogNColor.Printer(str("Heal-Your HP:%d" %player.hp))


########################################


    
def arcanebolt(player,target):
    target.hp-=player.spell*3 if not isCritical(player.crit) else player.spell*6
    LogNColor.Printer(str("Arcanebolt-Enemy HP:%d" %target.hp))


##################################################


def prayer(player,placeHolder):
    hpHeal=int(round(player.spell/0.2))
    if player.hp+hpHeal>StatsNDice.calculateHpWBuffs(player):
        player.hp = StatsNDice.calculateHpWBuffs(player)
    else:
        player.hp+=hpHeal
    player.hots.append(HotsNDots.HotNDot(hp=hpHeal,time=4,name="Prayer"))
    LogNColor.Printer(str("Prayer-Your HP:%d" %player.hp))

################################################

def deadlyshot(player,target):
    target.hp-=(player.dmg*2)-target.arm*0.9 if not isCritical(player.crit) else (player.dmg*4)-target.arm*0.9
    LogNColor.Printer(str("Deadly Shot-Enemy HP:%d" %target.hp))

#####################################################


def deathgrip(player,target):
    target.hp-=((player.spell*0.5)+(player.dmg*0.5))-target.arm if not isCritical(player.crit) else ((player.spell*0.5)+(player.dmg*0.5))*2-target.arm
    LogNColor.Printer(str("Death Grip-Enemy HP:%d" %target.hp))    

def deathstrike(player,target):
    target.hp-=((player.spell*0.25)+(player.dmg*0.25)) if not isCritical(player.crit) else ((player.spell*0.5)+(player.dmg*0.5))*2
    player.hp+=player.spell*0.25+player.dmg*0.25
    LogNColor.Printer(str("Death Strike-Enemy HP:%d" %target.hp))
    LogNColor.Printer(str("Death Strike-Your HP:%d" %player.hp))
    
########################################################
    
    #################################################
    
########################################################

def dragonbreath(enemy,target):
    s=enemy.spell
    target.hp-=roll(s*2,s*4) if not isCritical(enemy.crit) else roll(s*4,s*8)
    LogNColor.Printer(str("Dragonbreath-Your HP:%d" %target.hp))

def tailwhip(enemy,target):
    target.hp-=enemy.dmg*3 if not isCritical(enemy.crit) else enemy.spell*8
    LogNColor.Printer(str("Tailwhip-Your HP:%d" %target.hp))

        
    
def soulsteal(enemy,target):
    target.hp-=int(round(enemy.spell))
    enemy.hp+=enemy.spell
    LogNColor.Printer(str("Soulsteal-Your HP:%d" %target.hp))
    LogNColor.Printer(str("Soulsteal-Enemy HP:%d" %enemy.hp))

def shadowstrike(enemy,target):
    target.hp-=(enemy.dmg*3)-target.arm*0.5 if not isCritical(enemy.crit) else (enemy.dmg*6)-target.arm*0.5
    LogNColor.Printer(str("Shadow Strike-Your HP:%d" %target.hp))

def deadlybolt(enemy,target):
    target.hp-=enemy.spell*5 if not isCritical(enemy.crit) else enemy.spell*10
    LogNColor.Printer(str("Deadlybolt-Your HP:%d" %target.hp))

def sinisterstrike(enemy,target):
    target.hp-=(enemy.dmg*2)-target.arm*0.75 if not isCritical(enemy.crit) else (enemy.dmg*4)-target.arm*0.75
    LogNColor.Printer(str("Sinister Strike-Your HP:%d" %target.hp))

def titanstrike(enemy,target):
    target.hp-=(enemy.dmg*3) if not isCritical(enemy.crit) else (enemy.dmg*6)
    LogNColor.Printer(str("Titan Strike-Your HP:%d" %target.hp))

def stealife(enemy,target):
    target.hp-=int(round(enemy.spell*1.5))
    enemy.hp+=enemy.spell*1.5
    LogNColor.Printer(str("Steal Life-Your HP:%d" %target.hp))
    LogNColor.Printer(str("Steal Life-Enemy HP:%d" %enemy.hp))

def bloodstrike(enemy,target):
    target.hp-=((player.spell*0.25)+(player.dmg*0.25)) if not isCritical(player.crit) else ((player.spell*0.5)+(player.dmg*0.5))*2
    player.hp+=player.spell*0.25+player.dmg*0.25
    LogNColor.Printer(str("Blood Strike-Enemy HP:%d" %target.hp))
    LogNColor.Printer(str("Blood Strike-Your HP:%d" %player.hp))

def bloodboil(placeHolder,target):
    dmg=int(round(player.spell/2))
    target.hp-=dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg,time=3,name="Bloodboil"))
    LogNColor.Printer(str("Bloodboil-Enemy HP:%d" %target.hp))

def mutilate(enemy,target):
    target.hp-=(enemy.dmg*3) if not isCritical(enemy.crit) else (enemy.dmg*6)
    LogNColor.Printer(str("Mutilate-Your HP:%d" %target.hp))







    
