from collections import Counter
import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0
        self.next_notes = Counter()

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.start_states = []

    def insert(self, state, next_note):
        current = self.root

        for note in state:
            if note not in current.children:
                current.children[note] = TrieNode()

            current = current.children[note]

            current.frequency += 1

        current.next_notes[next_note] += 1

    def find_next(self, state):
        current = self.root

        for note in state:
            if note in current.children:
                current = current.children[note]
            else:
                return ([], [])

        successors = []
        weights = []

        for note in current.next_notes:
            successors.append(note)
            weights.append(current.next_notes[note])

        return (successors, weights)

if __name__ == "__main__":
    trie = Trie()
    trie.insert((60, 62), 64)
    trie.insert((61, 63), 65)
    print(trie.find_next((60, 62)))
