import random
import BuffNDebuff
import HotsNDots
import StatsNDice
import LogNColor
import Spellcast
from StatsNDice import isCritical


#########################
##BlackDragon##
#########################

def dragonbreath(enemy, target):
    Spellcast.castSpell(target, 0, 0.75,  # caster, damageModifier, spellModifier
                        target, 0, 0.8,  # target, armorModifier, resistanceModifier
                        target.fireRes, 0,  # resistanceTyper, lifesteal
                        "Dragonbreath")

def tailwhip(enemy, target):
    Spellcast.castSpell(target, 0.9, 0.15,  # caster, damageModifier, spellModifier
                        target, 0.2, 0.9,  # target, armorModifier, resistanceModifier
                        target.natureRes, 0,  # resistanceTyper, lifesteal
                        "Tail Whip")

#########################
##DarkKnight##
#########################

def darkbinding(enemy, target):
    Spellcast.castDebuff(target,
                         0, 0, 0.5,  # strength, agility, intellect
                         4,  # duration
                         "Dark Binding")

def darkstrike(enemy, target):
    Spellcast.castSpell(target, 1.3, 0,  # caster, damageModifier, spellModifier
                        target, 0.5, 0,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0,  # resistanceTyper, lifesteal
                        "Dark Strike")

def darktouch(enemy, target):
    Spellcast.castDot(target, 0.5,  # caster, spellModifier
                      target, 0.75,  # target, targetResistanceModifier
                      target.shadowRes, 4,  # targetResistance, duration
                      "Dark Touch")

#########################
##Lich##
#########################

def icychains(enemy, target):
    Spellcast.castDebuff(target,
                         0, 0.5, 0,  # strength, agility, intellect
                         4,  # duration
                         "Icy Chains")

def frostbolt(enemy, target):
    Spellcast.castSpell(target, 0, 1.5,  # caster, damageModifier, spellModifier
                        target, 0, 0.75,  # target, armorModifier, resistanceModifier
                        target.iceRes, 0,  # resistanceTyper, lifesteal
                        "Frostbolt")

def stealife(enemy, target):
    Spellcast.castSpell(target, 0, 1,  # caster, damageModifier, spellModifier
                        target, 0, 0.65,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0.75,  # resistanceTyper, lifesteal
                        "Steal Life")

#########################
##Archmage##
#########################

def arcanefocus(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0, 0, 0.5,  # strength, agility, intellect
                       4,  # duration
                       "Arcane Focus")

def arcanemissiles(enemy, target):
    Spellcast.castSpell(target, 0, 1,  # caster, damageModifier, spellModifier
                        target, 0, 0.65,  # target, armorModifier, resistanceModifier
                        target.arcaneRes, 0.75,  # resistanceTyper, lifesteal
                        "Arcane Missiles")

def arcaneleak(enemy, target):
    Spellcast.castDebuff(target,
                         0, 0, 0.5,  # strength, agility, intellect
                         4,  # duration
                         "Arcane Leak")

#########################
##Demon##
#########################

def soulsteal(enemy, target):
    Spellcast.castSpell(target, 0, 1,  # caster, damageModifier, spellModifier
                        target, 0, 0.45,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0.85,  # resistanceTyper, lifesteal
                        "Soulsteal")

def wrath(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.5, 0.5, 0,  # strength, agility, intellect
                       4,  # duration
                       "Wrath")

#########################
##FuriousSwordmaster##
#########################

def furiousstrike(enemy, target):
    Spellcast.castSpell(target, 1.3, 0,  # caster, damageModifier, spellModifier
                        target, 0.4, 0,  # target, armorModifier, resistanceModifier
                        target.fireRes, 0,  # resistanceTyper, lifesteal
                        "Furious Strike")

def swiftspirit(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0, 0.25, 0,  # strength, agility, intellect
                       4,  # duration
                       "Swift Spirit")

def cuttingedge(enemy, target):
    Spellcast.castDot(target, 0.9,  # caster, spellModifier
                      target, 0.25,  # target, targetResistanceModifier
                      target.fireRes, 4,  # targetResistance, duration
                      "Cutting Edge")

#########################
##DarkWizard##
#########################

def darkarts(enemy, target):
    Spellcast.castSpell(target, 0, 1.3,  # caster, damageModifier, spellModifier
                        target, 0, 0.9,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0,  # resistanceTyper, lifesteal
                        "Dark Arts")

def darkfocus(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0, 0, 0.5,  # strength, agility, intellect
                       3,  # duration
                       "Dark Focus")

def darkcurse(enemy, target):
    Spellcast.castDebuff(target,
                         0.5, 0, 0,  # strength, agility, intellect
                         4,  # duration
                         "Dark Curse")

#########################
##Dreadlord##
#########################

def mindblast(enemy, target):
    Spellcast.castSpell(target, 0, 1.8,  # caster, damageModifier, spellModifier
                        target, 0, 0.85,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0,  # resistanceTyper, lifesteal
                        "Mind Blast")

def paralysis(enemy, target):
    Spellcast.castDebuff(target,
                         0.25, 0.5, 0,  # strength, agility, intellect
                         3,  # duration
                         "Paralysis")

