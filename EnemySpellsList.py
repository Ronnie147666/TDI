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

                                            #########################
                                                        ##BlackDragon##
                                            #########################

def dragonbreath(enemy,target):
    s=enemy.spell
    target.hp-=roll(s*2,s*4) if not isCritical(enemy.crit) else roll(s*4,s*8)
    LogNColor.Printer(str("Dragonbreath-Your HP:%d" %target.hp))

def tailwhip(enemy,target):
    target.hp-=enemy.dmg*3 if not isCritical(enemy.crit) else enemy.spell*8
    LogNColor.Printer(str("Tailwhip-Your HP:%d" %target.hp))

                                            #########################
                                                        ##DarkKnight##
                                            #########################
            
def darkbinding(enemy,player):
    inlDebuff=int(round(player.inl/2))
    enemy.spell-=inlBuff*5
    enemy.res-=inlBuff*3
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(inl=inlDebuff,time=4),)
    LogNColor.Printer(str("Dark Binding-Your Intellect:%d" %(player.inl+inlDebuff)))

def shadowstrike(enemy,target):
    target.hp-=(enemy.dmg*3)-target.arm*0.5 if not isCritical(enemy.crit) else (enemy.dmg*6)-target.arm*0.5
    LogNColor.Printer(str("Shadow Strike-Your HP:%d" %target.hp))

def darktouch(player,target):
    dmg=int(round(player.spell/2))
    target.hp-=dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg,time=5,name="Dark Touch"))
    LogNColor.Printer(str("Dark Touch-Enemy HP:%d" %target.hp))

                                            #########################
                                                        ##Lich##
                                            #########################

def icychains(enemy,player):
    agiDebuff=int(round(player.agi/2))
    enemy.arm-=agiBuff*3
    enemy.crit-=agiBuff*0.1    
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4),)
    LogNColor.Printer(str("Icy Chains-Your Agility:%d" %(player.agi+agiDebuff)))

def frostbolt(enemy,target):
    target.hp-=enemy.spell*5 if not isCritical(enemy.crit) else enemy.spell*10
    LogNColor.Printer(str("Deadlybolt-Your HP:%d" %target.hp))

def stealife(enemy,target):
    target.hp-=int(round(enemy.spell*1.5))
    enemy.hp+=enemy.spell*1.5
    LogNColor.Printer(str("Steal Life-Your HP:%d" %target.hp))
    LogNColor.Printer(str("Steal Life-Enemy HP:%d" %enemy.hp))

                                            #########################
                                                        ##Archmage##
                                            #########################

def arcanefocus(enemy,placeHolder):
    inlBuff=int(round(enemy.inl/2))
    enemy.spell+=inlBuff*5
    enemy.res+=inlBuff*3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff,time=4),)
    LogNColor.Printer(str("Arcane Focus-Your Intellect:%d" %(enemy.inl+inlBuff)))

def arcanemissiles(player,enemy):
    dmg=enemy.spell*3
    player.hp-=dmg if not isCritical(enemy.crit) else dmg*2
    LogNColor.Printer(str("Arcane Missiles-Your HP:%d" %target.hp))    

def arcaneleak(enemy,player):
    inlDebuff=int(round(player.inl/2))
    player.spell-=inlBuff*5
    player.res-=inlBuff*3
    player.debuffs.append(BuffNDebuff.BuffNDebuff(inl=inlDebuff,time=4),)
    LogNColor.Printer(str("Arcane Leak-Your Intellect:%d" %(player.inl+inlDebuff)))

                                            #########################
                                                        ##Demon##
                                            #########################

def soulsteal(enemy,target):
    target.hp-=int(round(enemy.spell))
    enemy.hp+=enemy.spell
    LogNColor.Printer(str("Soulsteal-Your HP:%d" %target.hp))
    LogNColor.Printer(str("Soulsteal-Enemy HP:%d" %enemy.hp))

def wrath(enemy,placeHolder):
    stgBuff=int(round(enemy.stg/2))
    agiBuff=int(round(enemy.agi/2))
    enemy.dmg+=stgBuff*10
    enemy.dmg+=stgBuff*5
    enemy.arm+= agiBuff*3
    enemy.crit+= agiBuff*0.1
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,agi=agiBuff,time=4))
    LogNColor.Printer(str("Wrath-Enemy Strength:%d" %(enemy.stg+stgBuff)))
    LogNColor.Printer(str("Wrath-Enemy Agility:%d" %(enemy.agi+agiBuff)))
    
                                            #########################
                                                ##FuriousSwordmaster##
                                            #########################

def furiousstrike(enemy,target):
    target.hp-=(enemy.dmg*3) if not isCritical(enemy.crit) else (enemy.dmg*6)
    LogNColor.Printer(str("Furious Strike-Your HP:%d" %target.hp))

def swiftspirit(enemy,placeHolder):
    agiBuff=int(round(enemy.agi/4))
    enemy.arm+= agiBuff*3
    enemy.crit+= agiBuff*0.1
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff,time=4))
    LogNColor.Printer(str("Swift Spirit-Enemy Strength:%d" %enemy.agi+agiBuff))    

