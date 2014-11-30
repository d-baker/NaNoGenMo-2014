#encoding: utf-8
from __future__ import unicode_literals
from pattern.en import tag

def parse_pos(source_filename, output_filename, pos):
    wordlist = list(open(source_filename).read().split())
    matched_words = [word for word in wordlist if tag(word)[0][1] == pos]

    fp = open(output_filename, "w")
    for w in matched_words:
        fp.write("%s\n" % w)
    fp.close()


if __name__ == "__main__":
    # refer to the link below for tags that can be used:
    # http://www.clips.ua.ac.be/pages/mbsp-tags
    parse_pos("full-wordlist.txt", "superlatives.txt", "RBS")
