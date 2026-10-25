import unittest
from flashcards import load_cards, select_cards

class FlashcardTests(unittest.TestCase):
    def test_real_deck_loads(self):
        self.assertGreaterEqual(len(load_cards()), 10)

    def test_cards_have_required_fields(self):
        for card in load_cards():
            self.assertTrue(all(card.get(key) for key in ("topic", "question", "answer")))

    def test_filter_by_topic(self):
        chosen = select_cards(load_cards(), topic="caching", count=10, seed=1)
        self.assertTrue(chosen)
        self.assertTrue(all(card["topic"] == "Caching" for card in chosen))

    def test_deterministic_order(self):
        cards = load_cards()
        self.assertEqual(select_cards(cards, count=6, seed=12), select_cards(cards, count=6, seed=12))

    def test_invalid_topic(self):
        with self.assertRaises(ValueError):
            select_cards(load_cards(), topic="Not a topic")

    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            select_cards(load_cards(), count=0)

if __name__=="__main__":
    unittest.main()
