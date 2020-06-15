import EnemySpellsList
from StatsNDice import roll, range_dict


class Enemy(object):
    def __init__(self):
        self.stg = 50
        self.agi = 50
        self.inl = 50
        self.bonusStg = 0
        self.bonusAgi = 0
        self.bonusInl = 0

        self.hp = 0
        self.dmg = 0
        self.arm = 0
        self.crit = 0
        self.spell = 0
        self.res = 0
        self.moveCount = 1

        self.fireRes = 0
        self.frostRes = 0
        self.shadowRes = 0
        self.natureRes = 0

        self.buffs = []
        self.debuffs = []
        self.dots = []
        self.hots = []
        self.curse = 0


###################################

class BlackDragon(Enemy):
    def __init__(self):
        super(BlackDragon, self).__init__()
        self.stg = roll(20, 25)
        self.agi = roll(10, 20)
        self.inl = roll(10, 20)

    @staticmethod
    def create():
        blackDragon = BlackDragon()
        return blackDragon

    movesList = {
        1: EnemySpellsList.dragonbreath,
        2: EnemySpellsList.tailwhip
    }

###################################


class DarkKnight(Enemy):
    def __init__(self):
        super(DarkKnight, self).__init__()
        self.stg = roll(15, 20)
        self.agi = roll(20, 25)
        self.inl = roll(10, 15)

    @staticmethod
    def create():
        darkKnight = DarkKnight()
        return darkKnight

    movesList = {
        1: EnemySpellsList.darkbinding,
        2: EnemySpellsList.shadowstrike,
        3: EnemySpellsList.darktouch
    }

###################################


class Lich(Enemy):
    def __init__(self):
        super(Lich, self).__init__()
        self.stg = roll(10, 15)
        self.agi = roll(15, 20)
        self.inl = roll(25, 30)

    @staticmethod
    def create():
        lich = Lich()
        return lich

    movesList = {
        1: EnemySpellsList.icychains,
        2: EnemySpellsList.frostbolt,
        3: EnemySpellsList.stealife
    }

###################################


class Archmage(Enemy):
    def __init__(self):
        super(Archmage, self).__init__()
        self.stg = roll(10, 15)
        self.agi = roll(20, 35)
        self.inl = roll(30, 35)

    @staticmethod
    def create():
        archmage = Archmage()
        return archmage

    movesList = {
        1: EnemySpellsList.arcanefocus,
        2: EnemySpellsList.arcanemissiles,
        3: EnemySpellsList.arcaneleak
    }


###################################

class Demon(Enemy):
    def __init__(self):
        super(Demon, self).__init__()
        self.stg = roll(20, 25)
        self.agi = roll(15, 25)
        self.inl = roll(15, 20)

    @staticmethod
    def create():
        demon = Demon()
        return demon

    movesList = {
        1: EnemySpellsList.soulsteal,
        2: EnemySpellsList.wrath
    }


###################################

class FuriousSwordmaster(Enemy):
    def __init__(self):
        super(FuriousSwordmaster, self).__init__()
        self.stg = roll(20, 25)
        self.agi = roll(25, 35)
        self.inl = roll(10, 35)

    @staticmethod
    def create():
        furiousSwordmaster = FuriousSwordmaster()
        return furiousSwordmaster

    movesList = {
        1: EnemySpellsList.furiousstrike,
        2: EnemySpellsList.swiftspirit,
        3: EnemySpellsList.cuttingedge
    }


###################################

class DarkWizard(Enemy):
    def __init__(self):
        super(DarkWizard, self).__init__()
        self.stg = roll(15, 20)
        self.agi = roll(15, 20)
        self.inl = roll(35, 40)

    @staticmethod
    def create():
        darkWizard = DarkWizard()
        return darkWizard

    movesList = {
        1: EnemySpellsList.darkarts,
        2: EnemySpellsList.darkfocus,
        3: EnemySpellsList.darkcurse
    }


###################################

class Dreadlord(Enemy):
    def __init__(self):
        super(Dreadlord, self).__init__()
        self.stg = roll(25, 30)
        self.agi = roll(15, 20)
        self.inl = roll(15, 20)

    @staticmethod
    def create():
        dreadlord = Dreadlord()
        return dreadlord

    movesList = {
        1: EnemySpellsList.mindblast,
        2: EnemySpellsList.paralysis
    }


