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

	def train(self):
		for file in self.files:
			notes = get_sequence(file)

			start_state = tuple(notes[:self.order])
			self.trie.start_states.append(start_state)

			for i in range(len(notes)-self.order):
				state = tuple(notes[i:i+self.order])
				next_note = notes[i+self.order]

				self.trie.insert(state, next_note)
