itemArt = {
    'short sword': [ 
'        ▄▄',
'       (▓█)',
'        │║',
'        │║',
'    ╬┬┬┬╣╠┬╦╦╬',
'    ╬╩╩┼╩╩┼╩╩╬',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       │▒░╣',
'       \▒░/',
'        \/'
        
    ],

    'dagger': [
'        (o)    ',
'       («0»)   ',
'        ├x╣    ',
'        ├x╣    ',
'    /═══┼X╬═══\ ',
'    \╩╩╩┼═┼╩╩╩/ ',
'        ╠░║    ',
'        ╠░║    ',
'        ╠░║    ',
'        ╠░║    ',
'        ╠░║    ',
'        ╠░║    ',  
'        ╠░║    ',
'        \░/    ',
'         V     '
  
    ],

    'padded armor': ['''

            _______      _______
           /X X X X\____/X X X X\
          /X X X X X  X  X X X XX\
         /                        \
        /                          \
       /      ┼               ┼     \
      /       └             /        \
     |         \             \        \
      \          \            \        \
        \          ┐           \        \
          \        /           │\        \
            \     /            │ \        \
             │\_/              │  \        \
             │                 │   \_______/
             │                 │
             │                 │
             └─────────────────┘
    '''], 

    'small shield': [
'          ┼┼┼┼┼╬╬╬╬╬╬╬',
'         ┼OOOOOOØØØØØØ╬',
'        ┼O░░░▒░░▒░▒▒▓▓Ø╬',
'       ┼O░░░░▒┌──┐░░▒▓▒Ø╬',
'      ┼O░░▒┌──┤▒▓├────┐▒Ø╬',
'     ┼O░░┌─┘┌─┤░▒├───┐│▓▒Ø╬',
'    ┼O░░▒│  │░│░▓│▒░▒└┘▒▓▓Ø╬',
'     ┼O░┌┘ ┌┘▒│░▒│░▒▓▓▒▓▓Ø╬',
'      ┼O│  └──┴──┴──┐▒▓▓Ø╬,',
'       ┼└─────┬──┬─┐│▓░Ø╬',
'        ┼O░▒┌─┤▒▓├─┘│▒Ø╬',
'         ┼O░│ ┴─┐├──┘Ø╬',
'          ┼O└─┬┐││▓▓Ø╬',
'           ┼O▒└┤├┘▒Ø╬',
'            ┼O░└┘▓Ø╬',
'             ┼O░▒Ø╬',
'              ┼OØ╬',
'               ┼╬'
    ],

    'healing potion': [
'              O       ',
'          o           ',
'                O     ',
'          ________    ',
'         (     o  )   ',
'          \      /    ',
'          │  O   │    ',
'          │      │    ',
'         /        \   ',
'       ( o    O     ) ',
'     (░ █▓░░ ░  o░▓  ░)',
'    (▓▓██▒▒▒░▒▒▒░▒░░▓░░)',
'    (▓█▓▓▓██▓▓▒▒░▓░▒░░▒)',
'    (▓▓██▓▓▓▒▒▓▓▓▒░░░▒▒)',
'     \▓▓██▓▓▓█▒▓▒░░░░▒/',
'      \▓▓██▓▓██▓▒░░▒▒/',
'       \▀▀▀▀▀▀▀▀▀▀▀▀/'
    ],

    
          
}

itemList = []
for item in itemArt.keys():
    itemList.append(item)
    
while True:
    lookAt = input("Do you want to look at the " + ' or '.join(itemList) + "? ")
    if lookAt.lower() in itemList:
        print()
        for row in range(len(itemArt[lookAt])):
            print(itemArt[lookAt][row])
        print()
    else:
        print('Choose what\'s listed, dummy.')
