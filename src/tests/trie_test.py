import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    #test if inserting creates a path in trie
    def test_insert_makes_path(self):

        self.trie.insert((60, 62), 64)

        self.assertIn(60, self.trie.root.children)

        node = self.trie.root.children[60]

        self.assertIn(62, node.children)

    #test if frequency updates when adding the same sequence
    def test_frequency_updates(self):

        self.trie.insert((60, 62), 64)
        self.trie.insert((60, 62), 64)

        node = self.trie.root.children[60].children[62]

        self.assertEqual(node.next_notes[64], 2)

    #test if multiple successors are shown correctly
    def test_multiple_successors(self):

        self.trie.insert((60, 62), 64)
        self.trie.insert((60, 62), 67)

        node = self.trie.root.children[60].children[62]

        self.assertEqual(node.next_notes[64], 1)
        self.assertEqual(node.next_notes[67], 1)

    #test if trie returns all successors and their weights
    def test_find_next(self):

        self.trie.insert((60, 62), 64)
        self.trie.insert((60, 62), 64)
        self.trie.insert((60, 62), 67)

        successors, weights = self.trie.find_next((60, 62))

        self.assertEqual(set(successors), {64, 67})
        self.assertEqual(set(weights), {2, 1})

    #test what happens when state is unknown/np successors
    def test_without_successors(self):

        result = self.trie.find_next((1, 2))

        self.assertEqual(result, ([], []))

    #test if start states are correct
    def test_start_states(self):

        self.trie.start_states.append((60, 62))

        self.assertEqual(self.trie.start_states[0], (60, 62))

if __name__ == "__main__":
    unittest.main()
