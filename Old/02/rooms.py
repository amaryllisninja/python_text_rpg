# Room dictionaries

roomNames = {
    0:'the Dojo',
    1:'a Hallway',
    2:'a Hallway',
    3:'a Hallway',
    4:'a Hallway',
    5:'a Hallway',
    6:'a Hallway',
    7:'a Hallway',
    8:'a Hallway',
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
To the North and South are hallways. To the East is the Dojo.''',
    4:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the East and West are hallways. To the South is the Dojo.''',
    5:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the South and West are hallways.''',
    6:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North and West are hallways.''',
    7:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the North and East are hallways.''',
    8:'''A quiet, dusty hallway. It does not look as if anyone has been here in a long time.
To the East and South are hallways.''',
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
