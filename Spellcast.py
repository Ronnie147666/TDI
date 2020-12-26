import BuffNDebuff
import HotsNDots
import LogNColor
import StatsNDice


def castSpell(caster, casterDamageModifier, casterSpellModifier,
              target, targetArmorModifier, targetResistance, targetResistanceModifier,
              lifestealModifier, spellName):
    pDmg = caster.dmg * casterDamageModifier * (1 - (target.arm * targetArmorModifier)/100)
    mDmg = caster.spell * casterSpellModifier * (1 - (targetResistance * targetResistanceModifier) / 100)
    dmg = round(pDmg + mDmg)
    totalDmg = dmg if not StatsNDice.isCritical(caster.crit) else int(round((dmg * 1.75)))
    target.hp -= totalDmg
    caster.hp = caster.hp + (totalDmg * lifestealModifier) \
        if (caster.hp + (totalDmg * lifestealModifier)) <= StatsNDice.calculateHpWithBuffs(caster) \
        else StatsNDice.calculateHpWithBuffs(caster)
    LogNColor.Printer(str(LogNColor.splitWords(type(caster).__name__)) +
                      " casts " + spellName + " for " + str(totalDmg) + "!")


def castHeal(caster, modifier, spellName):
    healAmount = caster.spell * modifier if not StatsNDice.isCritical(caster.crit) else (caster.spell * modifier) * 2
    caster.hp = caster.hp + healAmount if caster.hp + healAmount <= StatsNDice.calculateHpWithBuffs(
        caster) else StatsNDice.calculateHpWithBuffs(caster)
    LogNColor.Printer(str(LogNColor.splitWords(type(caster).__name__)) +
                      LogNColor.Printer(" casts" + spellName) + " for " + str(healAmount) + " heal!")


def castBuff(target, sBuff, aBuff, iBuff, duration, spellName):
    stgBuff = int(round(target.stg * sBuff))
    agiBuff = int(round(target.agi * aBuff))
    inlBuff = int(round(target.inl * iBuff))
    target.hp += stgBuff * 10
    target.dmg += stgBuff * 5
    target.spell += inlBuff * 5
    target.crit += agiBuff * 0.1
    target.arm = round(StatsNDice.setArmor(target.agi + agiBuff), 1)
    target.arcaneRes = round(StatsNDice.setResistance(target.inl + inlBuff), 1)
    target.fireRes = round(StatsNDice.setResistance(target.inl + inlBuff), 1)
    target.frostRes = round(StatsNDice.setResistance(target.inl + inlBuff), 1)
    target.shadowRes = round(StatsNDice.setResistance(target.inl + inlBuff), 1)
    target.natureRes = round(StatsNDice.setResistance(target.inl + inlBuff), 1)
    target.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, agi=agiBuff, inl=inlBuff, time=duration))
    LogNColor.Printer(str(LogNColor.splitWords(type(target).__name__)) +
                      " casts " + spellName + " for" +
                      str(" %d Strength" % stgBuff) +
                      str(" %d Agility" % agiBuff) +
                      str(" %d Intellect" % inlBuff))


def castDebuff(target, sDebuff, aDebuff, iDebuff, duration, spellName):
    stgDebuff = int(round(target.stg * sDebuff))
    agiDebuff = int(round(target.agi * aDebuff))
    inlDebuff = int(round(target.inl * iDebuff))
    newHp = (target.stg - stgDebuff) * 10
    target.hp = newHp if not (newHp > target.hp and sDebuff == 0) else target.hp
    target.dmg -= stgDebuff * 5
    target.spell -= inlDebuff * 5
    target.crit -= agiDebuff * 0.1
    target.arm = round(StatsNDice.setArmor(target.agi - agiDebuff), 1)
    target.arcaneRes = round(StatsNDice.setResistance(target.inl - inlDebuff), 1)
    target.fireRes = round(StatsNDice.setResistance(target.inl - inlDebuff), 1)
    target.frostRes = round(StatsNDice.setResistance(target.inl - inlDebuff), 1)
    target.shadowRes = round(StatsNDice.setResistance(target.inl - inlDebuff), 1)
    target.natureRes = round(StatsNDice.setResistance(target.inl - inlDebuff), 1)
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, agi=agiDebuff, inl=inlDebuff, time=duration))
    LogNColor.Printer(str(LogNColor.splitWords(type(target).__name__)) +
                      " casts " + spellName + " for" +
                      str(" %d Strength" % stgDebuff) +
                      str(" %d Agility" % agiDebuff) +
                      str(" %d Intellect" % inlDebuff))


def castHot(caster, modifier, duration, spellName):
    h = int(round(caster.spell * modifier))
    hot = h if not StatsNDice.isCritical(caster.crit) else h * 2
    maxHp = StatsNDice.calculateHpWithBuffs(caster)
    if caster.hp + hot > maxHp:
        caster.hp = maxHp
    else:
        caster.hp += hot
    caster.hots.append(HotsNDots.HotNDot(hp=hot, time=duration, name=spellName))


def castDot(caster, casterSpellModifier, target, targetResistanceModifier, targetResistance, duration, spellName):
    d = int(round(caster.spell * casterSpellModifier * (1 - (targetResistance * targetResistanceModifier)/100)))
    dot = d if not StatsNDice.isCritical(caster.crit) else d * 2
    target.hp -= dot if not StatsNDice.isCritical(caster.crit) else dot * 2
    caster.dots.append(HotsNDots.HotNDot(hp=dot, time=duration, name=spellName))
    LogNColor.Printer(str(LogNColor.splitWords(type(caster).__name__)) +
                      LogNColor.Printer(" casts" + spellName) + "for a DoT of" + str(dot) + "damage for" +
                      str(duration) + "turns!")