#########################
##CursedNecromancer##
#########################

def deathfocus(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0, 0, 0.5,  # strength, agility, intellect
                       4,  # duration
                       "Death Focus")

def deathcall(enemy, target):
    Spellcast.castSpell(target, 0, 2.0,  # caster, damageModifier, spellModifier
                        target, 0, 0.75,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0.25,  # resistanceTyper, lifesteal
                        "Death Call")

#########################
##DrowRanger##
#########################


def precisionaura(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0, 0.5, 0.5,  # strength, agility, intellect
                       2,  # duration
                       "Precision Aura")

def frostshot(enemy, target):
    Spellcast.castSpell(target, 2.0, 0,  # caster, damageModifier, spellModifier
                        target, 0.85, 0,  # target, armorModifier, resistanceModifier
                        target.frostRes, 0.15,  # resistanceTyper, lifesteal
                        "Frost Shot")

def icyglance(enemy, target):
    Spellcast.castDebuff(target,
                         0, 0.3, 0,  # strength, agility, intellect
                         5,  # duration
                         "Icy Glance")

#########################
##ArcaneElemental##
#########################

def arcanestrike(enemy, target):
    Spellcast.castSpell(target, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.5,  # target, armorModifier, resistanceModifier
                        target.arcaneRes, 0.5,  # resistanceTyper, lifesteal
                        "Arcane Strike")

def arcaneinvocation(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.25, 0.25, 0.25,  # strength, agility, intellect
                       2,  # duration
                       "Arcane Invocation")

def arcanestorm(enemy, target):
    Spellcast.castDebuff(target,
                         0.25, 0.25, 0.25,  # strength, agility, intellect
                         2,  # duration
                         "Arcane Storm")

#########################
##FireElemental##
#########################

def firestrike(enemy, target):
    Spellcast.castSpell(target, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.5,  # target, armorModifier, resistanceModifier
                        target.fireRes, 0.5,  # resistanceTyper, lifesteal
                        "Fire Strike")

def fireinvocation(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.25, 0.25, 0.25,  # strength, agility, intellect
                       2,  # duration
                       "Fire Invocation")

def firestorm(enemy, target):
    Spellcast.castDebuff(target,
                         0.25, 0.25, 0.25,  # strength, agility, intellect
                         2,  # duration
                         "Fire Storm")

#########################
##FrostElemental##
#########################

def froststrike(enemy, target):
    Spellcast.castSpell(target, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.5,  # target, armorModifier, resistanceModifier
                        target.frostRes, 0.5,  # resistanceTyper, lifesteal
                        "Frost Strike")

def frostinvocation(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.25, 0.25, 0.25,  # strength, agility, intellect
                       2,  # duration
                       "Frost Invocation")

def froststorm(enemy, target):
    Spellcast.castDebuff(target,
                         0.25, 0.25, 0.25,  # strength, agility, intellect
                         2,  # duration
                         "Frost Storm")

#########################
##ShadowElemental##
#########################


def shadowstrike(enemy, target):
    Spellcast.castSpell(target, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.5,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0.5,  # resistanceTyper, lifesteal
                        "Shadow Strike")

def shadowinvocation(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.25, 0.25, 0.25,  # strength, agility, intellect
                       2,  # duration
                       "Shadow Invocation")

def shadowstorm(enemy, target):
    Spellcast.castDebuff(target,
                         0.25, 0.25, 0.25,  # strength, agility, intellect
                         2,  # duration
                         "Shadow Storm")

#########################
##NatureElemental##
#########################


def naturestrike(enemy, target):
    Spellcast.castSpell(target, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.5,  # target, armorModifier, resistanceModifier
                        target.natureRes, 0.5,  # resistanceTyper, lifesteal
                        "Nature Strike")

def natureinvocation(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.25, 0.25, 0.25,  # strength, agility, intellect
                       2,  # duration
                       "Nature Invocation")

def naturestorm(enemy, target):
    Spellcast.castDebuff(target,
                         0.25, 0.25, 0.25,  # strength, agility, intellect
                         2,  # duration
                         "Nature Storm")

#########################
##Ghost##
#########################

def nighthowl(placeHolder, target):
    Spellcast.castDebuff(target,
                         0.25, 0, 0.25,  # strength, agility, intellect
                         4,  # duration
                         "Night Howl")

#########################
##MercilessGladiator##
#########################

def colossalstrike(enemy, target):
    Spellcast.castSpell(target, 1.35, 0,  # caster, damageModifier, spellModifier
                        target, 0.4, 0,  # target, armorModifier, resistanceModifier
                        target.armor, 0,  # resistanceTyper, lifesteal
                        "Colossal Strike")

def colossalspirit(enemy, placeHolder):
    Spellcast.castBuff(enemy,
                       0.75, 0, 0,  # strength, agility, intellect
                       4,  # duration
                       "Colossal Spirit")

def piercingshout(placeHolder, target):
    Spellcast.castDebuff(target,
                         0.55, 0, 0,  # strength, agility, intellect
                         4,  # duration
                         "Piercing Shout")
