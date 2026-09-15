import sys
import random
from collections import defaultdict, Counter
from sequences import get_sequence
from pathlib import Path

class MarkovChain:
	def __init__(self, key, order):
		if key == "Minors":
			self.files = Path("../midi/Minors").glob("*.mid")
		else:
			self.files = Path("../midi/Majors").glob("*.mid")
		self.order = order
		self.model = defaultdict(Counter)

	def train(self):

		for file in self.files:
			notes = get_sequence(file)

			for i in range(len(notes)-self.order):
				state = tuple(notes[i:i+self.order])
				next_note = notes[i+self.order]

				self.model[state][next_note]+=1

		return(self.model)

if __name__ == "__main__":
	m = MarkovChain(sys.argv[1], 2)
	print(m.train())
