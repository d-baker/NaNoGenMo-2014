import random
from bot import capitalize
ASSOCIATIONS = {}

# ughhh don't ask
def breakup(sentence):
    max = len(sentence) - 1

    for i in range (0, max):
        if sentence[i] in ASSOCIATIONS:
            l = ASSOCIATIONS.get(sentence[i])
            if sentence[i+1] not in l:
                if i >= max:
                    l.append(sentence[i])
                else:
                    l.append(sentence[i+1])
        else:
            if i >= max:
                ASSOCIATIONS[sentence[i]] = [sentence[i]]
            else:
                ASSOCIATIONS[sentence[i]] = [sentence[i+1]]

    if len(sentence) > 1:
        breakup(sentence[1:])

def gen(filepath, place, name):
    sentences = []
    with open(filepath) as fp:
        # TODO workaround: avoiding words that need to be capitalized completely
        sentences = [s.lower().strip("\n ") for s in fp.read().split(".") if place not in s and " i " not in s]

    # ugh I can't remember how to fix this
    sentences.remove(sentences[0])
    sentences.remove(sentences[len(sentences)-1])


    for sentence in sentences:
        breakup(sentence.split())

    s = random.choice(sentences)
    words = random.choice(sentences).split()
    i = 0
    while random.randint(0, len(words)-1) > len(words)-1:
        i+=1

    seedword = words[i]

    prefix = " ".join(w for w in words[:i])

    text = prefix + " " + seedword + " " + chain(seedword)

    # don't know where the key errors are coming from, so just sweeping them
    # under the carpet with this
    while text.split()[-1] in ASSOCIATIONS:
        text += chain(text.split()[-1])

    return text.strip()+ "."

def chain(seedword):
    if seedword in ASSOCIATIONS:
        return random.choice(ASSOCIATIONS[seedword]) + " "
    else:
        return seedword + " "


if __name__ == "__main__":
    print gen()
