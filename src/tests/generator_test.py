import unittest
from src.trie import Trie
from src.generator import generate
from src.markov_chain import MarkovChain

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.m = MarkovChain("Minors", 2)

    #test if generator generates allowed notes
    def test_generate_notes(self):

        self.m.train_notes([60, 62, 64, 65, 67])

        generated = generate(self.m.trie)

        self.assertEqual(generated, [60, 62, 64, 65, 67])

if __name__ == "__main__":
    unittest.main()
