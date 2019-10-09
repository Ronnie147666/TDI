import random
import BuffNDebuff
import HotsNDots
import StatsNDice
import LogNColor
from StatsNDice import isCritical


#########################
##BlackDragon##
#########################

def dragonbreath(enemy, target):
    s = enemy.spell
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Dragonbreath-Your HP:%d" % target.hp))


def tailwhip(enemy, target):
    s = int(round(enemy.dmg * 1.3))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Tailwhip-Your HP:%d" % target.hp))

    #########################
    ##DarkKnight##
    #########################


def darkbinding(enemy, target):
    inlDebuff = int(round(target.inl / 2))
    target.spell -= inlDebuff * 1.5
    target.res -= inlDebuff * 1.3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(inl=inlDebuff, time=4))
    LogNColor.Printer(str("Dark Binding-Your Intellect:%d" % (target.inl + inlDebuff)))


def shadowstrike(enemy, target):
    s = int(round((enemy.dmg * 1.3) - target.arm * 0.5))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Shadow Strike-Your HP:%d" % target.hp))


def darktouch(enemy, target):
    dmg = int(round(enemy.spell / 2))
    target.hp -= dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg, time=5, name="Dark Touch"))
    LogNColor.Printer(str("Dark Touch-Enemy HP:%d" % target.hp))

    #########################
    ##Lich##
    #########################


def icychains(enemy, target):
    agiDebuff = int(round(target.agi / 2))
    target.arm -= agiDebuff * 1.3
    target.crit -= agiDebuff * 0.1
    target.debuffs.append(BuffNDebuff.BuffNDebuff(agi=agiDebuff, time=4))
    LogNColor.Printer(str("Icy Chains-Your Agility:%d" % (target.agi + agiDebuff)))


def frostbolt(enemy, target):
    s = int(round(enemy.spell * 1.5))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Deadlybolt-Your HP:%d" % target.hp))


def stealife(enemy, target):
    s = int(round(enemy.spell * 1.5))
    sd = StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    target.hp -= sd
    enemy.hp += sd
    LogNColor.Printer(str("Steal Life-Your HP:%d" % target.hp))
    LogNColor.Printer(str("Steal Life-Enemy HP:%d" % enemy.hp))

    #########################
    ##Archmage##
    #########################


def arcanefocus(enemy, placeHolder):
    inlBuff = int(round(enemy.inl / 2))
    enemy.spell += inlBuff * 1.5
    enemy.res += inlBuff * 1.3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff, time=4))
    LogNColor.Printer(str("Arcane Focus-Enemy Intellect:%d" % (enemy.inl + inlBuff)))


def arcanemissiles(enemy, target):
    s = int(round(enemy.spell * 1.3))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Arcane Missiles-Your HP:%d" % player.hp))


def arcaneleak(enemy, target):
    inlDebuff = int(round(target.inl / 2))
    target.spell -= inlBuff * 1.5
    target.res -= inlBuff * 1.3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(inl=inlDebuff, time=4))
    LogNColor.Printer(str("Arcane Leak-Your Intellect:%d" % (target.inl + inlDebuff)))

    #########################
    ##Demon##
    #########################


def soulsteal(enemy, target):
    dmg = int(round(enemy.spell))
    target.hp -= dmg
    enemy.hp += dmg
    LogNColor.Printer(str("Soulsteal-Your HP:%d" % target.hp))
    LogNColor.Printer(str("Soulsteal-Enemy HP:%d" % enemy.hp))


def wrath(enemy, placeHolder):
    stgBuff = int(round(enemy.stg / 2))
    agiBuff = int(round(enemy.agi / 2))
    enemy.dmg += stgBuff * 1.1
    enemy.dmg += stgBuff * 1.5
    enemy.arm += agiBuff * 1.3
    enemy.crit += agiBuff * 0.1
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, agi=agiBuff, time=4))
    LogNColor.Printer(str("Wrath-Enemy Strength:%d" % (enemy.stg + stgBuff)))
    LogNColor.Printer(str("Wrath-Enemy Agility:%d" % (enemy.agi + agiBuff)))

    #########################
    ##FuriousSwordmaster##
    #########################


