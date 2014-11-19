#encoding: utf-8
from __future__ import unicode_literals
import random
from pattern.en import referenced, pluralize

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

PRONOUN = ""
VERB = ""
NAME = ""

# Edward Bulwer-Lytton, "Paul Clifford" (opening paragraph)
def opening():
    p = "It was {adjective} and {adjectively} {noun}.".format(
        adjective=referenced(random.choice(adjs)).strip(), 
        adjectively=random.choice(adjeys).strip(), 
        noun=random.choice(ns).strip()
        )
    return p

# Edward Bulwer-Lytton, "Paul Clifford" (opening paragraph)
def p1():
    p = "The {n1} {verbed1} {quant1} — except at occasional intervals, when it was checked by {adj1} {quant2} of {n2} which {verbed2} {nouns1} (for it is in {place} that our scene lies), {verbing1} the {n3}, and {adverbly} {verbing2} the {adjective} {n4} of the {nouns2} that {verbed3} the {nounness}.".format(
        n1=random.choice(ns).strip(),
        verbed1=random.choice(verbed).strip(),
        #quant1=pluralize(random.choice(ns).strip()),
        quant1=random.choice(quants).strip(),
        adj1=random.choice(adjs).strip(),
        quant2=random.choice(quants).strip(),
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

    return p

# Oscar Wilde, "Dorian Gray"
def p2():
    p = "The {place} was filled with the {adjective1} {noun1} of {nouns1}, and when the {adjective2} {adjective3} {noun2} stirred admist the {nouns2} of the {noun3}, there came through the {adjective4} {noun4} the {adjective5} {noun5} of the {noun6}, or the more {adjective6} {noun7} of the {adjective7} {noun8}.".format(
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

    return p

# Alastair Reynolds, "Century Rain" (opening line)
def p3():
    p = "The {noun} {verbing} {adverbly} under {place} was {adjective1} and {adjective2}, like {adjective3} {nouns}.".format(
        noun = random.choice(ns).strip(),
        verbing = random.choice(verbing).strip(),
        adverbly = random.choice(adverbs).strip(),
        place = random.choice(places).strip(),
        adjective1 = random.choice(adjs).strip(),
        adjective2 = random.choice(adjs).strip(),
        adjective3 = random.choice(adjs).strip(),
        nouns = pluralize( (random.choice(ns)).strip() )
    )

    return p

def p4():
    p = "{pronoun} seated in {noun}, surrounded by {nouns1} and {nouns2}.".format(
        pronoun = PRONOUN + " " + VERB,
        noun = referenced(random.choice(ns).strip()),
        nouns1 = pluralize(random.choice(ns).strip()),
        nouns2 = pluralize(random.choice(ns).strip())
    )

    return p

def gen():

    text = ""

    for i in range(0, random.randint(1, 5)):
        text += "\n" + random.choice([opening(), p1(), p2(), p3(), p4()]) + "\n"

    return text



if __name__ == "__main__":
    #PRONOUN = raw_input("what pronoun would you like used throughout the book?\n")
    #NAME = raw_input("choose a name\n")
    PRONOUN = "they"
    NAME = "Sasha"

    if PRONOUN == "they":
        VERB = "were"
    else:
        VERB = "was"

    for i in range (0, 5):
        print gen()
