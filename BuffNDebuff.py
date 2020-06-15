import StatsNDice


class BuffNDebuff(object):
    def __init__(self, stg=0, att=0, agi=0, inl=0, time=0, calculated=0):
        self.stg = stg
        self.agi = agi
        self.inl = inl
        self.time = time


def getStrBuffNDebuff(character):
    s = 0
    for buff in character.buffs:
        s += buff.stg
    for debuff in character.debuffs:
        s += debuff.stg
    return s


def getAgiBuffNDebuff(character):
    s = 0
    for buff in character.buffs:
        s += buff.agi
    for debuff in character.debuffs:
        s += debuff.agi
    return s


def getIntBuffNDebuff(character):
    s = 0
    for buff in character.buffs:
        s += buff.inl
    for debuff in character.debuffs:
        s += debuff.inl
    return s


def clearBuffsNDebuffs(character):
    stgBuffs = 0
    for b in character.buffs:
        if b.time == 0:
            stgBuffs += b.stg
    stgDebuffs = 0
    for b in character.debuffs:
        if b.time == 0:
            stgDebuffs += b.stg
    character.buffs = [buff for buff in character.buffs if buff.time > 0]
    character.debuffs = [debuff for debuff in character.debuffs if debuff.time > 0]
    if stgBuffs > 0:
        if character.hp > StatsNDice.calculateHpWithBuffs(character):
            character.hp = StatsNDice.calculateHpWithBuffs(character)
    if stgDebuffs > 0:
        character.hp += stgDebuffs * 10


def reduceBuffsNDebuffs(character):
    for buff in character.buffs:
        buff.time -= 1
    for debuff in character.debuffs:
        debuff.time -= 1
