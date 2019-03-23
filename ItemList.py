import Item
import StatsNDice
import randint from random

items = {
    'Titansword': Item.Item(strg=100,agi=150,name="Titansword"),
    'Dark Cleaver': Item.Item(strg=300,agi=150,name="Dark Cleaver"),
    'Dragonlance': Item.Item(strg=300,agi=150,name="Dragonlance"),
    'Grey Staff': Item.Item(strg=300,agi=150,name="Grey Staff"),
    'Cursed Dagger': Item.Item(strg=300,agi=150,name="Cursed Dagger"),
    'Twisted Hammer': Item.Item(strg=300,agi=150,name="Twisted Hammer"),
    'Rod Of Betrayal': Item.Item(strg=300,agi=150,name="Rod Of Betrayal"),
    'Arcanesword': Item.Item(strg=300,agi=150,name="Arcanesword"),
    'Rod Of Centuries': Item.Item(strg=300,agi=150,name="Rod Of Centuries"),
    'Forbidden Wand': Item.Item(strg=300,agi=150,name="Forbidden Wand"),
    'Raven Cloak': Item.Item(strg=300,agi=150,name="Raven Cloak"),
    'Morellonomicon': Item.Item(agi=200,intl=300,name="Morellonomicon")
    }


itemChance = StatsNDice.range_dict(
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



