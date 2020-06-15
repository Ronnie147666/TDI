import random
import BuffNDebuff
import HotsNDots
import Spellcast
import StatsNDice
import LogNColor
from StatsNDice import isCritical


#########################
##Rogue##
#########################

def preparation(player, placeHolder):
    agiBuff = int(round(player.agi / 2))
    intBuff = int(round(player.inl / 2))
    player.arm += agiBuff * 3
    player.crit += agiBuff * 0.1
    player.spell += intBuff * 5
    player.res += intBuff * 3
    player.buffs.append(BuffNDebuff.BuffNDebuff(agi=agiBuff, inl=intBuff, time=4))
    LogNColor.Printer(str("Preparation-Your Agility:%d" % (player.agi + agiBuff)))
    LogNColor.Printer(str("Preparation-Your Intellect:%d" % (player.inl + intBuff)))


def poison(player, target):
    dmg = int(round(player.spell / 2)) - (target.res * 0.8)
    target.hp -= dmg
    target.dots.append(HotsNDots.HotNDot(hp=dmg, time=5, name="Poison"))
    LogNColor.Printer(str("Poison-Enemy HP:%d" % target.hp))


def backstab(player, target):
    dmg = (player.dmg * 3) - (target.arm * 0.8)
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    LogNColor.Printer(str("Backstab-Enemy HP:%d" % target.hp))

    #########################
    ##Warlock##
    #########################


def shadowbolt(player, target):
    Spellcast.castSpellTypeOne(player, 0, 2, target, 0, 0.5, target.shadowRes, 0)
    LogNColor.Printer(str("Shadowbolt-Enemy HP:%d" % target.hp))


def lifedrain(player, target):
    Spellcast.castSpellTypeOne(player, 0, 0.5, target, 0, 0.5, target.shadowRes, 0.5)
    dmg = int(round(player.spell / 2))
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    player.hp += player.spell
    LogNColor.Printer(str("Lifedrain-Enemy HP:%d" % target.hp))
    LogNColor.Printer(str("Lifedrain-Your HP:%d" % player.hp))


def immolate(player, target):
    dmg = int(round(player.spell / 3))
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    target.dots.append(HotsNDots.HotNDot(hp=dmg, time=4, name="Immolate"))
    LogNColor.Printer(str("Immolate-Enemy HP:%d" % target.hp))

    #########################
    ##Druid##
    #########################


def lunarstrike(player, target):
    dmg = ((player.spell * 0.5) + (player.dmg * 0.5)) - (target.arm * 0.75 + target.res * 0.75)
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    LogNColor.Printer(str("Lunar Strike-Enemy HP:%d" % target.hp))


def growth(player, placeHolder):
    hpHeal = int(round(player.spell / 4))
    if player.hp + hpHeal > StatsNDice.calculateHpWithBuffs(player):
        player.hp = StatsNDice.calculateHpWithBuffs(player)
    else:
        player.hp += hpHeal
    player.hots.append(HotsNDots.HotNDot(hp=hpHeal, time=4, name="Growth"))
    LogNColor.Printer(str("Growth-Your HP:%d" % player.hp))


def spirituality(player, placeHolder):
    stgBuff = int(round(player.stg / 2))
    agiBuff = int(round(player.agi / 2))
    intBuff = int(round(player.inl / 2))
    player.hp = stgBuff * 10
    player.dmg += stgBuff * 3
    player.arm += agiBuff * 0.1
    player.crit += agiBuff * 3
    player.spell += intBuff * 5
    player.res += intBuff * 3
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, agi=agiBuff, inl=intBuff, time=4))
    LogNColor.Printer(str("Spirituality-Your Strength:%d" % (player.stg + stgBuff)))
    LogNColor.Printer(str("Spirituality-Your Agility:%d" % (player.agi + agiBuff)))
    LogNColor.Printer(str("Spirituality-Your Intellect:%d" % (player.inl + intBuff)))

    #########################
    ##Warrior##
    #########################


def slam(player, target):
    dmg = player.dmg * 1.5 - target.arm * 0.7
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    LogNColor.Printer(str("Slam-Enemy HP: %d" % target.hp))


def shieldblock(player, placeHolder):
    stgBuff = int(round(player.stg / 4))
    player.hp += stgBuff * 10
    player.dmg += stgBuff * 5
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, time=4))
    LogNColor.Printer(str("Shieldblock-Your Strength:%d" % (player.stg + stgBuff)))


def taunt(placeHolder, target):
    stgDebuff = -int(round(target.stg / 4))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg -= stgDebuff * 5
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, time=4))
    LogNColor.Printer(str("Taunt-Enemy Strength:%d" % (target.stg + stgDebuff)))

    #########################
    ##Paladin##
    #########################


def crusaderstrike(player, target):
    Spellcast.castSpell(player, 2, 0.2,  # caster, damageModifier, spellModifier
                        target, 0.7, 0.9,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0,  # resistanceTyper, lifesteal
                        "Crusader Strike")

    # dmg = (player.dmg * 2) - (target.arm * 0.75)
    # target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    # LogNColor.Printer(str("Crusader Strike-Enemy HP:%d" % target.hp))


