import unittest

from main import get_keywords, search_chunks


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.chunks = [
            "FORMATO DEI DOCUMENTI\n"
            "Vengono utilizzati documenti di testo.",

            "GESTIONE DELLE FONTI\n"
            "Le risposte devono indicare le fonti utilizzate.",
        ]

    def test_finds_document_format(self):
        result = search_chunks(
            "Quali documenti vengono utilizzati?",
            self.chunks,
        )

        self.assertIsNotNone(result)
        index, chunk, shared_words = result

        self.assertEqual(index, 1)
        self.assertIn("documenti di testo", chunk)
        self.assertIn("documenti", shared_words)

    def test_finds_sources(self):
        result = search_chunks(
            "Come vengono gestite le fonti?",
            self.chunks,
        )

        self.assertIsNotNone(result)
        self.assertEqual(result[0], 2)

    def test_returns_none_without_matching_words(self):
        result = search_chunks("Quanto costa?", self.chunks)

        self.assertIsNone(result)

    def test_ignores_case_and_punctuation(self):
        self.assertEqual(
            get_keywords("DOCUMENTI!"),
            get_keywords("documenti"),
        )


if __name__ == "__main__":
    unittest.main()