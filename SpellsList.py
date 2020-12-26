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
    Spellcast.castBuff(player,
                       0, 0.5, 0.5,  # strength, agility, intellect
                       4,  # duration
                       "Preparation")

def poison(player, target):
    Spellcast.castDot(player, 0.5,  # caster, spellModifier
                      target, 0.8,  # target, targetResistanceModifier
                      target.natureRes, 5,  # targetResistance, duration
                      "Poison")

def backstab(player, target):
    Spellcast.castSpell(player, 3, 0,  # caster, damageModifier, spellModifier
                        target, 0.7, 0,  # target, armorModifier, resistanceModifier
                        0, 0.25,  # resistanceTyper, lifesteal
                        "Backstab")

    #########################
    ##Warlock##
    #########################


def shadowbolt(player, target):
    Spellcast.castSpell(player, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.5,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0,  # resistanceTyper, lifesteal
                        "Shadowbolt")

def lifedrain(player, target):
    Spellcast.castSpell(player, 0, 0.75,  # caster, damageModifier, spellModifier
                        target, 0, 0.75,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 1,  # resistanceTyper, lifesteal
                        "Lifedrain")

def immolate(player, target):
    Spellcast.castDot(player, 0.3,  # caster, spellModifier
                      target, 0.65,  # target, targetResistanceModifier
                      target.fireRes, 3,  # targetResistance, duration
                      "Immolate")

    #########################
    ##Druid##
    #########################


def lunarstrike(player, target):
    Spellcast.castSpell(player, 0.25, 0.5,  # caster, damageModifier, spellModifier
                        target, 0.9, 0.75,  # target, armorModifier, resistanceModifier
                        target.natureRes, 0,  # resistanceTyper, lifesteal
                        "Lunar Strike")

def growth(player, placeHolder):
    Spellcast.castHot(player, 0.25,  # caster, spellModifier
                      3, "Growth")  # duration

def spirituality(player, placeHolder):
    Spellcast.castBuff(player,
                       0.5, 0.5, 0.5,  # strength, agility, intellect
                       4,  # duration
                       "Shieldblock")

    #########################
    ##Warrior##
    #########################

def slam(player, target):
    Spellcast.castSpell(player, 1.5, 0,  # caster, damageModifier, spellModifier
                        target, 0.7, 0,  # target, armorModifier, resistanceModifier
                        0, 0,  # resistanceTyper, lifesteal
                        "Slam")

def shieldblock(player, placeHolder):
    Spellcast.castBuff(player,
                       0.25, 0, 0,  # strength, agility, intellect
                       4,  # duration
                       "Shieldblock")

def taunt(placeHolder, target):
    Spellcast.castDebuff(target,
                       0.25, 0, 0,  # strength, agility, intellect
                       4,  # duration
                       "Taunt")

    #########################
    ##Paladin##
    #########################

def crusaderstrike(player, target):
    Spellcast.castSpell(player, 2, 0.2,  # caster, damageModifier, spellModifier
                        target, 0.7, 0.9,  # target, armorModifier, resistanceModifier
                        target.fireRes, 0,  # resistanceTyper, lifesteal
                        "Crusader Strike")

def blessingofkings(player, placeHolder):
    Spellcast.castBuff(player,
                       0.35, 0, 0.25,  # strength, agility, intellect
                       4,  # duration
                       "Blessing Of Kings")

def heal(player, placeHolder):
    Spellcast.castHeal(player, 0.75,
                       "Heal")

    #########################
    ##Mage##
    #########################


def arcanepower(player, placeHolder):
    Spellcast.castBuff(player,
                       0, 0, 0.85,  # strength, agility, intellect
                       4,  # duration
                       "Arcane Power")

def arcanebolt(player, target):
    Spellcast.castSpell(player, 0, 3,  # caster, damageModifier, spellModifier
                        target, 0, 0.4,  # target, armorModifier, resistanceModifier
                        target.arcaneRes, 0,  # resistanceTyper, lifesteal
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
    Spellcast.castHot(player, 0.2,
                      5, "Prayer")

def silence(player, target):
    Spellcast.castDebuff(target,
                       0, 0, 0.3,  # strength, agility, intellect
                       4,  # duration
                       "Silence")

def penance(player, target):
    Spellcast.castSpell(player, 0, 2,  # caster, damageModifier, spellModifier
                        target, 0, 0.65,  # target, armorModifier, resistanceModifier
                        target.fireRes, 0,  # resistanceTyper, lifesteal
                        "Penance")

    #########################
    ##Ranger##
    #########################


def wildcall(player, placeHolder):
    Spellcast.castBuff(player,
                       0.45, 0.45, 0,  # strength, agility, intellect
                       4,  # duration
                       "Wild Call")

def deadlyshot(player, target):
    Spellcast.castSpell(player, 2, 0,  # caster, damageModifier, spellModifier
                        target, 0.9, 0,  # target, armorModifier, resistanceModifier
                        target.natureRes, 0,  # resistanceTyper, lifesteal
                        "Deadly Shot")

def paralyzeshot(player, target):
    Spellcast.castDebuff(target,
                       0, 0.3, 0,  # strength, agility, intellect
                       4,  # duration
                       "Paralyze Shot")

    #########################
    ##DeathKnight##
    #########################


def deathgrip(player, target):
    Spellcast.castSpell(player, 1.25, 0.75,  # caster, damageModifier, spellModifier
                        target, 0.6, 0.8,  # target, armorModifier, resistanceModifier
                        target.frostRes, 0,  # resistanceTyper, lifesteal
                        "Death Grip")

def deathstrike(player, target):
    Spellcast.castSpell(player, 0.25, 0.25,  # caster, damageModifier, spellModifier
                        target, 0.2, 45,  # target, armorModifier, resistanceModifier
                        target.shadowRes, 0.9,  # resistanceTyper, lifesteal
                        "Death Grip")

def runiccorruption(placeHolder, target):
    Spellcast.castDebuff(target,
                       0.25, 0.25, 0.25,  # strength, agility, intellect
                       3,  # duration
                       "Runic Corruption")
