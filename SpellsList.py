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
    intBuff=int(round(player.inl/2))
    player.arm+= agiBuff*3
    player.crit+= agiBuff*0.1
    player.spell+= intBuff*5
    player.res+= intBuff*3
    player.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff,inl=intBuff,time=4))
    LogNColor.Printer(str("Preparation-Your Agility:%d" %(player.agi+agiBuff)))
    LogNColor.Printer(str("Preparation-Your Intellect:%d" %(player.inl+intBuff)))

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
    player.hp= player.stg*10  
    player.dmg+= stgBuff*3
    player.arm+= agiBuff*0.1
    player.crit+= agiBuff*3
    player.spell+= intBuff*5
    player.res+= intBuff*3
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,agi=agiBuff,inl=intBuff,time=4))
    LogNColor.Printer(str("Spirituality-Your Strength:%d" %(player.stg+stgBuff)))
    LogNColor.Printer(str("Spirituality-Your Agility:%d" %(player.agi+agiBuff)))
    LogNColor.Printer(str("Spirituality-Your Intellect:%d" %(player.inl+intBuff)))

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

def crusaderstrike(player,target):
    dmg=(player.dmg*2)-(target.arm*0.75)
    target.hp-=dmg if not isCritical(player.crit) else dmg*2
    LogNColor.Printer(str("Crusader Strike-Enemy HP:%d" %target.hp))

def blessingofkings(player,placeHolder):
    stgBuff=int(round(player.stg/2))
    inlBuff=int(round(player.inl/2))
    player.dmg+=stgBuff*10
    player.dmg+=stgBuff*5
    player.spell+=inlBuff*5
    player.res+=inlBuff*3

    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,inl=inlBuff,time=4),)
    LogNColor.Printer(str("Blessing Of Kings-Your Strength:%d" %(player.stg+stgBuff)))
    LogNColor.Printer(str("Blessing Of Kings-Your Intellect:%d" %(player.inl+inlBuff)))

def heal(player,placeHolder):
    player.hp+=player.spell
    LogNColor.Printer(str("Heal-Your HP:%d" %player.hp))


########################################

def arcanepower(player,placeHolder):
    inlBuff=int(round(player.inl/2))
    player.spell+=inlBuff*5
    player.res+=inlBuff*3
    player.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff,time=4),)
    LogNColor.Printer(str("Arcane Power-Your Intellect:%d" %(player.inl+inlBuff)))
    
def arcanebolt(player,target):
    target.hp-=player.spell*3 if not isCritical(player.crit) else player.spell*6
    LogNColor.Printer(str("Arcanebolt-Enemy HP:%d" %target.hp))

def ignite(player,target):
    dmg=int(round(player.spell/2,5))
    target.hp-=dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg,time=4,name="ignite"))
    LogNColor.Printer(str("Ignite-Enemy HP:%d" %target.hp))
    
##################################################

def prayer(player,placeHolder):
    hpHeal=int(round(player.spell/0.2))
    if player.hp+hpHeal>StatsNDice.calculateHpWBuffs(player):
        player.hp = StatsNDice.calculateHpWBuffs(player)
    else:
        player.hp+=hpHeal
    player.hots.append(HotsNDots.HotNDot(hp=hpHeal,time=4,name="Prayer"))
    LogNColor.Printer(str("Prayer-Your HP:%d" %player.hp))

def silence(player,enemy):
    intDebuff=int(round(player.inl/3))
    enemy.spell-= intBuff*5
    enemy.res-= intBuff*3
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(inl=intDebuff,time=4))
    LogNColor.Printer(str("Silence-Enemy Intellect:%d" %enemy.inl+intDebuff))

def penance(player,target):
    target.hp-=player.spell*2 if not isCritical(player.crit) else player.spell*4
    LogNColor.Printer(str("Penance-Enemy HP:%d" %target.hp))

################################################

def wildcall(player,placeHolder):
    stgBuff=int(round(player.stg/2))
    agiBuff=int(round(player.agi/2))
    player.dmg+=stgBuff*10
    player.dmg+=stgBuff*5
    player.arm+= agiBuff*3
    player.crit+= agiBuff*0.1
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,agi=agiBuff,time=4))
    LogNColor.Printer(str("Wild Call-Your Strength:%d" %(player.stg+stgBuff)))
    LogNColor.Printer(str("Wild Call-Your Agility:%d" %(player.agi+agiBuff)))

def deadlyshot(player,target):
    target.hp-=(player.dmg*2)-target.arm*0.9 if not isCritical(player.crit) else (player.dmg*4)-target.arm*0.9
    LogNColor.Printer(str("Deadly Shot-Enemy HP:%d" %target.hp))

def paralyzeshot(player,enemy):
    agiDebuff=int(round(player.agi/3))
    enemy.arm-= agiBuff*0.1
    enemy.crit-= agiBuff*3
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(agi=agiDebuff,time=4))
    LogNColor.Printer(str("Paralyze Shot-Enemy Agility:%d" %enemy.agi+agiDebuff))

#####################################################


def deathgrip(player,target):
    target.hp-=((player.spell*0.5)+(player.dmg*0.5))-target.arm if not isCritical(player.crit) else ((player.spell*0.5)+(player.dmg*0.5))*2-target.arm
    LogNColor.Printer(str("Death Grip-Enemy HP:%d" %target.hp))    

def deathstrike(player,target):
    target.hp-=((player.spell*0.25)+(player.dmg*0.25)) if not isCritical(player.crit) else ((player.spell*0.5)+(player.dmg*0.5))*2
    player.hp+=player.spell*0.25+player.dmg*0.25
    LogNColor.Printer(str("Death Strike-Enemy HP:%d" %target.hp))
    LogNColor.Printer(str("Death Strike-Your HP:%d" %player.hp))

def runiccorruption(player,enemy):
    stgDebuff=int(round(player.stg/2))
    agiDebuff=int(round(player.agi/2))
    intDebuff=int(round(player.inl/2))
    enemy.hp-= stgBuff*10
    enemy.dmg-= stgBuff*3
    enemy.arm-= agiBuff*0.1
    enemy.crit-= agiBuff*3
    enemy.spell-= intBuff*5
    enemy.res-= intBuff*3
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff,agi=agiDebuff,inl=intDebuff,time=4))
    LogNColor.Printer(str("Runic Corruption-Enemy Strength:%d" %enemy.stg+stgDebuff))
    LogNColor.Printer(str("Runic Corruption-Enemy Agility:%d" %enemy.agi+agiBuff))
    LogNColor.Printer(str("Runic Corruption-Enemy Intellect:%d" %enemy.inl+intDebuff))

    
