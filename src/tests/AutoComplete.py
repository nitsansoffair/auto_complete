import unittest

from src.AutoComplete import AutoComplete


class AutoCompleteTest(unittest.TestCase):
    def test_split_to_sentences(self):
        auto_complete = AutoComplete()
        target = auto_complete.split_to_sentences
        test_cases = [
            {
                "name": "default_check",
                "input": "I have a pen.\nI have an apple. \nAh\nApple pen.\n",
                "expected": ["I have a pen.", "I have an apple.", "Ah", "Apple pen."],
            },
            {
                "name": "twitter_check",
                "input": """
                Exhaust leak! arrrgh\ni Love Reading your magazine (: it always cheers me up\nTables are all sold out for the Mystique Masquerade Ball.\n
                """,
                "expected": [
                    "Exhaust leak! arrrgh",
                    "i Love Reading your magazine (: it always cheers me up",
                    "Tables are all sold out for the Mystique Masquerade Ball.",
                ],
            },
            {"name": "space_null_check", "input": """ \n \n\n\n""", "expected": [], },
            {
                "name": "small_check",
                "input": """a\n  b\n\n\n. """,
                "expected": ["a", "b", "."],
            },
        ]
        for test_case in test_cases:
            result = target(test_case["input"])
            self.assertEqual(True, isinstance(result, type(test_case["expected"])))
            self.assertEqual(True, result == test_case["expected"])
            if test_case["name"] == "space_null_check":
                self.assertEqual(True, len(result) == 0)
            if test_case["name"] == "space_null_check":
                self.assertEqual(True, len(result) == 0)
            if test_case["name"] == "small_check":
                for elem in result:
                    self.assertEqual(True, len(elem) == 1)

    def test_tokenize_sentences(self):
        auto_complete = AutoComplete()
        target = auto_complete.tokenize_sentences
        test_cases = [
            {
                "name": "notebook example",
                "input": ["Sky is blue.", "Leaves are green.", "Roses are red."],
                "expected": [
                    ["sky", "is", "blue", "."],
                    ["leaves", "are", "green", "."],
                    ["roses", "are", "red", "."],
                ],
            },
            {"name": "no sentence", "input": [], "expected": []},
            {
                "name": "one sentence with ;",
                "input": ["Grass is greener;"],
                "expected": [["grass", "is", "greener", ";"]],
            },
            {
                "name": "two sentences, one in CAPS",
                "input": ["Space if infinite.", "OR IS IT?"],
                "expected": [["space", "if", "infinite", "."], ["or", "is", "it", "?"]],
            },
            {
                "name": "Sentence with empty string",
                "input": ["Next sentence is empty string.", "", "This one is not empty."],
                "expected": [
                    ["next", "sentence", "is", "empty", "string", "."],
                    [],
                    ["this", "one", "is", "not", "empty", "."],
                ],
            },
            {
                "name": "Sentence with space",
                "input": ["Next sentence is full of spaces.", "   ", "This one is full."],
                "expected": [
                    ["next", "sentence", "is", "full", "of", "spaces", "."],
                    [],
                    ["this", "one", "is", "full", "."],
                ],
            },
            {
                "name": "long sentence",
                "input": [
                    "Really really long sentence. It is very long indeed; so long..."
                ],
                "expected": [
                    [
                        "really",
                        "really",
                        "long",
                        "sentence",
                        ".",
                        "it",
                        "is",
                        "very",
                        "long",
                        "indeed",
                        ";",
                        "so",
                        "long",
                        "...",
                    ]
                ],
            },
        ]
        for test_case in test_cases:
            result = target(test_case["input"])
            self.assertEqual(True, isinstance(result, type(test_case["expected"])))
            self.assertEqual(True, len(result) == len(test_case["expected"]))
            self.assertEqual(True, test_case["expected"] == result)

    def test_get_tokenized_data(self):
        auto_complete = AutoComplete()
        target = auto_complete.get_tokenized_data
        test_cases = [
            {
                "name": "default_check",
                "input": "Sky is blue.\nLeaves are green\nRoses are red.",
                "expected": [
                    ["sky", "is", "blue", "."],
                    ["leaves", "are", "green"],
                    ["roses", "are", "red", "."],
                ],
            },
            {
                "name": "spaces_check",
                "input": "   Sky   is  blue.   \nLeaves are green.\nSpace  if  Infinite.\nOR IS IT?\n\n   \nLast sentence .\n",
                "expected": [
                    ["sky", "is", "blue", "."],
                    ["leaves", "are", "green", "."],
                    ["space", "if", "infinite", "."],
                    ["or", "is", "it", "?"],
                    ["last", "sentence", "."],
                ],
            },
        ]
        for test_case in test_cases:
            result = target(test_case["input"])
            self.assertEqual(True, isinstance(result, type(test_case["expected"])))
            self.assertEqual(True, len(result) == len(test_case["expected"]))
            self.assertEqual(True, result == test_case["expected"])

    def test_count_words(self):
        auto_complete = AutoComplete()
        target = auto_complete.count_words
        test_cases = [
            {
                "name": "default_check",
                "input": [
                    ["sky", "is", "blue", "."],
                    ["leaves", "are", "green", "."],
                    ["roses", "are", "red", "."],
                ],
                "expected": {
                    "sky": 1,
                    "is": 1,
                    "blue": 1,
                    ".": 3,
                    "leaves": 1,
                    "are": 2,
                    "green": 1,
                    "roses": 1,
                    "red": 1,
                },
            },
            {
                "name": "larger_check",
                "input": [
                    ["sky", "is", "blue", "."],
                    ["leaves", "are", "green", "."],
                    ["space", "is", "infinite", "."],
                    ["or", "is", "it", "?"],
                    ["last", "sentence", "?", ",", "no"],
                    ["in", "sunset", "sky", "is", "red"],
                ],
                "expected": {
                    "sky": 2,
                    "is": 4,
                    "blue": 1,
                    ".": 3,
                    "leaves": 1,
                    "are": 1,
                    "green": 1,
                    "space": 1,
                    "infinite": 1,
                    "or": 1,
                    "it": 1,
                    "?": 2,
                    "last": 1,
                    "sentence": 1,
                    ",": 1,
                    "no": 1,
                    "in": 1,
                    "sunset": 1,
                    "red": 1,
                },
            },
        ]
        for test_case in test_cases:
            result = target(test_case["input"])
            self.assertEqual(True, isinstance(result, dict))
            self.assertEqual(True, result == test_case["expected"])

    def test_get_words_with_nplus_frequency(self):
        auto_complete = AutoComplete()
        target = auto_complete.get_words_with_nplus_frequency
        test_cases = [
            {
                "name": "default_check",
                "input": {
                    "tokenized_sentences": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["roses", "are", "red", "."],
                    ],
                    "count_threshold": 2,
                },
                "expected": [".", "are"],
            },
            {
                "name": "long_check",
                "input": {
                    "tokenized_sentences": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["space", "is", "infinite", "."],
                        ["or", "is", "it", "?"],
                        ["last", "sentence", "?", ",", "no"],
                        ["in", "sunset", "sky", "is", "red"],
                    ],
                    "count_threshold": 2,
                },
                "expected": ["sky", "is", ".", "?"],
            },
            {
                "name": "threshold_check",
                "input": {
                    "tokenized_sentences": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["space", "is", "infinite", "."],
                        ["or", "is", "it", "?"],
                        ["last", "sentence", "?", ",", "no"],
                        ["in", "sunset", "sky", "is", "red"],
                    ],
                    "count_threshold": 4,
                },
                "expected": ["is"],
            },
        ]
        for test_case in test_cases:
            result = target(**test_case["input"])
            self.assertEqual(True, isinstance(result, type(test_case["expected"])))
            self.assertEqual(True, len(result) == len(test_case["expected"]))
            self.assertEqual(True, result == test_case["expected"])

if __name__ == '__main__':
    unittest.main()
