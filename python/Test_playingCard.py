import unittest
from playingCard import generateDeck, shuffleCards

class test_playingCard(unittest.TestCase):

    def test_HA(self):
        self.assertEqual(generateDeck()[0],"HA")

    def test_shuffle(self):
        cards = generateDeck()
        self.assertNotEqual(shuffleCards(cards)[0],"HA")

    def main():
        unittest.main()

if __name__ == "__main__":
    unittest.main()
