#encoding: utf-8
from __future__ import unicode_literals
import random
from pattern.en import referenced, pluralize
import chainer
import textwrap

##############################################################################
# NaNoGenMo 2014, by dbaker
# working title: Baroque Encodings
##############################################################################

adjs = list(open("resources/adjectives.txt").readlines())
adverbs = list(open("resources/adverbs.txt").readlines())
adjeys = list(open("resources/adjectively.txt").readlines())
ns = list(open("resources/nouns.txt").readlines())
verbed = list(open("resources/verbed.txt").readlines())
verbing = list(open("resources/verbing.txt").readlines())
quants = list(open("resources/quantities.txt").readlines())
places = list(open("resources/cities.txt").readlines())
qualities = list(open("resources/qualities.txt").readlines())
pronouns1 = list(open("resources/pronouns1.txt").readlines())
colors = list(open("resources/colors.txt").readlines())

# TODO multiple forms of pronoun, text replacement for formatting strings
# read from files

PRONOUN = ""
VERB = ""
NAME = ""

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

meanwhiles = list(open("resources/meanwhiles.txt").readlines())
actions = list(open("resources/actions.txt").readlines())
lost = list(open("resources/lost.txt").readlines())

def meanwhiler(string):
    return random.choice(meanwhiles).strip() + ", " + string

def look_around_you(string):
    if random.random() < 0.5:
        return "{pronoun} {action}. ".format(
            pronoun = capitalize(random.choice([PRONOUN, NAME])),
            action = random.choice(actions).strip()
        ) + capitalize(string)

    else:
        return string + " {pronoun} {action}.".format(
            pronoun = capitalize(random.choice([PRONOUN, NAME])),
            action = random.choice(actions).strip()
        )

def get_lost(string):
    said = ["said", "asked", "wondered", "demanded"]

    if random.random() < 0.5:
        return string + " {} {} said.".format(random.choice(lost).strip(), PRONOUN)
    else:
        return "{} {} {}.".format(random.choice(lost).strip(), PRONOUN, random.choice(said)) + " " + capitalize(string)

def suddenly(string):
    suddenlies = ["suddenly", "unexpectedly", "without warning", "in an instant"]
    return capitalize(random.choice(suddenlies)) + ", " + string


############################### PARAGRAPHS ###################################

# Edward Bulwer-Lytton, "Paul Clifford" (opening paragraph)
def opening():
    p = "it was {adjective} and {adjectively} {noun}.".format(
        adjective=referenced(random.choice(adjs)).strip(), 
        adjectively=random.choice(adjeys).strip(), 
        noun=random.choice(ns).strip()
        )

    return capitalize(p)

# Edward Bulwer-Lytton, "Paul Clifford" (opening paragraph)
def p1():
    p = "the {n1} {verbed1} {quant1} — except at occasional intervals, when it was checked by {adj1} {quant2} of {n2} which {verbed2} {nouns1} (for it is in {place} that our scene lies), {verbing1} the {n3}, and {adverbly} {verbing2} the {adjective} {n4} of the {nouns2} that {verbed3} the {nounness}.".format(
        n1=random.choice(ns).strip(),
        verbed1=random.choice(verbed).strip(),
        #quant1=pluralize(random.choice(ns).strip()),
        quant1=pluralize(random.choice(quants).strip()),
        adj1=random.choice(adjs).strip(),
        quant2=pluralize(random.choice(quants).strip()),
        n2=random.choice(ns).strip(),
        verbed2=random.choice(verbed).strip(),
        nouns1=pluralize(random.choice(ns).strip()),
        place=random.choice(places).strip(),
        verbing1=random.choice(verbing).strip(),
        n3=random.choice(ns).strip(),
        adverbly=random.choice(adverbs).strip(),
        verbing2=random.choice(verbing).strip(),
        adjective=random.choice(adjs).strip(),
        n4=random.choice(ns).strip(),
        nouns2=pluralize(random.choice(ns).strip()),
        verbed3=random.choice(verbed).strip(),
        nounness=random.choice(qualities).strip()
    )

    return capitalize(p)

