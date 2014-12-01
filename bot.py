#encoding: utf-8
from __future__ import unicode_literals
import random
from pattern.en import referenced, pluralize
import chainer
import textwrap
import os

##############################################################################
# NaNoGenMo 2014, by dbaker
##############################################################################

adjs = [line.strip() for line in open("resources/adjectives.txt").readlines()]
adverbs = [line.strip() for line in open("resources/adverbs.txt").readlines()]
adjeys = [line.strip() for line in open("resources/adjectively.txt").readlines()]
ns = [line.strip() for line in open("resources/nouns.txt").readlines()]
verbed = [line.strip() for line in open("resources/verbed.txt").readlines()]
verbing = [line.strip() for line in open("resources/verbing.txt").readlines()]
quants = [line.strip() for line in open("resources/quantities.txt").readlines()]
places = [line.strip() for line in open("resources/cities.txt").readlines()]
qualities = [line.strip() for line in open("resources/qualities.txt").readlines()]
colors = [line.strip() for line in open("resources/colors.txt").readlines()]
fnames = [line.strip() for line in open("resources/names-f.txt").readlines()]
mnames = [line.strip() for line in open("resources/names-m.txt").readlines()]
superlatives = [line.strip() for line in open("resources/superlatives.txt").readlines()]

PRONOUN = "they"
POS_PRONOUN = "their"
VERB = "were"
NAME = random.choice([random.choice(fnames), random.choice(mnames)])
PLACE = random.choice(places)
LENGTH = random.randint(1000, 50000)
NUM_CHAPTERS = random.randint(2, 15)

while LENGTH / NUM_CHAPTERS < 100:
    LENGTH = random.randint(1000, 50000)
    NUM_CHAPTERS = random.randint(2, 15)

TITLE = "Baroque Encodings: A Degenerative Novel"

############################## STRING MANIP TOOLS #############################

def decapitalize(string):
    return string[:1].lower() + string[1:]

def capitalize(string):
    return string[:1].upper() + string[1:]

# thankyou helpful person 
# http://stackoverflow.com/questions/1166317/python-textwrap-library-how-to-preserve-line-breaks
def wraptext(text, char_lim):
    new_text = ""
    lines = text.split("\n")

    for line in lines:
        if len(line) > char_lim:
            w = textwrap.TextWrapper(width=char_lim, break_long_words=False)
            line = '\n'.join(w.wrap(line))

        new_text += line + "\n"

    return new_text


############################## STORYTELLING TOOLS #############################

meanwhiles = [line.strip() for line in open("resources/meanwhiles.txt").readlines()]
actions = [line.strip() for line in open("resources/actions.txt").readlines()]
lost = [line.strip() for line in open("resources/lost.txt").readlines()]

def meanwhiler(string):
    return random.choice(meanwhiles) + ", " + string

def look_around_you(string):
    if random.random() < 0.5:
        return "{pronoun} {action}. ".format(
            pronoun = capitalize(random.choice([PRONOUN, NAME])),
            action = random.choice(actions)
        ) + capitalize(string)

    else:
        return string + " {pronoun} {action}.".format(
            pronoun = capitalize(random.choice([PRONOUN, NAME])),
            action = random.choice(actions)
        )

def get_lost(string):
    said = ["said", "asked", "wondered", "demanded"]

    if random.random() < 0.5:
        return string + " {} {} said.".format(random.choice(lost), random.choice([PRONOUN, NAME]))
    else:
        return "{} {} {}.".format(random.choice(lost), random.choice([PRONOUN, NAME]), random.choice(said)) + " " + capitalize(string)

def suddenly(string):
    suddenlies = ["suddenly", "unexpectedly", "without warning", "in an instant"]
    return capitalize(random.choice(suddenlies)) + ", " + string


############################### PARAGRAPHS ###################################

# Edward Bulwer-Lytton, "Paul Clifford" (opening paragraph)
def opening():
    p = "it was {adjective} and {adjectively} {noun}.".format(
        adjective=referenced(random.choice(adjs)), 
        adjectively=random.choice(adjeys), 
        noun=random.choice(ns)
        )

    return capitalize(p)

