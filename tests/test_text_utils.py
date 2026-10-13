import unittest

from text_utils import slugify


class SlugifyTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_lowercases_letters_and_preserves_digits(self):
        self.assertEqual(slugify("ABC123"), "abc123")

    def test_collapses_separator_runs(self):
        for text in ("a__ !!b", "a---b", "a \t\n b", "a/.b"):
            with self.subTest(text=text):
                self.assertEqual(slugify(text), "a-b")

    def test_replaces_multiple_separator_runs(self):
        self.assertEqual(slugify("a/b.c"), "a-b-c")

    def test_trims_leading_and_trailing_separators(self):
        self.assertEqual(slugify(" --Hi-- "), "hi")

    def test_empty_input(self):
        self.assertEqual(slugify(""), "")

    def test_only_symbols_or_whitespace(self):
        for text in ("!@#$", "---", " \t\n "):
            with self.subTest(text=text):
                self.assertEqual(slugify(text), "")

    def test_preserves_existing_slugs_and_digits(self):
        for text in ("hello-world", "abc123", "123", "a"):
            with self.subTest(text=text):
                self.assertEqual(slugify(text), text)


if __name__ == "__main__":
    unittest.main()
