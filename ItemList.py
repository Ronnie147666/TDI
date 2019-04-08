import Item
from random import randint
from StatsNDice import roll,range_dict

items = {
    'Titansword': Item.Item(stg=roll(5,25),agi=roll(5,25),name="Titansword"),
    'Dark Cleaver': Item.Item(stg=roll(5,10),agi=roll(5,15),name="Dark Cleaver"),
    'Dragonlance': Item.Item(stg=roll(5,15),agi=roll(5,10),name="Dragonlance"),
    'Grey Staff': Item.Item(agi=roll(5,10),inl=roll(5,10),name="Grey Staff"),
    'Cursed Dagger': Item.Item(stg=roll(5,10),agi=roll(5,25),name="Cursed Dagger"),
    'Twisted Hammer': Item.Item(stg=roll(5,20),agi=roll(5,10),name="Twisted Hammer"),
    'Rod Of Betrayal': Item.Item(agi=roll(5,15),inl=roll(5,15),name="Rod Of Betrayal"),
    'Arcanesword': Item.Item(stg=roll(5,15),inl=roll(5,15),name="Arcanesword"),
    'Rod Of Centuries': Item.Item(stg=roll(5,20),agi=roll(5,20),inl=roll(5,20),name="Rod Of Centuries"),
    'Forbidden Wand': Item.Item(agi=roll(5,10),inl=roll(5,20),name="Forbidden Wand"),
    'Raven Cloak': Item.Item(agi=roll(5,15),inl=roll(5,10),name="Raven Cloak"),
    'Morellonomicon': Item.Item(agi=roll(5,10),inl=roll(10,15),name="Morellonomicon")
    }


itemChance = range_dict(
                     (range(0,10), items['Titansword']),
                     (range(10,20), items['Dark Cleaver']),
                     (range(20,30), items['Dragonlance']),
                     (range(30,40), items['Grey Staff']),
                     (range(40,50), items['Cursed Dagger']),
                     (range(50,60), items['Twisted Hammer']),
                     (range(60,70), items['Rod Of Betrayal']),
                     (range(70,80), items['Arcanesword']),
                     (range(80,90), items['Rod Of Centuries']),
                     (range(90,100), items['Morellonomicon']),
                     (range(100,110), items['Raven Cloak']),
                     (range(120,130), items['Forbidden Wand']))



