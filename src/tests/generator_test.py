import unittest
from src.trie import Trie
from src.generator import generate
from src.markov_chain import MarkovChain

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.m = MarkovChain("Minors", 2)

    #test if generator generates allowed notes
    def test_generate_notes(self):

        self.m.train_notes([60, 62, 45, 67, 68, 66, 64, 65, 60, 62, 55, 67, 68, 60])

        generated = generate(self.m.trie, "generated_song")

        sequences = []

        for i in range(len(generated)-3):
            sequences.append([generated[i], generated[i+1], generated[i+2]])

        result = 0

        for sequence in sequences:
            if sequence[2] in self.m.trie.find_next((sequence[0], sequence[1]))[0]:
                result += 1

        self.assertEqual(result, len(sequences))

if __name__ == "__main__":
    unittest.main()
