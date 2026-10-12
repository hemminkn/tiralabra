import unittest
from src.markov_chain import MarkovChain

class TestMarkov(unittest.TestCase):

    def setUp(self):
        self.m = MarkovChain("Minors", 2)

    #test if progressions are right
    def test_train_notes(self):

        self.m.train_notes([60, 62, 64, 65])
        successors, weights = self.m.trie.find_next((60, 62))
        self.assertEqual(successors, [64])

if __name__ == "__main__":
    unittest.main()
