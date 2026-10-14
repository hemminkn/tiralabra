import unittest
from src.trie import Trie
from src.generator import generate
from src.markov_chain import MarkovChain

class TestEndToEnd(unittest.TestCase):

    def setUp(self):
        self.m = MarkovChain("Minors", 2)

    #test if the whole process works
    def test_end_to_end(self):

        self.m.train_notes([60, 65, 67, 68, 65, 67, 69, 60, 65, 64, 64, 67])

        generated = generate(self.m.trie)

        self.assertTrue(len(generated)>0)

if __name__ == "__main__":
    unittest.main()
