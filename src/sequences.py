#!/usr/bin/python

from mido import MidiFile

import sys

#creates a sequence of notes from the given file
def get_sequence(filename):
	sequence = []
	mid = MidiFile(filename)
	for track in mid.tracks:
		for msg in track:
			if msg.type == "note_on":
				sequence.append(msg.note)
	return(sequence)

if __name__ == "__main__":
	get_sequence(sys.argv[1])
