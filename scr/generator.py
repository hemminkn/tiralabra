#!/usr/bin/python

import random
import trie

def generate(degree):

midi = []
help_list = []

first = random.choice(trie) #i know this is not correct

#after the first we generate until len(help_list) == degree
#and then we use that as the start state to start generating the next progressions
# and the window moves until the midi-list has enough notes to make a midi file

while len(midi) < 100:

    successors, weights = trie.find_next(state)
    if not successors:
        break

    next_note = random.choices(successors, weights=weights, k=1)[0]