# Oscar Wilde, "Dorian Gray"
def p2():
    p = "the {place} was filled with the {adjective1} {noun1} of {nouns1}, and when the {adjective2} {adjective3} {noun2} stirred admist the {nouns2} of the {noun3}, there came through the {adjective4} {noun4} the {adjective5} {noun5} of the {noun6}, or the more {adjective6} {noun7} of the {adjective7} {noun8}.".format(
        place = random.choice(ns).strip(),
        adjective1 = random.choice(adjs).strip(),
        noun1 = random.choice(ns).strip(),
        nouns1 = pluralize(random.choice(ns).strip()),
        adjective2 = random.choice(adjs).strip(),
        adjective3 = random.choice(adjs).strip(),
        noun2 = random.choice(ns).strip(),
        nouns2 = pluralize(random.choice(ns).strip()),
        noun3 = random.choice(ns).strip(),
        adjective4 = random.choice(adjs).strip(),
        noun4 = random.choice(ns).strip(),
        adjective5 = random.choice(adjs).strip(),
        noun5 = random.choice(ns).strip(),
        noun6 = random.choice(ns).strip(),
        adjective6 = random.choice(adjs).strip(),
        noun7 = random.choice(ns).strip(),
        adjective7 = random.choice(adjs).strip(),
        noun8 = random.choice(ns).strip()
    )

    if random.random() > 0.6:
        p = random.choice([look_around_you(p), get_lost(p)])
    elif random.random() > 0.8:
        p = suddenly(p)

    return capitalize(p)

# Alastair Reynolds, "Century Rain" (opening line)
# TODO not quite sure the beginning of this works
def p3():
    p = "the {noun} {verbing} {adverbly} under {place} was {adjective1} and {adjective2}, like {adjective3} {nouns}.".format(
        noun = random.choice(ns).strip(),
        verbing = random.choice(verbing).strip(),
        adverbly = random.choice(adverbs).strip(),
        place = random.choice(places).strip(),
        adjective1 = random.choice(adjs).strip(),
        adjective2 = random.choice(adjs).strip(),
        adjective3 = random.choice(adjs).strip(),
        nouns = pluralize( (random.choice(ns)).strip() )
    )

    if random.random() > 0.6:
        p = random.choice([look_around_you(p), get_lost(p)])

    return capitalize(p)

# David Foster Wallace, "Infinite Jest" (opening line)
def p4():
    p = "{pronoun} seated in {noun}, surrounded by {nouns1} and {nouns2}.".format(
        pronoun = capitalize(PRONOUN) + " " + VERB,
        noun = referenced(random.choice(ns).strip()),
        nouns1 = pluralize(random.choice(ns).strip()),
        nouns2 = pluralize(random.choice(ns).strip())
    )

    return p

