import Item
from random import randint
from StatsNDice import roll, range_dict

def items():
    return {
    'Titansword': Item.Item(stg=roll(5, 25), agi=roll(5, 25), fireRes=roll(5, 25), frostRes=roll(5, 25) ,name="Titansword"),
    'Dark Cleaver': Item.Item(stg=roll(5, 10), agi=roll(5, 15), shadowRes=roll(5, 25), natureRes=roll(5, 25) ,name="Dark Cleaver"),
    'Dragonlance': Item.Item(stg=roll(5, 15), agi=roll(5, 10), fireRes=roll(5, 25), natureRes=roll(5, 25) ,name="Dragonlance"),
    'Grey Staff': Item.Item(agi=roll(5, 10), inl=roll(5, 10), fireRes=roll(5, 25), shadowRes=roll(5, 25) ,name="Grey Staff"),
    'Cursed Dagger': Item.Item(stg=roll(5, 10), agi=roll(5, 25), shadowRes=roll(5, 25), frostRes=roll(5, 25) ,name="Cursed Dagger"),
    'Twisted Hammer': Item.Item(stg=roll(5, 20), agi=roll(5, 10), natureRes=roll(5, 25), frostRes=roll(5, 25) ,name="Twisted Hammer"),
    'Rod Of Betrayal': Item.Item(agi=roll(5, 15), inl=roll(5, 15), fireRes=roll(5, 25), frostRes=roll(5, 25) ,name="Rod Of Betrayal"),
    'Arcanesword': Item.Item(stg=roll(5, 15), inl=roll(5, 15), natureRes=roll(5, 25), frostRes=roll(5, 25) ,name="Arcanesword"),
    'Rod Of Centuries': Item.Item(stg=roll(5, 20), agi=roll(5, 20), inl=roll(5, 20), shadowRes=roll(5, 25), frostRes=roll(5, 25) ,name="Rod Of Centuries"),
    'Forbidden Wand': Item.Item(agi=roll(5, 10), inl=roll(5, 20), natureRes=roll(5, 25), frostRes=roll(5, 25) ,name="Forbidden Wand"),
    'Raven Cloak': Item.Item(agi=roll(5, 15), inl=roll(5, 10), fireRes=roll(5, 25), shadowRes=roll(5, 25) ,name="Raven Cloak"),
    'Morellonomicon': Item.Item(agi=roll(5, 10), inl=roll(10, 15), fireRes=roll(5, 25), frostRes=roll(5, 25) ,name="Morellonomicon")
}


def itemChance():
    items_instance = items()
    return range_dict(
    (range(0, 10), items_instance['Titansword']),
    (range(10, 20), items_instance['Dark Cleaver']),
    (range(20, 30), items_instance['Dragonlance']),
    (range(30, 40), items_instance['Grey Staff']),
    (range(40, 50), items_instance['Cursed Dagger']),
    (range(50, 60), items_instance['Twisted Hammer']),
    (range(60, 70), items_instance['Rod Of Betrayal']),
    (range(70, 80), items_instance['Arcanesword']),
    (range(80, 90), items_instance['Rod Of Centuries']),
    (range(90, 100), items_instance['Morellonomicon']),
    (range(100, 110), items_instance['Raven Cloak']),
    (range(110, 121), items_instance['Forbidden Wand']))
