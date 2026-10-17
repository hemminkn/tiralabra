#!/usr/bin/python

import random
from mido import Message, MidiFile, MidiTrack

#generates a sequence of notes
def generate(trie, file_name):
    first = random.choice(trie.start_states)
    state = first
    generated = list(first)

    while len(generated) < 100:

        successors, weights = trie.find_next(state)
        if not successors:
            print()
            print(f"Couldn't find more successors, song has {len(generated)} notes.")
            break

        next_note = random.choices(successors, weights=weights, k=1)[0]
        generated.append(next_note)

        state = state[1:]+(next_note,)

    mid = MidiFile()
    track = MidiTrack()

    for note in generated:
        track.append(Message("note_on", note=note, velocity=64, time=32))
        track.append(Message("note_off", note=note, velocity=0, time=70))

    mid.tracks.append(track)
    mid.save(f"{file_name}.mid")

    print()
    print("Generated notes:")
    print()
    print(generated)
    print()
    return generated