# Edward Bulwer-Lytton, "Paul Clifford" (opening paragraph)
def p1():
    p = "the {n1} {verbed1} {quant1} — except at occasional intervals, when it was checked by {adj1} {quant2} of {n2} which {verbed2} {nouns1} (for it is in {place} that our scene lies), {verbing1} the {n3}, and {adverbly} {verbing2} the {adjective} {n4} of the {nouns2} that {verbed3} the {nounness}.".format(
        n1=random.choice(ns),
        verbed1=random.choice(verbed),
        quant1=pluralize(random.choice(quants)),
        adj1=random.choice(adjs),
        quant2=pluralize(random.choice(quants)),
        n2=random.choice(ns),
        verbed2=random.choice(verbed),
        nouns1=pluralize(random.choice(ns)),
        place=PLACE,
        verbing1=random.choice(verbing),
        n3=random.choice(ns),
        adverbly=random.choice(adverbs),
        verbing2=random.choice(verbing),
        adjective=random.choice(adjs),
        n4=random.choice(ns),
        nouns2=pluralize(random.choice(ns)),
        verbed3=random.choice(verbed),
        nounness=random.choice(qualities)
    )

    return capitalize(p)

# Oscar Wilde, "Dorian Gray"
def p2():
    p = "the {place} was filled with the {adjective1} {noun1} of {nouns1}, and when the {adjective2} {adjective3} {noun2} stirred admist the {nouns2} of the {noun3}, there came through the {adjective4} {noun4} the {adjective5} {noun5} of the {noun6}, or the more {adjective6} {noun7} of the {adjective7} {noun8}.".format(
        place = random.choice(ns),
        adjective1 = random.choice(adjs),
        noun1 = random.choice(ns),
        nouns1 = pluralize(random.choice(ns)),
        adjective2 = random.choice(adjs),
        adjective3 = random.choice(adjs),
        noun2 = random.choice(ns),
        nouns2 = pluralize(random.choice(ns)),
        noun3 = random.choice(ns),
        adjective4 = random.choice(adjs),
        noun4 = random.choice(ns),
        adjective5 = random.choice(adjs),
        noun5 = random.choice(ns),
        noun6 = random.choice(ns),
        adjective6 = random.choice(adjs),
        noun7 = random.choice(ns),
        adjective7 = random.choice(adjs),
        noun8 = random.choice(ns)
    )

    if random.random() > 0.6:
        p = random.choice([look_around_you(p), get_lost(p)])
    elif random.random() > 0.8:
        p = suddenly(p)

    return capitalize(p)

# David Foster Wallace, "Infinite Jest" (opening line)
def p3():
    p = "{pronoun} seated in {noun}, surrounded by {nouns1} and {nouns2}.".format(
        pronoun = capitalize(PRONOUN) + " " + VERB,
        noun = referenced(random.choice(ns)),
        nouns1 = pluralize(random.choice(ns)),
        nouns2 = pluralize(random.choice(ns))
    )

    return capitalize(p)

