#NPC dictionaries

npcNames = (
    'guard',
    'alchemist'
)

npcDescriptions = {
    'guard':'''This guard stands here, defending. They look formidable and impressive. You
can\'t quite tell if they\'re a man or a woman, though.''',
    'alchemist':'''Tara the Alchemist stands before you, short and round, with flowing black
hair. She may have once been very beautiful, but after countless failed experiments and
explosions, her face and skin are burnt and deformed. Still, she is friendly enough.'''
}

deadNPCDescriptions = {
    'guard':'''A dead guard lies here. They look battered and bloody, dying to defend those
that can\'t defend themselves. Even in death, they look impressive and strong. What a shame
that they had to die at their prime. Still, you can\'t tell if they're a man or woman.''',
    'alchemist':'''Tara lies here, bleeding out multi-coloured blood. It's slightly off-
putting, but you can't help but wonder if she was actually human or not.'''
}

npcStats = {    # Str, Int, Dex, HP, MP, AC
    'guard':'16 10 12 30 0 15',
    'alchemist':'6 18 10 14 25 3'
}

npcItems = {
    'guard':['plate armor', 'short sword', 'large shield', 'healing potion'],
    'alchemist':['healing potion', 'healing potion', 'healing potion', 'wizard robes', 'dagger']
}

npcDropPercentage = {
    'guard':[70],
    'alchemist':[70]
}

npcMainStat = {
    'guard':'strength',
    'alchemist':'intelligence'
}

npcType = {
    'guard':'guard',
    'alchemist':'shopkeep'
}

npcGreeting = {
    'guard':'\'How may I help you this fine day?\' the guard says.',
    'alchemist':'\'Welcome to my little shop!\' the alchemist says.'              
}

npcTalk = {
    'guard':['\'How may I help you this fine day?\' the guard says.',
             '\'Can I direct you somewhere?\' the guard says.',
             '\'Are you lost? I can help you get to where you need to go.\' the guard says.'],
    'alchemist':['\'Can I recommend the healing potions? They are particularly potent and useful,\' the alchemist says.',
                 '\'You seem the adventurous sort. Why not try a random, discount potion?\' the alchemist says.']
}

npcFarewell = {
    'guard':['\'May the gods protect you!\' the guard says.',
             '\'Safe travels,\' the guard says.' ,
             '\'Stay true to your course.\' the guard says.'],
    'alchemist':['\'Don\'t be a stranger!\' the alchemist says.',
                 '\'Come again, soon!\' the alchemist says.',
                 '\'Safe travels!\' the alchemist says.']
}

npcAttacked = {
    'guard':'\'You will know Death, today,\' the guard says.',
    'alchemist':'\'Fool! You will never get another discount!\' the alchemist says.'
}

npcOptions = {
    'guard':('directions', 'talk', 'leave'),
    'shopkeep':('buy', 'sell', 'random', 'talk', 'leave')
}

npcOptPrompt = {
    'guard':'Do you want to ask DIRECTIONS, TALK, or LEAVE?',
    'shopkeep':'Do you want to BUY an item, SELL an item, buy a RANDOM item, TALK, or LEAVE?'
}

shopkeepInventory = {
    'alchemist':('healing potion', 'rope')
}
