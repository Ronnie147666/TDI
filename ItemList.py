import Item
import StatsNDice

items = {
    'Broadsword': Item.Item(strg=100,agi=150,intl=50,name="Broadsword"),
    'Cleaver': Item.Item(strg=300,agi=150,intl=20,name="Cleaver"),
    'Morellonomicon': Item.Item(strg=50,agi=200,intl=300,name="Morellonomicon")

    }


itemChance = StatsNDice.range_dict(
                     (range(0,10), items['Broadsword']),
                     (range(10,20), items['Morellonomicon']),                     
                     (range(20,40), items['Cleaver']))



