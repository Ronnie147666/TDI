from StatsNDice import roll


class Recipe(object):
    def __init__(self,
                 opal=0, amber=0, emerald=0, diamond=0, zircon=0, crystal=0, turquoise=0, tourmaline=0,
                 citrine=0, aquamarine=0, amethyst=0, ruby=0, peridot=0, sapphire=0, spinel=0,
                 topaz=0, tanzanite=0, alexandrite=0, heliodor=0, taffelit=0, jade=0, coral=0, name=""):
        self.opal = opal
        self.amber = amber
        self.emerald = emerald
        self.diamond = diamond
        self.zircon = zircon
        self.crystal = crystal
        self.turquoise = turquoise
        self.tourmaline = tourmaline
        self.citrine = citrine
        self.aquamarine = aquamarine
        self.amethyst = amethyst
        self.ruby = ruby
        self.peridot = peridot
        self.sapphire = sapphire
        self.spinel = spinel
        self.topaz = topaz
        self.tanzanite = tanzanite
        self.alexandrite = alexandrite
        self.heliodor = heliodor
        self.taffelit = taffelit
        self.jade = jade
        self.coral = coral
        self.name = name


def recipes():
    return {
    'Rod of Lordly Might': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Rod of Lordly Might"),
    'Rod of Retribution': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Rod of Retribution"),
    'Staff of Fire': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Staff of Fire"),
    'Staff of Frost': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Staff of Frost"),
    'Staff of Power': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Staff of Power"),
    'Staff of Air': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Staff of Air"),
    'Bow of Slaying': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Bow of Slaying"),
    'Black Razor': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Black Razor"),
    'Azure Edge': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Azure Edge"),
    'Blood Axe': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Blood Axe"),
    'Bone Counter': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Bone Counter"),
    'Dragon Slayer': Recipe(opal=roll(1, 3), peridot=roll(1, 6), name="Dragon Slayer"),
}