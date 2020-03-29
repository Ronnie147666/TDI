import BuffNDebuff
import HotsNDots
import StatsNDice


def castSpell(caster, target, targetElementResistance, lifestealModifier):
    dmg = (caster.casterDamage * caster.casterDamageModifier - (target.targetArmor * target.targetArmorModifier) - targetElementResistance)
    spell = (caster.casterSpell * caster.casterSpellModifier - (target.targetResilience * target.targetResilienceModifier) - targetElementResistance)
    totalDmg = dmg + spell if not StatsNDice.isCritical(caster.crit) else (dmg + spell) * 2
    target.hp -= totalDmg
    caster.hp = caster.hp + (totalDmg * lifestealModifier) if (caster.hp + (totalDmg * lifestealModifier)) <= StatsNDice.calculateHpWBuffs(caster) else StatsNDice.calculateHpWBuffs(caster)

def castHeal(caster, modifier):
    healAmount = caster.spell * modifier if not StatsNDice.isCritical(caster.crit) else (caster.spell * modifier) * 2
    caster.hp = caster.hp + healAmount if caster.hp + healAmount <= StatsNDice.calculateHpWBuffs(caster) else StatsNDice.calculateHpWBuffs(caster)


def castBuff(target, sBuff, aBuff, iBuff, modifier, duration):  #sBuff, aBuff, iBuff -> 0 if not included
    stgBuff = sBuff * int(round(target.stg / modifier))
    agiBuff = aBuff * int(round(target.agi / modifier))
    inlBuff = iBuff * int(round(target.inl / modifier))
    target.hp += stgBuff * 10
    target.dmg += stgBuff * 5
    target.arm += agiBuff * 3
    target.crit += agiBuff * 0.1
    target.spell += inlBuff * 5
    target.res += inlBuff * 3
    target.buffs.append(BuffNDebuff.BuffNDebuff(stg=stgBuff, agi=agiBuff, inl=inlBuff, time=duration))


def castDebuff(target, sDebuff, aDebuff, iDebuff, modifier, duration):  #sDebuff, aDebuff, iDebuff -> 0 if not included
    stgDebuff = sDebuff * int(round(target.stg / modifier))
    agiDebuff = aDebuff * int(round(target.agi / modifier))
    inlDebuff = iDebuff * int(round(target.inl / modifier))
    newHp = (target.stg - stgDebuff) * 10
    target.hp =  newHp if not (newHp>target.hp and sDebuff == 0) else target.hp
    target.dmg += stgDebuff * 5
    target.arm += agiDebuff * 3
    target.crit += agiDebuff * 0.1
    target.spell += inlDebuff * 5
    target.res += inlDebuff * 3
    target.debuffs.append(BuffNDebuff.BuffNDebuff(stg=stgDebuff, agi=agiDebuff, inl=inlDebuff, time=duration))


def castHot(caster, modifier, duration, title):
    h = caster.spell * modifier
    hot = h if not StatsNDice.isCritical(caster.crit) else h * 2
    if caster.hp + hot > StatsNDice.calculateHpWBuffs(caster):
        caster.hp = StatsNDice.calculateHpWBuffs(caster)
    else:
        caster.hp += hot
    caster.hots.append(HotsNDots.HotNDot(hp=hot, time=duration, name=title))


def castDot(caster, target, modifier, duration, title):
    d = int(round(caster.spell * modifier))
    dot = d if not StatsNDice.isCritical(caster.crit) else d * 2
    target.hp -= dot if not StatsNDice.isCritical(caster.crit) else dot * 2
    caster.dots.append(HotsNDots.HotNDot(hp=dot, time=duration, name=title))