def furiousstrike(enemy, target):
    s = int(round(enemy.dmg * 1.3))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Furious Strike-Your HP:%d" % target.hp))


def swiftspirit(enemy, placeHolder):
    agiBuff = int(round(enemy.agi / 4))
    enemy.arm += agiBuff * 1.3
    enemy.crit += agiBuff * 1.1
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff, time=4))
    LogNColor.Printer(str("Swift Spirit-Enemy Strength:%d" % (enemy.agi + agiBuff)))


def cuttingedge(enemy, target):
    dmg = int(round(enemy.dmg / 2)) - (target.arm * 0.8)
    target.hp -= dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg, time=5, name="Cutting Edge"))
    LogNColor.Printer(str("Cutting Edge-Enemy HP:%d" % target.hp))

    #########################
    ##DarkWizard##
    #########################


def darkarts(enemy, target):
    s = int(round(enemy.spell * 1.3))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Dark Arts-Your HP:%d" % target.hp))


def darkfocus(enemy, placeHolder):
    inlBuff = int(round(enemy.inl / 2))
    enemy.spell += inlBuff * 1.5
    enemy.res += inlBuff * 1.3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff, time=4))
    LogNColor.Printer(str("Dark Focus-Enemy Intellect:%d" % (enemy.inl + inlBuff)))


def darkcurse(enemy, target):
    stgDebuff = int(round(target.stg / 2))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg -= stgDebuff * 1.3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(inl=inlDebuff, time=4))
    LogNColor.Printer(str("Dark Curse-Your Intellect:%d" % (target.inl + inlDebuff)))

    #########################
    ##Dreadlord##
    #########################


def mindblast(enemy, target):
    s = int(round(enemy.spell * 1.8))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Mind Blast-Your HP:%d" % target.hp))


def paralysis(enemy, target):
    stgDebuff = -int(round(target.stg / 4))
    agiDebuff = int(round(target.agi / 2))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg -= stgDebuff * 5
    target.arm -= agiDebuff * 1.3
    target.crit -= agiDebuff * 0.1
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, agi=agiDebuff, time=4))
    LogNColor.Printer(str("Paralysis-Your Strength:%d" % (target.stg - stgDebuff)))
    LogNColor.Printer(str("Paralysis-Your Agility:%d" % (target.agi - agiDebuff)))

    #########################
    ##CursedNecromancer##
    #########################


def deathfocus(enemy, placeHolder):
    inlBuff = int(round(enemy.inl / 2))
    enemy.spell += inlBuff * 1.5
    enemy.res += inlBuff * 1.3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff, time=4))
    LogNColor.Printer(str("Death Focus-Enemy Intellect:%d" % (enemy.inl + inlBuff)))


def deathcall(enemy, target):
    s = int(round(enemy.spell * 2.0))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Death Call - Your HP:%d" % target.hp))

    #########################
    ##DrowRanger##
    #########################


def precisionaura(enemy, placeHolder):
    agiBuff = int(round(enemy.agi / 2))
    inlBuff = int(round(enemy.inl / 2))
    enemy.arm += agiBuff * 3
    enemy.crit += agiBuff * 0.1
    enemy.spell += inlBuff * 1.5
    enemy.res += inlBuff * 1.3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff, inl=inlBuff, time=4))
    LogNColor.Printer(str("Precision Aura-Enemy Agility:%d" % (enemy.agi + agiBuff)))
    LogNColor.Printer(str("Precision Aura-Enemy Strength:%d" % (enemy.inl + inlBuff)))


def frostshot(enemy, target):
    dmg = enemy.dmg * 2 - target.arm * 0.9
    target.hp -= dmg if not isCritical(enemy.crit) else dmg * 2
    LogNColor.Printer(str("Frost Shot-Your HP:%d" % target.hp))


def icyglance(enemy, target):
    agiDebuff = int(round(target.agi / 3))
    target.arm -= agiDebuff * 0.1
    target.crit -= agiDebuff * 3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(agi=agiDebuff, time=4))
    LogNColor.Printer(str("Icy Glance-Your Agility:%d" % (target.agi + agiDebuff)))

    #########################
    ##FireElemental##
    #########################


