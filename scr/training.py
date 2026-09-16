import sys
from sequences import get_sequence
from pathlib import Path
import trie

class Train:
	def __init__(self, key, order):
		if key == "Minors":
			self.files = Path("../midi/Minors").glob("*.mid")
		else:
			self.files = Path("../midi/Majors").glob("*.mid")
		self.order = order

	def organize_data(self):

		for file in self.files:
			notes = get_sequence(file)

			for i in range(len(notes)-self.order):
				state = tuple(notes[i:i+self.order])
				next_note = notes[i+self.order]

				#tähän trie eli trie.insert(state, next_note)

if __name__ == "__main__":
	t = Train(sys.argv[1], 2)
	print(t.organize_data())
