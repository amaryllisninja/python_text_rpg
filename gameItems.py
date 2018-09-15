# Game item dictionaries
itemNames = (
    'short sword',
    'dagger',
    'padded armor',
    'leather armor',
    'studded armor',
    'scalemail',
    'chainmail',
    'banded armor',
    'splintmail',
    'plate armor',
    'wizard robes',
    'pointed hat',
    'small shield',
    'spell book',
    'lock picking kit',
    'rope',
    'healing potion'
)

itemDescriptions = {
    'short sword':'''A sword about one third the length of your body. It feels comfortable
in your hand.''',
    'dagger':'''A sharp dagger that gleams in the light when you hold it up. It\'s not much,
but still looks dangerous.''',
    'padded armor':'''Light weight, fabric armour that fits you comfortably, although is
getting a little warm for your tastes.''',
    'leather armor':'''Light, sturdy armor. When you smell it, it reminds you of nature.''',
    'studded armor':'''Medium weight armor. It/'s made of stiff leather and brass studs.''',
    'scalemail':'''Heavy weight armor. Picking it up is difficult, but the overlapping steel
scales look like they could protect you from most anything.''',
    'chainmail':'''Heavy armor that jingles with every little movement. There's no way you
could sneak in this, but you're pretty sure it\'ll defend you.''',
    'banded armor':'''The definition of articulation. This heavy armor is the most moveable
of all the metal armors you\'ve encountered.''',
    'splintmail':'''Heavy armor that you\'re pretty sure took years to make.''',
    'plate armor':'''Heavy, study armor. You could face anything in this armor, even if it
does look battered.''',
    'wizard robes':'''A warm, woolen tunic that looks no more wizardly than hamster in a wheel.
It\'s seen a lot of use, however, so the wool is soft and comforting on your skin.''',
    'pointed hat':'''This hat looks majestic and magical. The fabric may be frayed, the copper
stars and moons tarnished, but it has an aura about it that almost glows.''',
    'small shield':'''A small shield with a metal handle on the back. It looks like it will
only give you a little protection.''',
    'medium shield':'''A medium-sized shield with an arm strap and a handle. This shield is
small enough to be travel-friendly, but large enough to offer you a lot of protection.''',
    'large shield':'''A great, heacy shield, made to stand up to horse and orc stampedes.
You're pretty sure this could even stop a dragon. That is, if you're strong enough to hold up
a whole dragon.''',
    'spell book':'''This is a dank and mouldy tome, handed down from generation to
generation. The pages look worn, the edges are frayed and torn. In some places, it even
looks like pages were torn out.''',
    'lock picking kit':'''While far from being the best crafted, these lock picks are sturdy
and useful. You can tell that many skillful hands have manipulated these tools.''',
    'rope':'''This rope is strong and thick. It would take a dragon biting through this
rope to cut it.''',
    'healing potion':'''A small glass vial, filled with a shimmering silver liquid. This
potion looks like it\'s brimming over with magic. There\'s not very much, but it looks like
enough to keep you going for a while.'''
}

itemType = {
    'short sword':'weapon',
    'dagger':'weapon',
    'padded armor':'armor',
    'leather armor':'armor',
    'studded armor':'armor',
    'scalemail':'armor',
    'chainmail':'armor',
    'banded armor':'armor',
    'splintmail':'armor',
    'plate armor':'armor',
    'wizard robes':'clothes',
    'pointed hat':'hat',
    'small shield':'shield',
    'medium shield':'shield',
    'large shield':'shield',
    'spell book':'book',
    'lock picking kit':'unlock',
    'rope':'climb',
    'healing potion':'potion'
}

wieldTypes = (      #Wieldable items
    'weapon',
    'shield',
    'wand'
)

wearTypes = (       #Wearable items
    'clothes',
    'hat',
    'armor'
)

useTypes = (        #Usable items
    'item',
    'tool',
    'potion'
    'book',
    'spell',
    'climb',
    'unlock'
)

weaponHitDice = {   #Number of dice and number of sides on dice
    'short sword':'1 6',
    'dagger':'1 4'
}

weaponStat = {
    'short sword':'strength',
    'dagger':'dexterity'
}

armorClass = {
    'padded armor':'1',
    'leather armor':'2',
    'studded armor':'3',
    'scalemail':'4',
    'chainmail':'5',
    'banded armor':'6',
    'splintmail':'7',
    'plate armor':'8',
    'small shield':'1',
    'medium shield':'2',
    'large shield':'3'
}

wearables = {
    'padded armor':'armor',
    'leather armor':'armor',
    'studded armor':'armor',
    'scalemail':'armor',
    'chainmail':'armor',
    'banded armor':'armor',
    'splintmail':'armor',
    'plate armor':'armor',
    'wizard robes':'clothes',
    'pointed hat':'hat',
    'small shield':'shield',
    'medium shield':'shield',
    'large shield':'shield'
}

itemPrices = {
    'short sword':10,
    'dagger':2,
    'padded armor':4,
    'leather armor':5,
    'studded armor':20,
    'scalemail':120,
    'chainmail':75,
    'banded armor':200,
    'splintmail':80,
    'plate armor':600,
    'wizard robes':1,
    'pointed hat':1,
    'small shield':3,
    'medium shield':7,
    'large shield':10,
    'spell book':50,
    'lock picking kit':30,
    'rope':1,
    'healing potion':20
}
