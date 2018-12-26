#Monster dictionaries

monsterNames = (
    'goblin',
    'skeleton',
    'fairy',
    'larger spider',
    'giant snake',
    'rodent of unusual size',
    'humongous bat'
)

monsterDescriptions = {
    'goblin':'''A small, warty looking goblin stands here. They look to be ready for a nap or a
large meal. They eye you hungrily.''',
    'skeleton':'''The skeleton stands here, clacking as they move. They stare at you with glowing eyes.''',
    'fairy':'''The fairy is buzzing around anxiously. It looks very frail. You feel bad for it.
If only it had been born a little larger.''',
    'larger spider':'''This spider looks just like a regular spider, but uncomfortably larger.''',
    'giant snake':'''A large, slithery snake stares at you with beady, black eyes.''',
    'rodent of unusual size':'''This large rat skuttles around, occasionally glancing at you.
It looks rather diseased.''',
    'humongous bat':'''You were never really afraid of bats while you were sure they couldn't eat
you, but now you're uncomfortable and unsure if you're edible.'''
}

deadMonsterDescriptions = {
    'goblin':'''A small, warty looking goblin body lies here. They look like they died hungry.''',
    'skeleton':'''The dead skeleton lying here fills you with a sense of dread. It's bones have
been knocked around and partially scattered.''',
    'fairy':'''The fairy lies here, wings no longer attached to it's tiny body. Seeing it here
makes you contemplate mortality. It didn't really deserve to die.''',
    'larger spider':'''This uncomfortably large spider corpse at least is makes you more comfortable,
knowing that it is too dead to eat you.''',
    'giant snake':'''This large, slithery snake corpse lies here. Even in death, it continues
to stare at you with beady, dead eyes.''',
    'rodent of unusual size':'''This once-skuttling rat now lays bleeding on the ground. It is
most likely dead, but still carrying disease.''',
    'humongous bat':'''At least it can't suck your blood anymore.'''
}

monsterStats = { # Str, Int, Dex, HP, MP, AC
    'goblin':'4 3 4 8 0 1',
    'skeleton':'14 4 10 24 0 5',
    'fairy':'1 6 2 2 6 1',
    'larger spider':'5 2 6 8 0 3',
    'giant snake':'8 3 4 10 0 2',
    'rodent of unusual size':'2 5 4 6 0 3',
    'humongous bat':'4 6 10 10 0 2'
}

monsterItems = {
    'goblin':['dagger', 'padded armor', 'healing potion', 'water'],
    'skeleton':['short sword', 'healing potion'],
    'fairy':['dagger', 'mana potion', 'water'],
    'larger spider':['silken thread', 'dusty bread'],
    'giant snake':['sharp teeth', 'mana potion'],
    'rodent of unusual size':['moldy cheese', 'healing potion'],
    'humongous bat':['blood orange', 'dagger', 'muffin']
}

monsterDropPercentage = {
    'goblin':[80],
    'skeleton':[90],
    'fairy':[50],
    'larger spider':[80],
    'giant snake':[50],
    'rodent of unusual size':[40],
    'humongous bat':[30]

}

monsterMainStat = {
    'goblin':'strength',
    'skeleton':'strength',
    'fairy':'dexterity',
    'larger spider':'dexterity',
    'giant snake':'strength',
    'rodent of unusual size':'intelligence',
    'humongous bat':'dexterity'
}

monsterXP = { #Apprx. HP/2 * 10
    'goblin': 40,
    'skeleton': 120,
    'fairy': 20,
    'larger spider': 40,
    'giant snake': 50,
    'rodent of unusual size': 30,
    'humongous bat': 50
}