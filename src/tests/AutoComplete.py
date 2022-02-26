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


if __name__ == '__main__':
    unittest.main()
