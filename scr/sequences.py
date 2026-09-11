#!/usr/bin/python

from mido import MidiFile

import sys

def get_sequence(filename):
	sequence = []
	mid = MidiFile(filename)
	for track in mid.tracks:
		for msg in track:
			if msg.type == "note_on":
				sequence.append(msg.note)
	print(sequence)

if __name__ == "__main__":
	get_sequence(sys.argv[1])
