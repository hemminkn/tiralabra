from collections import Counter

Class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0
        self.next_notes = Counter()

Class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, state, next_note):
        current = self.root

        for note in state:
            if note not in current.children:
                current.children[note] = TrieNode()

            current = current.children[note]

        current.next_notes[next_note] += 1

    def find_next():
        pass
