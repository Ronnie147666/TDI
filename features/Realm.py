import random
import Enemy
from StatsNDice import range_dict

enemyList = range_dict(
    (range(0, 10), Enemy.BlackDragon.create),
    (range(10, 20), Enemy.DarkKnight.create),
    (range(20, 30), Enemy.Lich.create),
    (range(30, 40), Enemy.Archmage.create),
    (range(40, 50), Enemy.Demon.create),
    (range(50, 60), Enemy.FuriousSwordmaster.create),
    (range(60, 70), Enemy.DarkWizard.create),
    (range(70, 80), Enemy.DrowRanger.create),
    (range(80, 90), Enemy.Dreadlord.create),
    (range(90, 100), Enemy.CursedNecromancer.create),
    (range(100, 110), Enemy.Ghost.create),
    (range(110, 120), Enemy.MercilessGladiator.create),
    (range(120, 130), Enemy.FireElemental.create),
    (range(130, 140), Enemy.WindElemental.create),
    (range(140, 150), Enemy.WaterElemental.create)
)



class Realm:
    def __init__(self):
        pass


class Evermore(Realm):
    def getEnemy(self):
        return enemyList[random.randint(0, 150)]()