def firestrike(enemy, target):
    s = int(round((enemy.dmg + enemy.spell)))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Firestrike-Your HP:%d" % target.hp))


def fireinvocation(enemy, placeHolder):
    stgBuff = int(round(enemy.stg / 2))
    enemy.hp += stgBuff * 1.1
    enemy.dmg += stgBuff * 1.5
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, time=4))
    LogNColor.Printer(str("Fire Invocation-Enemy Strength:%d" % (enemy.stg + stgBuff)))


def firestorm(enemy, target):
    stgDebuff = int(round(target.stg / 2))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg -= stgDebuff * 1.5
    enemy.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, time=4))
    LogNColor.Printer(str("Fire Storm-Your Strength:%d" % (target.stg + stgDebuff)))

    #########################
    ##WindElemental##
    #########################


def windstrike(enemy, target):
    s = int(round((enemy.dmg + enemy.spell) * 0.75))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Windstrike-Your HP:%d" % target.hp))


def windinvocation(enemy, placeHolder):
    agiBuff = int(round(enemy.agi / 2))
    enemy.arm += agiBuff * 1.3
    enemy.crit += agiBuff * 1.1
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff, time=4), )
    LogNColor.Printer(str("Wind Invocation-Enemy Agility:%d" % (enemy.stg + stgBuff)))


def windstorm(enemy, target):
    agiDebuff = int(round(target.agi / 2))
    target.arm -= agiBuff * 1.3
    target.crit -= agiBuff * 1.1
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, time=4))
    LogNColor.Printer(str("Wind Storm-Your Agility:%d" % (target.stg + agiDebuff)))

    #########################
    ##WaterElemental##
    #########################


def waterstrike(enemy, target):
    s = int(round((enemy.dmg + enemy.spell) * 0.75))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Waterstrike-Your HP:%d" % target.hp))


def waterinvocation(enemy, placeHolder):
    inlBuff = int(round(enemy.inl / 2))
    enemy.spell += inlBuff * 1.5
    enemy.res += inlBuff * 1.3
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(inl=inlBuff, time=4))
    LogNColor.Printer(str("Water Invocation-Enemy Intellect:%d" % (enemy.inl + inlBuff)))


def waterstorm(enemy, target):
    agiDebuff = int(round(target.agi / 2))
    target.arm -= agiBuff * 1.3
    target.crit -= agiBuff * 1.1
    target.debuffs.append(BuffNDebuff.BuffNDebuff(agi=agiDebuff, time=4))
    LogNColor.Printer(str("Water Storm-Your Intellect:%d" % (target.stg + agiDebuff)))

    #########################
    ##Ghost##
    #########################


def nighthowl(placeHolder, target):
    stgDebuff = int(round(target.stg / 3))
    intDebuff = int(round(target.inl / 3))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg -= stgDebuff * 1.3
    target.spell -= intDebuff * 1.5
    target.res -= intDebuff * 1.3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, inl=intDebuff, time=4))
    LogNColor.Printer(str("Runic Corruption-Enemy Strength:%d" % (target.stg + stgDebuff)))
    LogNColor.Printer(str("Runic Corruption-Enemy Intellect:%d" % (target.inl + intDebuff)))

    #########################
    ##MercilessGladiator##
    #########################


def colossalstrike(enemy, target):
    s = int(round(enemy.dmg * 1.3))
    target.hp -= StatsNDice.roll(s * 2, s * 4) if not isCritical(enemy.crit) else StatsNDice.roll(s * 4, s * 8)
    LogNColor.Printer(str("Titan Strike-Your HP:%d" % target.hp))


def colossalspirit(enemy, placeHolder):
    stgBuff = int(round(enemy.stg / 4))
    enemy.hp += stgBuff * 1.1
    enemy.dmg += stgBuff * 1.5
    enemy.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, time=4))
    LogNColor.Printer(str("Colossal Spirit-Enemy Strength:%d" % (enemy.stg + stgBuff)))


def piercingshout(placeHolder, target):
    stgDebuff = -int(round(target.stg / 4))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg += stgDebuff * 1.5
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, time=4))
    LogNColor.Printer(str("Piercing Shout-Your Strength:%d" % (target.stg + stgDebuff)))
