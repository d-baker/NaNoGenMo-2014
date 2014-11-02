#encoding: utf-8
from __future__ import unicode_literals
import random
from pattern.en import referenced, pluralize

def gen():
    adjs = list(open("resources/adjectives.txt").read().split())
    adverbs = list(open("resources/adverbs.txt").read().split())
    adjeys = list(open("resources/adjectively.txt").read().split())
    ns = list(open("resources/nouns.txt").read().split())
    verbed = list(open("resources/verbed.txt").read().split())
    verbing = list(open("resources/verbing.txt").readlines())
    quants = list(open("resources/quantities.txt").read().split())
    places = list(open("resources/cities.txt").read().split())
    qualities = list(open("resources/qualities.txt").read().split())
    
    opening = "It was {adjective} and {adjectively} {noun}.".format(adjective=referenced(random.choice(adjs)), adjectively=random.choice(adjeys), noun=random.choice(ns))

    paragraph = "The {n1} {verbed1} in {quant1} — except at occasional intervals, when it was checked by {adj1} {quant2} of {n2} which {verbed2} (for it is in {place} that our scene lies), {verbing1} the {n3}, and {adverbly} {verbing2} the {adjective} {n4} of the {nouns} that {verbed3} against the {nounness}".format(
        n1=random.choice(ns),
        verbed1=random.choice(verbed),
        quant1=pluralize(random.choice(ns)),
        #quant1=random.choice(quants),
        adj1=random.choice(adjs),
        quant2=random.choice(quants),
        n2=random.choice(ns),
        verbed2=random.choice(verbed),
        place=random.choice(places),
        verbing1=random.choice(verbing).strip(),
        n3=random.choice(ns),
        adverbly=random.choice(adverbs),
        verbing2=random.choice(verbing).strip(),
        adjective=random.choice(adjs),
        n4=random.choice(ns),
        nouns=pluralize(random.choice(ns)),
        verbed3=random.choice(verbed),
        nounness=random.choice(qualities)
    )

    return opening + "\n" + paragraph

if __name__ == "__main__":
    print gen()