# Alastair Reynolds, "Century Rain"
def p5():
    p = "the {noun1} was {verbing} {closer}, like {quant} of {adjective} {noun2}.".format(
        noun1 = random.choice(ns).strip(),
        verbing = random.choice(["creeping", "crawling", "sneaking", "slithering"]),
        closer = random.choice(["closer", "nearer"]),
        quant = referenced(random.choice(quants).strip()),
        adjective = random.choice(adjs).strip(),
        noun2 = random.choice(ns).strip()
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.4:
        p = random.choice([look_around_you(p), get_lost(p)])

    return capitalize(p)

# Alastair Reynolds, "A spy in Europa"
def p6():
    p = "the {noun1} was surrounded by {quant} of {noun2} {nouns}, {adjective} as {noun3}.".format(
        noun1 = random.choice(ns).strip(),
        quant = referenced(random.choice(quants).strip()),
        noun2 = random.choice(ns).strip(),
        nouns = pluralize(random.choice(ns).strip()),
        adjective = random.choice(adjs).strip(),
        noun3 = referenced(random.choice(ns).strip())
    )

    if random.random() > 0.6:
        p = random.choice([look_around_you(p), get_lost(p)])
    elif random.random() > 0.8:
        p = suddenly(p)

    return capitalize(p)

# Alastair Reynolds, "Century Rain"
def p7():
    p = "the {adjective1} sound of {noun1} pushed itself into the room, disturbing the silence like {adjective2} {noun2}.".format(
        adjective1 = random.choice(adjs).strip(),
        noun1 = random.choice(ns).strip(),
        adjective2 = referenced(random.choice(adjs).strip()),
        noun2 = random.choice(ns).strip()
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.4:
        p = random.choice([look_around_you(p), get_lost(p)])
    elif random.random() < 0.6:
        p = suddenly(p)

    return capitalize(p)

# Alastair Reynolds, "Turquoise Days"
def p8():
    p = "{adjective1} {nouns1} were detaching from the {adjective2} {nouns2} and {nouns3}, {verbing} in {adjective3} {quants}.".format(
        adjective1 = random.choice(adjs).strip(),
        nouns1 = pluralize(random.choice(ns).strip()),
        adjective2 = random.choice(adjs).strip(),
        nouns2 = pluralize(random.choice(ns).strip()),
        nouns3 = pluralize(random.choice(ns).strip()),
        verbing = random.choice(verbing).strip(),
        adjective3 = random.choice(adjs).strip(),
        quants = pluralize(random.choice(quants).strip())
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.5:
        p = suddenly(p)

    return capitalize(p)

def p9():
    p = "the walls of the {noun1} were metre-high {quants} of {adjective1} {noun2}, like the {adjective2} {nouns} of a {noun3}.".format(
        noun1 = random.choice(ns).strip(),
        quants = pluralize(random.choice(quants).strip()),
        adjective1 = random.choice(adjs).strip(),
        noun2 = random.choice(ns).strip(),
        adjective2 = random.choice(adjs).strip(),
        nouns = pluralize(random.choice(ns).strip()),
        noun3 = random.choice(ns).strip()
    )

    if random.random() < 0.25:
        p = random.choice([look_around_you(p), get_lost(p)])

    return capitalize(p)

def p10():
    p = "{color1}-colored {nouns} {verbed} from deep within the {color2} structure, {verbing1} and {verbing2}.".format(
        color1 = random.choice(colors).strip(),
        nouns = pluralize(random.choice(ns).strip()),
        verbed = random.choice(verbed).strip().split()[0],
        color2 = random.choice(colors).strip(),
        verbing1 = random.choice(verbing).strip(),
        verbing2 = random.choice(verbing).strip()
    )

    if random.random() < 0.25:
        p = meanwhiler(p)
    elif random.random() < 0.5:
        p = suddenly(p)

    return capitalize(p)


#########################################################################

def gen():
    text = ""

    for i in range(0, random.randint(1, 5)):
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
                p10()
            ]
        ) + random.choice([" ", "\n"])

    return text


############################### CHAPTERS ################################

def chapter1():
    lines = "dbaker\nNANODEGENMO: BAROQUE ENCODINGS\nNaNoGenMo 2014\n"
    title = "\n".join(line.center(70) for line in lines.split("\n"))
    title += "\n" + "-" * 70 + "\n\n"
    chapter = "CHAPTER 1\n=========\n\n" + opening() + "\n" + p1() + "\n"

    text = ""

    while len(text.split()) < 100:
        text += gen()

    with open("/home/dbaker/Desktop/chapter1.txt", "w+") as fp:
        fp.write(title.encode("utf-8") + chapter.encode("utf-8") + text.rstrip().lstrip().encode('utf-8'))


def chapter2():
    chapter = "\n\n\nCHAPTER 2\n=========\n\n"
    text = ""

    while len(text.split()) < 100:
        text += random.choice(["", "\n"]) + capitalize(chainer.gen("/home/dbaker/Desktop/chapter1.txt").decode("utf-8")) + random.choice([" ", "\n"])

    with open("/home/dbaker/Desktop/chapter2.txt", "w+") as fp:
        fp.write(chapter.encode("utf-8") + text.rstrip().lstrip().encode('utf-8'))


def chapter3():
    chapter = "\n\n\nCHAPTER 3\n=========\n\n"
    text = ""

    while len(text.split()) < 100:
        text += random.choice(["", "\n"]) + capitalize(chainer.gen("/home/dbaker/Desktop/chapter2.txt").decode("utf-8")) + random.choice([" ", "\n"])

    with open("/home/dbaker/Desktop/chapter3.txt", "w+") as fp:
        fp.write(chapter.encode("utf-8") + text.rstrip().lstrip().encode('utf-8'))

########################################################################

if __name__ == "__main__":
    #PRONOUN = raw_input("what pronoun would you like used throughout the book?\n")
    #NAME = capitalize(raw_input("choose a name\n"))
    PRONOUN = "they"
    NAME = "asciibat"

    if PRONOUN == "they":
        VERB = "were"
    else:
        VERB = "was"

    chapter1()
    chapter2()
    chapter3()

    chapter1, chapter2, chapter3 = [], [], []
    with open ("/home/dbaker/Desktop/chapter1.txt") as fp:
        chapter1 = fp.read()
    with open ("/home/dbaker/Desktop/chapter2.txt") as fp:
        chapter2 = fp.read()
    with open ("/home/dbaker/Desktop/chapter3.txt") as fp:
        chapter3 = fp.read()

    text = chapter1.decode("utf-8") + chapter2.decode("utf-8") + chapter3.decode("utf-8")
    text = wraptext(text, 70)

    with open("/home/dbaker/Desktop/baroque_encodings.txt", "w+") as fp:
        fp.write(text.encode('utf-8'))

