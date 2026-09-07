#!/usr/bin/python

from mido import MidiFile

import sys

def read_midi(filename):
	mid = MidiFile(filename)
	for i, track in enumerate(mid.tracks):
		print('Track {}: {}'.format(i, track.name))
		for msg in track:
			print(msg)

if __name__ == "__main__":
	read_midi(sys.argv[1])
