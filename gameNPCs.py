#NPC dictionaries

npcNames = (
    'guard',
    'alchemist',
    'shopkeeper',
    'baker',
    'townsfolk',
    'child'
)

npcDescriptions = {
    'guard':'''This guard stands here, defending. They look formidable and impressive. You
can\'t quite tell if they're a man or a woman, though.''',
    'alchemist':'''Tara the Alchemist stands before you, short and round, with flowing black
hair. She may have once been very beautiful, but after countless failed experiments and
explosions, her face and skin are burnt and deformed. Still, she is friendly enough.''',
    'shopkeeper':'''A big, bearded man. He looks as if he were once a knight, but now he
runs a tame little shop.''',
    'baker':'''A thin person of indeterminate gender. Their face is covered in flour on
their lips are dry. You hope this baker is taking care of themselves.''',
    'townsfolk':'''This person is well dressed and seems lively, although busy.''',
    'child':'''Small and energetic, this child seems to be vibrating. You wonder if they've
had a lot of candy today or if they're always like this.'''
}

deadNPCDescriptions = {
    'guard':'''A dead guard lies here. They look battered and bloody, dying to defend those
that can't defend themselves. Even in death, they look impressive and strong. What a shame
that they had to die at their prime. Still, you can't tell if they're a man or woman.''',
    'alchemist':'''Tara the alchemist lies here, bleeding out multi-coloured blood. It's
slightly off-putting and you can't help but wonder if she was actually human or not.''',
    'shopkeeper':'''A dead, bearded shopkeeper lies here. He was surely once proud in battle,
but now he lays bloody and defeated on the ground.''',
    'baker':'''The baker lays on the ground, their blood soaked up and dried in the flour.
It's obvious now that the baker was a woman, trying to stay thin in a shop surrounded by
delicious breads.''',
    'townsfolk':'''A townsfolk lies here, dead. They're no longer busy.''',
    'child':'''Their small, frail corpse lies on the ground. They died far before their time.'''
}

npcStats = {    # Str, Int, Dex, HP, MP, AC
    'guard':'16 10 12 30 0 15',
    'alchemist':'6 18 10 14 25 3',
    'shopkeeper':'18 12 12 50 0 10',
    'baker':'8 12 15 20 5 5',
    'townsfolk':'8 8 8 15 0 3',
    'child':'5 5 5 8 0 1'
}

npcItems = {
    'guard':['plate armor', 'short sword', 'large shield', 'healing potion'],
    'alchemist':['healing potion', 'healing potion', 'healing potion', 'thaumaturge robes', 'dagger'],
    'shopkeeper':['rope', 'short sword'],
    'baker':['fresh bread', 'chefs hat'],
    'townsfolk':['dagger'],
    'child':['small toy']
}

npcDropPercentage = {
    'guard':[70],
    'alchemist':[70],
    'shopkeeper':[50],
    'baker':[80],
    'townsfolk':[50],
    'child':[70]
}

npcMainStat = {
    'guard':'strength',
    'alchemist':'intelligence'
}

npcType = {
    'guard':'guard',
    'alchemist':'merchant',
    'shopkeeper':'merchant',
    'baker':'merchant',
    'townsfolk':'commoner',
    'child':'commoner'
}

npcGreeting = {
    'guard':'\'How may I help you this fine day?\' the guard says.',
    'alchemist':'\'Welcome to my little shop!\' the alchemist says.' ,
    'shopkeeper':'\'Welcome! What can I do ya for?\' the shopkeeper says.',
    'baker':'\'Welcome to my bakery\' the baker says.',
    'townsfolk':'\'Can I help you?\', the townsfolk says.',
    'child':'\'I\'m not supposed to talk to strangers...\' the child says.'
}

npcTalk = {
    'guard':['\'How may I help you this fine day?\' the guard says.',
             '\'Can I direct you somewhere?\' the guard says.',
             '\'Are you lost? I can help you get to where you need to go.\' the guard says.'],
    'alchemist':['\'Can I recommend the healing potions? They are particularly potent and useful,\' the alchemist says.',
                 '\'You seem the adventurous sort. Why not try a random, discount potion?\' the alchemist says.'],
    'shopkeeper':['\'Take a look around and see what catches yer fancy!\' the shopkeeper says.',
                '\'Our ropes are the strongest you\'ll find anywhere!\' the shopkeeper says.',
                '\'You look like the discerning sort. Everything in my shop is the highest quality!\', the shopkeeper says.'],
    'baker':['\'I make bread,\' the baker says.',
             '\'Please look at my breads.\' the baker says.',
             '\It\'s all delicious.\' the baker says.',
             '\'Please just choose a bread,\' the baker says.',
             '\'I don\'t really want to talk to you,\' the baker says.'],
    'townsfolk':['I\'m quite busy, right now,\' the townsfolk says.',
                 '\'I really must be getting on.\' the townsfolk says.',
                 '\'I\'m sure you have more important things to do than talk to me.\' the townsfolk says.',
                 'The townsfolk impatiently looks at their watch.'],
    'child':['\'Gee, I sure like candy.\' the child says.',
             '\'I think I lost my toy in the garden.\'',
             '\'You should probably talk to a grownup.\'']
}

npcFarewell = {
    'guard':['\'May the gods protect you!\' the guard says.',
             '\'Safe travels,\' the guard says.' ,
             '\'Stay true to your course.\' the guard says.'],
    'alchemist':['\'Don\'t be a stranger!\' the alchemist says.',
                 '\'Come again, soon!\' the alchemist says.',
                 '\'Safe travels!\' the alchemist says.'],
    'shopkeeper':['\'Don\'t be a stranger!\' the shopkeeper says.',
                 '\'Come again, soon!\' the shopkeeper says.',
                 '\'Safe travels!\' the shopkeeper says.'],
    'baker':['\'Come again, I guess,\' the baker says.',
             '\'Enjoy your bread,\' the baker says.',
             'The baker seems to be relieved you\'re leaving.'],
    'townsfolk':['\'Have a good day,\' the townsfolk says.',
                 '\'See you,\' the townsfolk says.',
                 '\'Good day,\' the townsfolk says.'],
    'child':['\'See ya later,\' the child says.',
             '\'Nice to meet you,\' the child says.',
             '\'I better go see my mom,\' the child says.',
             'The child waves goodbye to you.']
}

npcAttacked = {
    'guard':'\'You will know Death, today,\' the guard says.',
    'alchemist':'\'Fool! You will never get another discount!\' the alchemist says.',
    'shopkeeper':'The shopkeeper laughs. \'Alright! Let it be a good fight!\' the shopkeep says.',
    'baker':'\'I just want to run my bakery in peace!\' the baker screeches.',
    'townsfolk':'\'I\'m not completely helpless, you know!\'',
    'child':'The child screams and starts to cry.'
}

npcOptions = {
    'guard':('directions', 'talk', 'leave'),
    'merchant':('buy', 'sell', 'random', 'talk', 'leave'),
    'commoner':('talk', 'leave')
}

npcOptPrompt = {
    'guard':'Do you want to ask DIRECTIONS, TALK, or LEAVE?',
    'merchant':'Do you want to BUY an item, SELL an item, TALK, or LEAVE?',
    'commoner':'Is there something you want to TALK about? Or do you want to LEAVE?'
}

merchantInventory = {
    'alchemist':('healing potion', 'mana potion'),
    'shopkeeper':('dagger', 'short sword', 'rope', 'padded armor', 'small shield', 'water'),
    'baker':('fresh bread', 'muffin', 'cake')
}