###################################

class CursedNecromancer(Enemy):
    def __init__(self):
        super(CursedNecromancer, self).__init__()
        self.stg = roll(15, 25)
        self.agi = roll(10, 15)
        self.inl = roll(25, 35)

    @staticmethod
    def create():
        cursedNecromancer = CursedNecromancer()
        return cursedNecromancer

    movesList = {
        1: EnemySpellsList.deathfocus,
        2: EnemySpellsList.deathcall
    }


###################################

class DrowRanger(Enemy):
    def __init__(self):
        super(DrowRanger, self).__init__()
        self.stg = roll(15, 25)
        self.agi = roll(20, 35)
        self.inl = roll(15, 25)

    @staticmethod
    def create():
        drowRanger = DrowRanger()
        return drowRanger

    movesList = {
        1: EnemySpellsList.precisionaura,
        2: EnemySpellsList.frostshot,
        3: EnemySpellsList.icyglance
    }


###################################

class FireElemental(Enemy):
    def __init__(self):
        super(FireElemental, self).__init__()
        self.stg = roll(20, 30)
        self.agi = roll(10, 20)
        self.inl = roll(10, 20)

    @staticmethod
    def create():
        fireElemental = FireElemental()
        return fireElemental

    movesList = {
        1: EnemySpellsList.firestrike,
        2: EnemySpellsList.fireinvocation,
        3: EnemySpellsList.firestorm
    }

###################################


class WindElemental(Enemy):
    def __init__(self):
        super(WindElemental, self).__init__()
        self.stg = roll(10, 20)
        self.agi = roll(20, 30)
        self.inl = roll(10, 20)

    @staticmethod
    def create():
        windElemental = WindElemental()
        return windElemental

    movesList = {
        1: EnemySpellsList.windstrike,
        2: EnemySpellsList.windinvocation,
        3: EnemySpellsList.windstorm
    }

###################################


class WaterElemental(Enemy):
    def __init__(self):
        super(WaterElemental, self).__init__()
        self.stg = roll(10, 20)
        self.agi = roll(10, 20)
        self.inl = roll(20, 30)

    @staticmethod
    def create():
        waterElemental = WaterElemental()
        return waterElemental

    movesList = {
        1: EnemySpellsList.waterstrike,
        2: EnemySpellsList.waterinvocation,
        3: EnemySpellsList.waterstorm
    }

###################################


class Ghost(Enemy):
    def __init__(self):
        super(Ghost, self).__init__()
        self.stg = roll(10, 15)
        self.agi = roll(20, 30)
        self.inl = roll(20, 30)

    @staticmethod
    def create():
        ghost = Ghost()
        return ghost

    movesList = {
        1: EnemySpellsList.nighthowl
    }

###################################


class MercilessGladiator(Enemy):
    def __init__(self):
        super(MercilessGladiator, self).__init__()
        self.stg = roll(20, 35)
        self.agi = roll(20, 35)
        self.inl = roll(10, 15)

    @staticmethod
    def create():
        mercilessGladiator = MercilessGladiator()
        return mercilessGladiator

    movesList = {
        1: EnemySpellsList.colossalstrike,
        2: EnemySpellsList.colossalspirit,
        3: EnemySpellsList.piercingshout
    }

###################################


enemyList = range_dict(
    (range(0, 10), BlackDragon.create),
    (range(10, 20), DarkKnight.create),
    (range(20, 30), Lich.create),
    (range(30, 40), Archmage.create),
    (range(40, 50), Demon.create),
    (range(50, 60), FuriousSwordmaster.create),
    (range(60, 70), DarkWizard.create),
    (range(70, 80), DrowRanger.create),
    (range(80, 90), Dreadlord.create),
    (range(90, 100), CursedNecromancer.create),
    (range(100, 110), Ghost.create),
    (range(110, 120), MercilessGladiator.create),
    (range(120, 130), FireElemental.create),
    (range(130, 140), WindElemental.create),
    (range(140, 150), WaterElemental.create)
)
