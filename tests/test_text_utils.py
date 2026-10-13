import unittest

from text_utils import parse_duration, slugify, word_count


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


class ParseDurationTests(unittest.TestCase):
    def test_supplied_examples(self):
        for text, expected in (
            ("90s", 90),
            ("2m", 120),
            ("1h30m", 5400),
            ("1h30m15s", 5415),
        ):
            with self.subTest(text=text):
                result = parse_duration(text)
                self.assertEqual(result, expected)
                self.assertIsInstance(result, int)

    def test_individual_units_and_optional_components(self):
        for text, expected in (
            ("1h", 3600),
            ("15s", 15),
            ("30m15s", 1815),
            ("1h15s", 3615),
            ("120m", 7200),
        ):
            with self.subTest(text=text):
                self.assertEqual(parse_duration(text), expected)

    def test_invalid_input_has_clear_error(self):
        for text in ("", "abc", "5x", "-5m", "5d", "5ms", "30", "1h-5m"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "Invalid duration"):
                    parse_duration(text)

    def test_valid_prefix_does_not_hide_invalid_text(self):
        for text in ("90sabc", "1h30m5x", "1h30m15s!", "abc90s", "90s\n"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "Invalid duration"):
                    parse_duration(text)


class WordCountTests(unittest.TestCase):
    def test_case_insensitive(self):
        self.assertEqual(word_count("The the THE"), {"the": 3})

    def test_ignores_punctuation(self):
        self.assertEqual(word_count("Hello, hello!"), {"hello": 2})

    def test_preserves_internal_apostrophe(self):
        self.assertEqual(word_count("don't"), {"don't": 1})

    def test_empty_input(self):
        self.assertEqual(word_count(""), {})

    def test_punctuation_separates_distinct_words(self):
        self.assertEqual(
            word_count("hello,world!hello/world.good-day"),
            {"hello": 2, "world": 2, "good": 1, "day": 1},
        )

    def test_only_internal_apostrophes_are_preserved(self):
        self.assertEqual(
            word_count("'Don't' DON'T rock'n'roll"),
            {"don't": 2, "rock'n'roll": 1},
        )

    def test_only_punctuation_or_whitespace(self):
        for text in (" \t\n ", "!.,--'''?"):
            with self.subTest(text=text):
                self.assertEqual(word_count(text), {})


if __name__ == "__main__":
    unittest.main()
