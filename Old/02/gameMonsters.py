monsterNames = (
    'goblin',
    'skeleton',
    'fairy'
)

monsterDescriptions = {
    'goblin':'''A small, warty looking goblin stands here. They look to be ready for a nap or a
large meal.''',
    'skeleton':'''This skeleton looks pretty spooky. He could probably smear you without even
thinking about it.''',
    'fairy':'''The fairy is buzzing around anxiously. It looks very frail. You feel bad for it.
If only it had been born a little larger.'''
}

monsterStats = { # Str, Int, Dex, HP, MP, AC
    'goblin':'4 3 4 8 0 1',
    'skeleton':'14 4 10 24 0 2',
    'fairy':'1 6 2 2 6 1'
}

monsterItems = {
    'goblin':['dagger', 'padded armor'],
    'skeleton':['short sword', 'healing potion'],
    'fairy':['wings']
}

monsterDropPercentage = {
    'goblin':[12],
    'skeleton':[10],
    'fairy':[40]

}

monsterMainStat = {
    'goblin':'strength',
    'skeleton':'strength',
    'fairy':'dexterity'
}