def cuttingedge(player,target):
    dmg=int(round(player.dmg/2))-(target.arm*0.8)
    target.hp-=dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg,time=5,name="Poison"))
    LogNColor.Printer(str("Cutting Edge-Enemy HP:%d" %target.hp))

                                            #########################
                                                     ##DarkWizard##
                                            #########################

                                            #########################
                                               ##CursedNecromancer##
                                            #########################

                                            #########################
                                                    ##DrowRanger##
                                            #########################

                                             #########################
                                                    ##FireElemental##
                                            #########################
    
def firestrike(enemy,player):
    dmg=(enemy.dmg+enemy.spell)
    player.hp-=(dmg*2) if not isCritical(enemy.crit) else (dmg*4)
    LogNColor.Printer(str("Firestrike-Your HP:%d" %player.hp))

def fireinvocation(enemy,placeHolder):
    stgBuff=int(round(enemy.stg/2))
    enemy.hp+=stgBuff*10
    enemy.dmg+=stgBuff*5

    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4),)
    LogNColor.Printer(str("Fire Invocation-Enemy Strength:%d" %(enemy.stg+stgBuff)))

def firestorm(enemy,player):
    stgDebuff=int(round(player.stg/2))
    enemy.hp-=stgBuff*10
    enemy.dmg-=stgBuff*5
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4),)
    LogNColor.Printer(str("Fire Storm-Your Strength:%d" %(player.stg+stgDebuff)))

                                             #########################
                                                  ##WindElemental##
                                            #########################

def windstrike(enemy,player):
    dmg=(enemy.dmg+enemy.spell)
    player.hp-=(dmg*2) if not isCritical(enemy.crit) else (dmg*4)
    LogNColor.Printer(str("Windstrike-Your HP:%d" %player.hp))

def windinvocation(enemy,placeHolder):
    agiBuff=int(round(enemy.agi/2))
    enemy.arm+=agiBuff*3
    enemy.crit+=agiBuff*0.1    

    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4),)
    LogNColor.Printer(str("Wind Invocation-Enemy Agility:%d" %(enemy.stg+stgBuff)))

def windstorm(enemy,player):
    agiDebuff=int(round(player.agi/2))
    enemy.arm-=agiBuff*3
    enemy.crit-=agiBuff*0.1    
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4),)
    LogNColor.Printer(str("Wind Storm-Your Agility:%d" %(player.stg+agiDebuff)))    
 
                                            #########################
                                                 ##WaterElemental##
                                            #########################

def waterstrike(enemy,player):
    dmg=(enemy.dmg+enemy.spell)
    player.hp-=(dmg*2) if not isCritical(enemy.crit) else (dmg*4)
    LogNColor.Printer(str("Waterstrike-Your HP:%d" %player.hp))
    
def waterinvocation(enemy,placeHolder):
    inlBuff=int(round(enemy.inl/2))
    enemy.spell+=inlBuff*5
    enemy.res+=inlBuff*3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff,time=4),)
    LogNColor.Printer(str("Water Invocation-Enemy Intellect:%d" %(enemy.inl+inlBuff)))

def waterstorm(enemy,player):
    agiDebuff=int(round(player.agi/2))
    enemy.arm-=agiBuff*3
    enemy.crit-=agiBuff*0.1    
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4),)
    LogNColor.Printer(str("Water Storm-Your Intellect:%d" %(player.stg+agiDebuff)))

                                            #########################
                                                        ##Ghost##
                                            #########################
    
def nighthowl(placeHolder,target):
    stgDebuff=int(round(target.stg/3))
    intDebuff=int(round(target.inl/3))
    target.hp-= stgBuff*10
    target.dmg-= stgBuff*3
    target.spell-= intBuff*5
    target.res-= intBuff*3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff,inl=intDebuff,time=4))
    LogNColor.Printer(str("Runic Corruption-Enemy Strength:%d" %target.stg+stgDebuff))
    LogNColor.Printer(str("Runic Corruption-Enemy Intellect:%d" %target.inl+intDebuff))

                                             #########################
                                                 ##MercilessGladiator##
                                            #########################

def colossalstrike(enemy,target):
    target.hp-=(enemy.dmg*3) if not isCritical(enemy.crit) else (enemy.dmg*6)
    LogNColor.Printer(str("Titan Strike-Your HP:%d" %target.hp))
    
def colossalspirit(enemy,placeHolder):
    stgBuff=int(round(enemy.stg/4))
    enemy.hp+= stgBuff*10
    enemy.dmg+= stgBuff*5
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff,time=4))
    LogNColor.Printer(str("Colossal Spirit-Enemy Strength:%d" %enemy.stg+stgBuff)) 

def piercingshout(placeHolder,target):
    stgDebuff=-int(round(target.stg/4))
    target.hp+= stgDebuff*10
    target.dmg+= stgDebuff*5
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff,time=4))
    LogNColor.Printer(str("Piercing Shout-Your Strength:%d" %(target.stg+stgDebuff)))

   








    