# Alastair Reynolds, "Century Rain"
def p4():
    p = "the {noun1} was {verbing} {closer}, like {quant} of {adjective} {noun2}.".format(
        noun1 = random.choice(ns),
        verbing = random.choice(["creeping", "crawling", "sneaking", "slithering"]),
        closer = random.choice(["closer", "nearer"]),
        quant = referenced(random.choice(quants)),
        adjective = random.choice(adjs),
        noun2 = random.choice(ns)
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.4:
        p = random.choice([look_around_you(p), get_lost(p)])

    return capitalize(p)

# Alastair Reynolds, "A spy in Europa"
def p5():
    p = "the {noun1} was surrounded by {quant} of {noun2} {nouns}, {adjective} as {noun3}.".format(
        noun1 = random.choice(ns),
        quant = referenced(random.choice(quants)),
        noun2 = random.choice(ns),
        nouns = pluralize(random.choice(ns)),
        adjective = random.choice(adjs),
        noun3 = referenced(random.choice(ns))
    )

    if random.random() > 0.6:
        p = random.choice([look_around_you(p), get_lost(p)])
    elif random.random() > 0.8:
        p = suddenly(p)

    return capitalize(p)

# Alastair Reynolds, "Century Rain"
def p6():
    p = "the {adjective1} sound of {noun1} pushed itself into the room, disturbing the silence like {adjective2} {noun2}.".format(
        adjective1 = random.choice(adjs),
        noun1 = random.choice(ns),
        adjective2 = referenced(random.choice(adjs)),
        noun2 = random.choice(ns)
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.4:
        p = random.choice([look_around_you(p), get_lost(p)])
    elif random.random() < 0.6:
        p = suddenly(p)

    return capitalize(p)

# Alastair Reynolds, "Turquoise Days"
def p7():
    p = "{adjective1} {nouns1} were detaching from the {adjective2} {nouns2} and {nouns3}, {verbing} in {adjective3} {quants}.".format(
        adjective1 = random.choice(adjs),
        nouns1 = pluralize(random.choice(ns)),
        adjective2 = random.choice(adjs),
        nouns2 = pluralize(random.choice(ns)),
        nouns3 = pluralize(random.choice(ns)),
        verbing = random.choice(verbing),
        adjective3 = random.choice(adjs),
        quants = pluralize(random.choice(quants))
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.5:
        p = suddenly(p)

    return capitalize(p)

def p8():
    p = "the walls of the {noun1} were metre-high {quants} of {adjective1} {noun2}, like the {adjective2} {nouns} of a {noun3}.".format(
        noun1 = random.choice(ns),
        quants = pluralize(random.choice(quants)),
        adjective1 = random.choice(adjs),
        noun2 = random.choice(ns),
        adjective2 = random.choice(adjs),
        nouns = pluralize(random.choice(ns)),
        noun3 = random.choice(ns)
    )

    if random.random() < 0.25:
        p = random.choice([look_around_you(p), get_lost(p)])

    return capitalize(p)

def p9():
    p = "{color1}-colored {nouns} {verbed} from deep within the {color2} structure, {verbing1} and {verbing2}.".format(
        color1 = random.choice(colors),
        nouns = pluralize(random.choice(ns)),
        verbed = random.choice(verbed).split()[0],
        color2 = random.choice(colors),
        verbing1 = random.choice(verbing),
        verbing2 = random.choice(verbing)
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.5:
        p = suddenly(p)

    return capitalize(p)

# Alastair Reynolds, "House of Suns"
def p10():
    p = "beneath {pronoun2} feet, the {adjective1} {noun1} {verbed} with the {adjective2} {quality} of {nouns1} and {nouns2}.".format(
        pronoun2 = random.choice([POS_PRONOUN, NAME + "\'s"]),
        adjective1 = random.choice(adjs),
        noun1 = random.choice(ns),
        verbed = random.choice(verbed),
        adjective2 = random.choice(adjs),
        quality = random.choice(qualities),
        nouns1 = pluralize(random.choice(ns)),
        nouns2 = pluralize(random.choice(ns))
    )

    return capitalize(p)

# Diamond Dogs
def p11():
    p = "the {noun1} was studded with an enormous number of {nouns}, flooding the {noun2} with {adjective} {noun3}.".format(
        noun1 = random.choice(ns),
        nouns = pluralize(random.choice(ns)),
        noun2 = random.choice(ns),
        adjective = random.choice(adjs),
        noun3 = random.choice(ns)
    )
    if random.random() < 0.25:
        p = look_around_you(p)

    return capitalize(p)

def p12():
    p = "{noun1} stood in the middle of the {noun2}, surrounded by {noun3} of {adjective} {nouns}.".format(
        noun1 = referenced(random.choice(ns)),
        noun2 = random.choice(ns),
        verbed = random.choice(verbed),
        noun3 = referenced(random.choice(ns)),
        adjective = random.choice(adjs),
        nouns = pluralize(random.choice(ns))
    )
    if random.random() < 0.25:
        p = look_around_you(p)

    return capitalize(p)

# Revelation Space
def p13():
    p = "the sound that the {nouns1} made was {adjective1} and {adjective2}; {adjective3} {adjective4} {nouns2} so {adjective5} that they were almost {verbed1} rather than {verbed2}.".format(
        nouns1 = pluralize(random.choice(ns)),
        adjective1 = random.choice(adjs),
        adjective2 = random.choice(adjs),
        adjective3 = random.choice(adjs),
        adjective4 = random.choice(adjs),
        nouns2 = pluralize(random.choice(ns)),
        adjective5 = random.choice(adjs),
        verbed1 = random.choice(verbed),
        verbed2 = random.choice(verbed)
    )
    if random.random() < 0.25:
        p = look_around_you(p)

    return capitalize(p)

def p14():
    p = "it was like the {superlative} {adjective1} {noun1}'s {noun2} imaginable; the sound that a {noun2} might make after {verbing} through a thousand miles of {noun3}.".format(
        superlative = random.choice(superlatives),
        adjective1 = random.choice(adjs),
        noun1 = random.choice(ns),
        noun2 = random.choice(ns),
        verbing = random.choice(verbing),
        noun3 = random.choice(ns)
    )

    return capitalize(p)

def p15():
    p = "the {noun1} consisted of {noun2}-like {adjective} {nouns1}, interupted at {number} points by {nouns2}.".format(
        noun1 = random.choice(ns),
        noun2 = random.choice(ns),
        adjective = random.choice(adjs),
        nouns1 = pluralize(random.choice(ns)),
        number = str(random.randint(3, 9)),
        nouns2 = pluralize(random.choice(ns))
    )
    if random.random() < 0.25:
        p = look_around_you(p)

    return capitalize(p)

# House of Suns
def p16():
    p = "the {noun1} was {adjective1} {noun2}, divided into {adjective2} {nouns1} by {quant} of {adjective3} {color} {nouns2}.".format(
        noun1 = random.choice(ns),
        adjective1 = referenced(random.choice(adjs)),
        noun2 = random.choice(ns),
        adjective2 = random.choice(adjs),
        nouns1 = pluralize(random.choice(ns)),
        quant = referenced(random.choice(quants)),
        adjective3 = random.choice(ns),
        color = random.choice(colors),
        nouns2 = pluralize(random.choice(ns))
    )

    return capitalize(p)

#########################################################################

def gen():
    text = ""

    for i in range(0, random.randint(1, 3)):
        text += random.choice(["", "\n"]) + random.choice(
            [
                p2(), 
                p3(), 
                p4(),
                p5(),
                p6(),
                p7(), 
                p8(),
                p9(),
                p10(),
                p11(),
                p12(),
                p13(),
                p13() + " " + p14(),
                p15(), 
                p16()
            ]
        ) + random.choice([" ", "\n"])

    return text


############################### CHAPTERS ################################

def gen_chapters():
    for i in range(1, NUM_CHAPTERS + 1):
        text = ""

        if i == 1:
            lines = "\n{} \n\nDorothea Baker | NaNoGenMo 2014\n".format(TITLE.upper())
            title = "\n".join(line.center(70) for line in lines.split("\n"))
            title += "\n" + "-" * 70 + "\n\n"
            chapter = "CHAPTER 1\n=========\n\n" + opening() + "\n" + p1() + "\n"

            while len(text.split()) < LENGTH / NUM_CHAPTERS:
                text += gen()

            with open("chapter1.txt", "w+") as fp:
                fp.write(title.encode("utf-8") + chapter.encode("utf-8") + text.rstrip().lstrip().encode('utf-8'))

        else:
            chapter = "\n\n\nCHAPTER {}\n=========\n\n".format(i)
            previous_chapter = "chapter{}.txt".format(i-1)
            new_chapter = "chapter{}.txt".format(i)

            while len(text.split()) < LENGTH / NUM_CHAPTERS:
                text += random.choice(["", "\n"]) + capitalize(chainer.gen(previous_chapter, PLACE, NAME).decode("utf-8")) + random.choice([" ", "\n"])

            with open(new_chapter, "w+") as fp:
                fp.write(chapter.encode("utf-8") + text.rstrip().lstrip().encode('utf-8'))

########################################################################

if __name__ == "__main__":
    print ("\n" + "-" * 70 + "\n")
    print wraptext("Welcome to {}.\nYou can customise some aspects of the story, or keep the default settings.\n\nThis code wasn't written with efficiency in mind and will appear to hang for some time with the default word count. Feel free to experiment, but please keep this in mind when choosing chapter and word counts. I'm not responsible for what happens if you ask for 10000 chapters.".format(TITLE), 70)
    print ("-" * 70)

    n = capitalize(raw_input("\nchoose a name for the \"protagonist\" (default: random)\n"))
    if not n:
        print("protagonist's name is {}".format(NAME))

    p = raw_input("\nwhat pronoun would you like used throughout the book? (default: {})\n".format(PRONOUN))

    pl = raw_input("\nwhere would you like the story to take place? (default: random)\n")
    if not pl:
        print("story takes place in {}".format(PLACE))

    c = raw_input(wraptext("\nhow many chapters would you like to generate? (default: random between 2-15)", 70))
    if not c:
        print("number of chapters is {}".format(NUM_CHAPTERS))

    l = raw_input(wraptext("\nhow many words would you like to generate (roughly)? WARNING: large numbers may take a long time. (default: random between 1000-50000)", 70))
    if not l:
        print("number of words is {}".format(LENGTH))

    # UGH
    if p:
        PRONOUN = p
    if n:
        NAME = n
    if pl:
        PLACE = pl
    if l:
        LENGTH = int(l)
        while LENGTH / NUM_CHAPTERS < 100:
            l = raw_input("\nsorry, that's probably not enough words to split between the chapters. try again:\n")
            LENGTH = int(l)
    if c:
        NUM_CHAPTERS = int(c)

    if PRONOUN != "they":
        VERB = "was"
        if PRONOUN == "he":
            POS_PRONOUN = "his"
        elif PRONOUN == "she":
            POS_PRONOUN = "her"


    print ("\nplease wait...\n")

    gen_chapters()

    text = ""
    for i in range(1, NUM_CHAPTERS + 1):
        with open ("chapter{}.txt".format(i)) as fp:
            text += fp.read().decode("utf-8")

    #text = wraptext(text, 70)

    with open("baroque_encodings.txt", "w+") as fp:
        fp.write(text.encode('utf-8'))

    for i in range(1, NUM_CHAPTERS+1):
        os.remove("chapter" + str(i) + ".txt")

    print wraptext("\nYour novel has been generated and is located in \"baroque_encodings.txt\".", 70)

