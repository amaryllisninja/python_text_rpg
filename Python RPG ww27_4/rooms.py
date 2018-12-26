# Room dictionaries

roomNames = {
    0:'the Dojo',
    1:'East Hallway',
    2:'South Hallway',
    3:'West Hallway',
    4:'North Hallway',
    5:'North-east Hallway',
    6:'South-west Hallway',
    7:'South-west Hallway',
    8:'Alchemy Shop',
}

roomDescriptions = {
    0:'''This room looks old, but well maintained. The wooden floors have seen many feet and
the sliding rice paper doors look like they have been repaired many times. But
while it looks as if it has been abused, it has an air of quiet dignity about it.
This is a respected and honorable room.
To the North, East, South, and West are hallways.''',
    1:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North and South are hallways. To the West is the Dojo.''',
    2:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North the is the Dojo. To the East and West are hallways.''',
    3:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North is a shop and to the South is a hallway. To the East is the Dojo.''',
    4:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the West is a shop and to the East is a hallway. To the South is the Dojo.''',
    5:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the South and West are hallways.''',
    6:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North and West are hallways.''',
    7:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North and East are hallways.''',
    8:'''A musty, dusty little shop with a grinning alchemist standing behind a counter. There
are all sorts of oddities and trinkets here. One wall of the shop is covered with glittering,
glistening, murky, slithery, or clear potions. Being here makes you uncomfortable.''',
}

directionsOpen = {
    0:'n e s w',
    1:'n x s w',
    2:'n e x w',
    3:'n e s x',
    4:'x e s w',
    5:'x x s w',
    6:'n x x w',
    7:'n e x x',
    8:'x e s x',
}

roomsConnectedTo = {
    0:'4 1 2 3',
    1:'5 x 6 0',
    2:'0 6 x 7',
    3:'8 0 7 x',
    4:'x 5 0 8',
    5:'x x 1 4',
    6:'1 x x 2',
    7:'3 2 x x',
    8:'x 4 3 x',
}

roomItems = (
    #0
    ['healing potion', 'short sword'],
    #1
    ['padded armor'],
    #2
    [''],
    #3
    [''],
    #4
    [''],
    #5
    [''],
    #6
    [''],
    #7
    [''],
    #8
    ['']
)

roomMonsters = (
    #0
    ['goblin', 'fairy'],
    #1
    [],
    #2
    [''],
    #3
    [''],
    #4
    [''],
    #5
    [''],
    #6
    ['skeleton'],
    #7
    [''],
    #8
    ['']
)

deadMonsters = (
    #0
    [''],
    #1
    [''],
    #2
    [''],
    #3
    ['skeleton'],
    #4
    [''],
    #5
    [''],
    #6
    [''],
    #7
    [''],
    #8
    ['']
)

roomNPCs = (
    #0
    [''],
    #1
    [''],
    #2
    [''],
    #3
    [''],
    #4
    ['guard'],
    #5
    [''],
    #6
    [''],
    #7
    [''],
    #8
    ['alchemist']
)
