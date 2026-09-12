import sys
import random
from collections import defaultdict, Counter
from sequences import get_sequence

class MarkovChain:
	def __init__(self, filename, order):
		self.filename = filename
		self.order = order
		self.model = defaultdict(Counter)

	def train(self):
		notes = get_sequence(self.filename)

		for i in range(len(notes)-self.order):
			state = tuple(notes[i:i+self.order])
			next_note = notes[i+self.order]
			self.model[state][next_note]+=1

		return(self.model)

if __name__ == "__main__":
	m = MarkovChain(sys.argv[1], 2)
	print(m.train())