def blessingofkings(player, placeHolder):
    Spellcast.castBuff(player,
                       1, 0, 1,  # strength, agility, intellect
                       0.35, 4,  # modifier, duration
                       "Blessing Of Kings")
    # stgBuff = int(round(player.stg / 2))
    # inlBuff = int(round(player.inl / 2))
    # player.dmg += stgBuff * 10
    # player.dmg += stgBuff * 5
    # player.spell += inlBuff * 5
    # player.res += inlBuff * 3
    #
    # player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, inl=inlBuff, time=4), )
    # LogNColor.Printer(str("Blessing Of Kings-Your Strength:%d" % (player.stg + stgBuff)))
    # LogNColor.Printer(str("Blessing Of Kings-Your Intellect:%d" % (player.inl + inlBuff)))


def heal(player, placeHolder):
    Spellcast.castHeal(player, 0.75,
                       "Heal")

    #########################
    ##Mage##
    #########################


def arcanepower(player, placeHolder):
    Spellcast.castBuff(player,
                       0, 0, 1,  # strength, agility, intellect
                       0.5, 4,  # modifier, duration
                       "Arcane Power")

def arcanebolt(player, target):
    Spellcast.castSpell(player, 0, 3,  # caster, damageModifier, spellModifier
                        target, 0, 0.4,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0,  # resistanceTyper, lifesteal
                        "Arcanebolt")


def ignite(player, target):
    Spellcast.castDot(player, 0.4,  # caster, spellModifier
                      target, 0.75,  # target, targetResistanceModifier
                      target.fireRes, 4,  # targetResistance, duration
                      "Ignite")

    #########################
    ##Priest##
    #########################


def prayer(player, placeHolder):
    hpHeal = int(round(player.spell / 0.2))
    if player.hp + hpHeal > StatsNDice.calculateHpWithBuffs(player):
        player.hp = StatsNDice.calculateHpWithBuffs(player)
    else:
        player.hp += hpHeal
    player.hots.append(HotsNDots.HotNDot(hp=hpHeal, time=4, name="Prayer"))
    LogNColor.Printer(str("Prayer-Your HP:%d" % player.hp))


def silence(player, target):
    intDebuff = int(round(target.inl / 3))
    target.spell -= intDebuff * 5
    target.res -= intDebuff * 3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(inl=intDebuff, time=4))
    LogNColor.Printer(str("Silence-Enemy Intellect:%d" % (target.inl + intDebuff)))


def penance(player, target):
    dmg = player.spell * 2 - target.res * 0.65
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    LogNColor.Printer(str("Penance-Enemy HP:%d" % target.hp))

    #########################
    ##Ranger##
    #########################


def wildcall(player, placeHolder):
    stgBuff = int(round(player.stg / 2))
    agiBuff = int(round(player.agi / 2))
    player.hp += stgBuff * 10
    player.dmg += stgBuff * 5
    player.arm += agiBuff * 3
    player.crit += agiBuff * 0.1
    player.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, agi=agiBuff, time=4))
    LogNColor.Printer(str("Wild Call-Your Strength:%d" % (player.stg + stgBuff)))
    LogNColor.Printer(str("Wild Call-Your Agility:%d" % (player.agi + agiBuff)))


def deadlyshot(player, target):
    dmg = player.dmg * 2 - target.arm * 0.9
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    LogNColor.Printer(str("Deadly Shot-Enemy HP:%d" % target.hp))


def paralyzeshot(player, target):
    agiDebuff = int(round(target.agi / 3))
    target.arm -= agiDebuff * 0.1
    target.crit -= agiDebuff * 3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(agi=agiDebuff, time=4))
    LogNColor.Printer(str("Paralyze Shot-Enemy Agility:%d" % (target.agi + agiDebuff)))

    #########################
    ##DeathKnight##
    #########################


def deathgrip(player, target):
    dmg = ((player.spell * 0.5) + (player.dmg * 0.5)) - (target.arm * 0.5 + target.res * 0.5)
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    LogNColor.Printer(str("Death Grip-Enemy HP:%d" % target.hp))


def deathstrike(player, target):
    dmg = ((player.spell * 0.25) + (player.dmg * 0.25)) - (target.arm * 0.5 + target.res * 0.5)
    target.hp -= dmg if not isCritical(player.crit) else dmg * 2
    player.hp += player.spell * 0.25 + player.dmg * 0.25
    LogNColor.Printer(str("Death Strike-Enemy HP:%d" % target.hp))
    LogNColor.Printer(str("Death Strike-Your HP:%d" % player.hp))


def runiccorruption(placeHolder, target):
    stgDebuff = int(round(target.stg / 4))
    agiDebuff = int(round(target.agi / 4))
    intDebuff = int(round(target.inl / 4))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not newHp>target.hp else target.hp
    target.dmg -= stgDebuff * 3
    target.arm -= agiDebuff * 0.1
    target.crit -= agiDebuff * 3
    target.spell -= intDebuff * 5
    target.res -= intDebuff * 3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, agi=agiDebuff, inl=intDebuff, time=4))
    LogNColor.Printer(str("Runic Corruption-Enemy Strength:%d" % (target.stg + stgDebuff)))
    LogNColor.Printer(str("Runic Corruption-Enemy Agility:%d" % (target.agi + agiDebuff)))
    LogNColor.Printer(str("Runic Corruption-Enemy Intellect:%d" % (target.inl + intDebuff)))
