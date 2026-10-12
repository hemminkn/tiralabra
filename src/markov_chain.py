import sys
from sequences import get_sequence
from pathlib import Path
from trie import Trie

class MarkovChain:
	def __init__(self, key, order):
		self.trie = Trie() #alustetaan trie, eli t = Train("Minors", 2) -> t.trie
		self.order = order

		if key == "Minors":
			self.files = Path("../midi/Minors").glob("*.mid")
		else:
			self.files = Path("../midi/Majors").glob("*.mid")

	#trains chain based on the key chosen by the user
	def train_notes(self, notes):
		start_state = tuple(notes[:self.order])
		self.trie.start_states.append(start_state)

		for i in range(len(notes)-self.order):
			state = tuple(notes[i:i+self.order])
			next_note = notes[i+self.order]

			self.trie.insert(state, next_note)

	def train(self):
		for file in self.files:
			notes = get_sequence(file)

			self.train_notes(notes)
