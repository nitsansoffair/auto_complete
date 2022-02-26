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

if __name__ == '__main__':
    unittest.main()
