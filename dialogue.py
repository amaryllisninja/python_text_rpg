import random, time

def narrator():
    global narratorSnark
    narratorSnark = ["Your mother would be proud.",
                     "What a shame you've done so little with your life.",
                     "I'm sure, with time and therapy, you'll come to forgive yourself.",
                     "You can't blame this one on your dad.",
                     "Your mother was a hamster and your father smells of elderberries.",
                     "Who taught you how to type?",
                     "Are you even trying to play this game?",
                     "Not all advice is good advice. Like this one for example. \nIt's just an obvious statement.",
                     "Thanks.",
                     "Your mom told you there was no such thing as a stupid question. \nMy mom said there're always exceptions to rules.",
                     "Your dating profile probably only has pictures of cute dogs.",
                     "If you ever have a dead body in your trunk, don't blow past a stop sign.",
                     "If every pork chop was perfect, we wouldn't have you. I mean, hot dogs.",
                     "You're gay. And by that, I mean needlessly happy.",
                     "If only we could all be like you...",
                     "A garlic clove a day keeps the dentist away. \nBut you don't need the garlic.",
                     "Every cloud has a rain storm waiting to be unleashed.",
                     "Oh, I'm fine, by the way.",
                     "You've done well for some with your eduction.",
                     "Are you sure you finished grade school?",
                     "I didn't hear what you said, but I'm sure the trees heard you.",
                     "If only we could all see the world the way you do.",
                     "Sure, sure.",
                     "Ookay.",
                     "At least you have great fingernails.",
                     "Do you even know what calusses are.",
                     "Bribery is only acceptable if it isn't money.",
                     "We can't all look like you. Fortunately.",
                     "You're part of what's wrong with this game.",
                     "If only I were so grossly incandescent.",
                     "You have the healthy appetite of an elephant.",
                     "What are you, from Jurassic Park or something?",
                     "Your outlook on life is unique.",
                     "Whatever you say, Chief.",
                     "The world is your canvas and you forgot the paintbrush.",
                     "Don't cry over spilt milk. Suck it up.",
                     "Lean on me! BOOM! Hey! You didn't expect me to stay there, did you?",
                     "If I were you, I'd probably forget to wake up tomorrow.",
                     "It's OK if you're late. No one really needs you today.",
                     "Intelligence is a blessing. You are neither.",
                     "Giraffes have longs necks so they don't have to see you.",
                     "Don't abandon your hopes and dreams. I still need a reason to make fun of you.",
                     "When I said there is no such thing as a stupid question,\nI didn't think you'd take it as a challenge.",
                     "I'm mostly speaking in generalities when I'm talking about you.",
                     "If you say so.",
                     "Is this something I'm giong to have to listen to?",
                     "You eat like a bird. A baby bird, specifically.",
                     "Congratulations on winning a consolation prize.",
                     "If you're trying to be terrible, you're really hitting the mark.",
                     "Without ugliness, we could not know beauty.\nThanks for that.",
                     "Suck less.",
                     "Your ignorance is showing.",
                     "Snarf SNARF snarf snarf."]
    quoteAmt = len(narratorSnark) - 1
    quoteNum = random.randint(0, quoteAmt)
    print(narratorSnark[quoteNum])

def advice():
    global adviceList
    adviceList = ["Try typing \'look at self\'.",
                  "When looking at or getting an item, type it's full name."]

def fortune():
    global fortuneCookie
    fortuneCookie = ["A man never got shot while doing dishes.",
                     "Smart parents investigate",
                     "A man that runs behind a car gets exhausted.",
                     "You got the wrong fortune. Good fortune comes to the person on your left.",
                     "Beware the light at the end of the tunnel.\nIt may be the train.",
                     "An alien of some sort will be appearing to you shortly!",
                     "You may not like the beard at first, but it will grow on you.",
                     "If everything seems to be going your way, you're in the wrong lane.",
                     "When life gives you lemons, demand to see life's manager.",
                     "If at first you don't succdeed, don't try skydiving."]

deathLess5 = [
    "\'Nice to see you, again. You should probably be more careful,\nthough. Shall we go for a walk?\'",
    "\'Hey. Are you still confused about what's going on?\nThat's completely understandable. You've just died, and that's always disorienting.\nJoin me for a walk?\'"
]

deathLess10 = [
    "\'I didn't expect to see you so soon. Did you miss me? Well, why\ndon't we go for a walk.\'",
    "\'Dying gets less uncomfortable the more it happens, doesn't it?\nWhy don't we go for a walk?\'"
]

deathLess15 = [
    "\'Can't say that I'm really surprised to see you, by now. You sure\nlike getting into trouble, don't you?\nLet's walk.\'",
    "\'You're really starting to turn this dying thing into a real habit,\n huh? No matter. Let's go for a walk.\'"
]

deathGreater15 = [
    "\'You know the deal, by now. Let's go.\'"
]
