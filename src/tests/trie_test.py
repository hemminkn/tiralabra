import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    #test if trie's structure is correct
    def test_trie_structure(self):

        self.trie.insert((60, 61), 62)
        self.trie.insert((60, 63), 66)
        self.trie.insert((60, 63), 65)
        self.trie.insert((62, 64), 65)
        self.trie.insert((62, 64), 64)
        self.trie.insert((62, 63), 60)
        self.trie.insert((62, 63), 61)
        self.trie.insert((63, 66), 61)
        self.trie.insert((63, 66), 62)
        self.trie.insert((63, 64), 65)

        #10 60 3 61 1 62 1 63 2 66 1 65 1
        #62 4 64 2 65 1 64 1 63 2 60 1 61 1
        #63 3 66 2 61 1 62 1 64 1 65 1

        def tree_traversal(self):
            result = []

            def dfs(node):
                for note, child in node.children.items():
                    result.append((note, child.frequency))
                    dfs(child)

            dfs(self.root)

            result = self.trie.tree_traversal()

            self.assertEqual([result, [10, 60, 3, 61, 1, 62, 1, 63, 2, 66, 1, 65, 1, 62, 4, 64, 2, 65, 1, 64, 1, 63, 2, 60, 1, 61, 1, 63, 3, 66, 2, 61, 1, 62, 1, 64, 1, 65, 1]])

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

    #test what happens when state is unknown/no successors
    def test_with_unknown_state(self):

        result = self.trie.find_next((1, 2))

        self.assertEqual(result, ([], []))

    #test if start states are correct
    def test_start_states(self):

        self.trie.start_states.append((60, 62))

        self.assertEqual(self.trie.start_states[0], (60, 62))

if __name__ == "__main__":
    unittest.main()
