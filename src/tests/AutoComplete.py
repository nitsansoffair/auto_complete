import unittest

import numpy as np

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

    def test_replace_oov_words_by_unk(self):
        auto_complete = AutoComplete()
        target = auto_complete.replace_oov_words_by_unk
        test_cases = [
            {
                "name": "default_check",
                "input": {
                    "tokenized_sentences": [["dogs", "run"], ["cats", "sleep"]],
                    "vocabulary": ["dogs", "sleep"],
                    "unknown_token": "<unk>",
                },
                "expected": {
                    "expected_list": [["dogs", "<unk>"], ["<unk>", "sleep"]],
                    "expected_count_unk": 2,
                },
            },
            {
                "name": "unk_check",
                "input": {
                    "tokenized_sentences": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["space", "is", "infinite", "?"],
                        ["in", "sunset", "sky", "is", "red"],
                    ],
                    "vocabulary": [
                        "sky",
                        "is",
                        "blue",
                        "are",
                        ".",
                        "space",
                        "infinite",
                        "red",
                    ],
                    "unknown_token": "-1",
                },
                "expected": {
                    "expected_list": [
                        ["sky", "is", "blue", "."],
                        ["-1", "are", "-1", "."],
                        ["space", "is", "infinite", "-1"],
                        ["-1", "-1", "sky", "is", "red"],
                    ],
                    "expected_count_unk": 5,
                },
            },
        ]
        for test_case in test_cases:
            result = target(**test_case["input"])
            self.assertEqual(True, isinstance(result, type(test_case["expected"]["expected_list"])))
            count_unk_result = 0
            for elem in result:
                if test_case["input"]["unknown_token"] in elem:
                    count_unk_result += elem.count(test_case["input"]["unknown_token"])
            self.assertEqual(True, count_unk_result == test_case["expected"]["expected_count_unk"])
            self.assertEqual(True, result == test_case["expected"]["expected_list"])

    def test_preprocess_data(self):
        auto_complete = AutoComplete()
        target = auto_complete.preprocess_data
        test_cases = [
            {
                "name": "default_check",
                "input": {
                    "train_data": [["sky", "is", "blue", "."], ["leaves", "are", "green"]],
                    "test_data": [["roses", "are", "red", "."]],
                    "count_threshold": 1,
                    "unknown_token": "<unk>",
                },
                "expected": {
                    "train_data_replaced": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green"],
                    ],
                    "test_data_replaced": [["<unk>", "are", "<unk>", "."]],
                    "vocabulary": ["sky", "is", "blue", ".", "leaves", "are", "green"],
                    "unk_count_train": 0,
                    "unk_count_test": 2,
                },
            },
            {
                "name": "larger_check",
                "input": {
                    "train_data": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["space", "is", "infinite", "?"],
                        ["in", "sunset", "sky", "is", "red"],
                    ],
                    "test_data": [
                        ["cats", "are", "animals", "."],
                        ["is", "the", "dog", "red", "?"],
                    ],
                    "count_threshold": 1,
                    "unknown_token": "-1",
                },
                "expected": {
                    "train_data_replaced": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["space", "is", "infinite", "?"],
                        ["in", "sunset", "sky", "is", "red"],
                    ],
                    "test_data_replaced": [
                        ["-1", "are", "-1", "."],
                        ["is", "-1", "-1", "red", "?"],
                    ],
                    "vocabulary": [
                        "sky",
                        "is",
                        "blue",
                        ".",
                        "leaves",
                        "are",
                        "green",
                        "space",
                        "infinite",
                        "?",
                        "in",
                        "sunset",
                        "red",
                    ],
                    "unk_count_train": 0,
                    "unk_count_test": 4,
                },
            },
            {
                "name": "threshold_check",
                "input": {
                    "train_data": [
                        ["sky", "is", "blue", "."],
                        ["leaves", "are", "green", "."],
                        ["space", "is", "infinite", "?"],
                        ["in", "sunset", "sky", "is", "red"],
                    ],
                    "test_data": [
                        ["cats", "are", "animals", "."],
                        ["is", "the", "dog", "red", "?"],
                    ],
                    "count_threshold": 2,
                    "unknown_token": "0",
                },
                "expected": {
                    "train_data_replaced": [
                        ["sky", "is", "0", "."],
                        ["0", "0", "0", "."],
                        ["0", "is", "0", "0"],
                        ["0", "0", "sky", "is", "0"],
                    ],
                    "test_data_replaced": [
                        ["0", "0", "0", "."],
                        ["is", "0", "0", "0", "0"],
                    ],
                    "vocabulary": ["sky", "is", "."],
                    "unk_count_train": 10,
                    "unk_count_test": 7,
                },
            },
        ]
        for test_case in test_cases:
            result = target(**test_case["input"])
            for elem in result:
                self.assertEqual(True, isinstance(elem, list))
            count_unk_result = 0
            for elem in result[0]:
                if test_case["input"]["unknown_token"] in elem:
                    count_unk_result += elem.count(test_case["input"]["unknown_token"])
            self.assertEqual(True, count_unk_result == test_case["expected"]["unk_count_train"])
            count_unk_result = 0
            for elem in result[1]:
                if test_case["input"]["unknown_token"] in elem:
                    count_unk_result += elem.count(test_case["input"]["unknown_token"])
            self.assertEqual(count_unk_result, test_case["expected"]["unk_count_test"])
            self.assertEqual(True, len(result[2]) == len(test_case["expected"]["vocabulary"]))

    def test_count_n_grams(self):
        auto_complete = AutoComplete()
        target = auto_complete.count_n_grams
        test_cases = [
            {
                "name": "default_check_1",
                "input": {
                    "data": [
                        ["i", "like", "a", "cat"],
                        ["this", "dog", "is", "like", "a", "cat"],
                    ],
                    "n": 1,
                    "start_token": "<s>",
                    "end_token": "<e>",
                },
                "expected": {
                    ("<s>",): 2,
                    ("i",): 1,
                    ("like",): 2,
                    ("a",): 2,
                    ("cat",): 2,
                    ("<e>",): 2,
                    ("this",): 1,
                    ("dog",): 1,
                    ("is",): 1,
                },
            },
            {
                "name": "default_check_2",
                "input": {
                    "data": [
                        ["i", "like", "a", "cat"],
                        ["this", "dog", "is", "like", "a", "cat"],
                    ],
                    "n": 2,
                    "start_token": "<s>",
                    "end_token": "<e>",
                },
                "expected": {
                    ("<s>", "<s>"): 2,
                    ("<s>", "i"): 1,
                    ("i", "like"): 1,
                    ("like", "a"): 2,
                    ("a", "cat"): 2,
                    ("cat", "<e>"): 2,
                    ("<s>", "this"): 1,
                    ("this", "dog"): 1,
                    ("dog", "is"): 1,
                    ("is", "like"): 1,
                },
            },
            {
                "name": "large_check",
                "input": {
                    "data": [
                        ["in", "sunset", "sky", "is", "red"],
                        ["i", "like", "a", "cat"],
                        ["this", "dog", "is", "like", "a", "cat"],
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
                        ],
                    ],
                    "n": 3,
                    "start_token": "-1",
                    "end_token": "-2",
                },
                "expected": {
                    ("-1", "-1", "-1"): 4,
                    ("-1", "-1", "in"): 1,
                    ("-1", "in", "sunset"): 1,
                    ("in", "sunset", "sky"): 1,
                    ("sunset", "sky", "is"): 1,
                    ("sky", "is", "red"): 1,
                    ("is", "red", "-2"): 1,
                    ("-1", "-1", "i"): 1,
                    ("-1", "i", "like"): 1,
                    ("i", "like", "a"): 1,
                    ("like", "a", "cat"): 2,
                    ("a", "cat", "-2"): 2,
                    ("-1", "-1", "this"): 1,
                    ("-1", "this", "dog"): 1,
                    ("this", "dog", "is"): 1,
                    ("dog", "is", "like"): 1,
                    ("is", "like", "a"): 1,
                    ("-1", "-1", "really"): 1,
                    ("-1", "really", "really"): 1,
                    ("really", "really", "long"): 1,
                    ("really", "long", "sentence"): 1,
                    ("long", "sentence", "."): 1,
                    ("sentence", ".", "it"): 1,
                    (".", "it", "is"): 1,
                    ("it", "is", "very"): 1,
                    ("is", "very", "long"): 1,
                    ("very", "long", "indeed"): 1,
                    ("long", "indeed", ";"): 1,
                    ("indeed", ";", "so"): 1,
                    (";", "so", "long"): 1,
                    ("so", "long", "..."): 1,
                    ("long", "...", "-2"): 1,
                },
            },
        ]
        for test_case in test_cases:
            result = target(**test_case["input"])
            self.assertEqual(True, isinstance(result, dict))
            self.assertEqual(result, test_case["expected"])

    def test_estimate_probability(self):
        auto_complete = AutoComplete()
        target = auto_complete.estimate_probability
        test_cases = [
            {
                "name": "default_check",
                "input": {
                    "word": "cat",
                    "previous_n_gram": "a",
                    "n_gram_counts": {
                        ("<s>",): 2,
                        ("i",): 1,
                        ("like",): 2,
                        ("a",): 2,
                        ("cat",): 2,
                        ("<e>",): 2,
                        ("this",): 1,
                        ("dog",): 1,
                        ("is",): 1,
                    },
                    "n_plus1_gram_counts": {
                        ("<s>", "<s>"): 2,
                        ("<s>", "i"): 1,
                        ("i", "like"): 1,
                        ("like", "a"): 2,
                        ("a", "cat"): 2,
                        ("cat", "<e>"): 2,
                        ("<s>", "this"): 1,
                        ("this", "dog"): 1,
                        ("dog", "is"): 1,
                        ("is", "like"): 1,
                    },
                    "vocabulary_size": 7,
                    "k": 1,
                },
                "expected": 0.3333333333333333,
            },
            {
                "name": "larger_check",
                "input": {
                    "word": "i",
                    "previous_n_gram": "like",
                    "n_gram_counts": {
                        ("-1", "-1"): 4,
                        ("-1", "in"): 1,
                        ("in", "sunset"): 1,
                        ("sunset", "sky"): 1,
                        ("sky", "is"): 1,
                        ("is", "red"): 1,
                        ("red", "-2"): 1,
                        ("-1", "i"): 1,
                        ("i", "like"): 1,
                        ("like", "a"): 2,
                        ("a", "cat"): 2,
                        ("cat", "-2"): 2,
                        ("-1", "this"): 1,
                        ("this", "dog"): 1,
                        ("dog", "is"): 1,
                        ("is", "like"): 1,
                        ("-1", "really"): 1,
                        ("really", "really"): 1,
                        ("really", "long"): 1,
                        ("long", "sentence"): 1,
                        ("sentence", "."): 1,
                        (".", "it"): 1,
                        ("it", "is"): 1,
                        ("is", "very"): 1,
                        ("very", "long"): 1,
                        ("long", "indeed"): 1,
                        ("indeed", ";"): 1,
                        (";", "so"): 1,
                        ("so", "long"): 1,
                        ("long", "..."): 1,
                        ("...", "-2"): 1,
                    },
                    "n_plus1_gram_counts": {
                        ("-1", "-1", "-1"): 4,
                        ("-1", "-1", "in"): 1,
                        ("-1", "in", "sunset"): 1,
                        ("in", "sunset", "sky"): 1,
                        ("sunset", "sky", "is"): 1,
                        ("sky", "is", "red"): 1,
                        ("is", "red", "-2"): 1,
                        ("-1", "-1", "i"): 1,
                        ("-1", "i", "like"): 1,
                        ("i", "like", "a"): 1,
                        ("like", "a", "cat"): 2,
                        ("a", "cat", "-2"): 2,
                        ("-1", "-1", "this"): 1,
                        ("-1", "this", "dog"): 1,
                        ("this", "dog", "is"): 1,
                        ("dog", "is", "like"): 1,
                        ("is", "like", "a"): 1,
                        ("-1", "-1", "really"): 1,
                        ("-1", "really", "really"): 1,
                        ("really", "really", "long"): 1,
                        ("really", "long", "sentence"): 1,
                        ("long", "sentence", "."): 1,
                        ("sentence", ".", "it"): 1,
                        (".", "it", "is"): 1,
                        ("it", "is", "very"): 1,
                        ("is", "very", "long"): 1,
                        ("very", "long", "indeed"): 1,
                        ("long", "indeed", ";"): 1,
                        ("indeed", ";", "so"): 1,
                        (";", "so", "long"): 1,
                        ("so", "long", "..."): 1,
                        ("long", "...", "-2"): 1,
                    },
                    "vocabulary_size": 21,
                    "k": 2,
                },
                "expected": 0.047619047619047616,
            },
        ]
        for test_case in test_cases:
            result = target(**test_case["input"])
            self.assertEqual(True, np.isclose(result, test_case["expected"]))

    def test_calculate_perplexity(self):
        auto_complete = AutoComplete()
        target = auto_complete.calculate_perplexity
        test_cases = [
            {
                "name": "default_check_train",
                "input": {
                    "sentence": ["i", "like", "a", "cat"],
                    "n_gram_counts": {
                        ("<s>",): 2,
                        ("i",): 1,
                        ("like",): 2,
                        ("a",): 2,
                        ("cat",): 2,
                        ("<e>",): 2,
                        ("this",): 1,
                        ("dog",): 1,
                        ("is",): 1,
                    },
                    "n_plus1_gram_counts": {
                        ("<s>", "<s>"): 2,
                        ("<s>", "i"): 1,
                        ("i", "like"): 1,
                        ("like", "a"): 2,
                        ("a", "cat"): 2,
                        ("cat", "<e>"): 2,
                        ("<s>", "this"): 1,
                        ("this", "dog"): 1,
                        ("dog", "is"): 1,
                        ("is", "like"): 1,
                    },
                    "vocabulary_size": 7,
                    "start_token": "<s>",
                    "end_token": "<e>",
                    "k": 1.0,
                },
                "expected": 2.8039657955522013,
            },
            {
                "name": "default_check_test",
                "input": {
                    "sentence": ["i", "like", "a", "dog"],
                    "n_gram_counts": {
                        ("<s>",): 2,
                        ("i",): 1,
                        ("like",): 2,
                        ("a",): 2,
                        ("cat",): 2,
                        ("<e>",): 2,
                        ("this",): 1,
                        ("dog",): 1,
                        ("is",): 1,
                    },
                    "n_plus1_gram_counts": {
                        ("<s>", "<s>"): 2,
                        ("<s>", "i"): 1,
                        ("i", "like"): 1,
                        ("like", "a"): 2,
                        ("a", "cat"): 2,
                        ("cat", "<e>"): 2,
                        ("<s>", "this"): 1,
                        ("this", "dog"): 1,
                        ("dog", "is"): 1,
                        ("is", "like"): 1,
                    },
                    "vocabulary_size": 7,
                    "start_token": "<s>",
                    "end_token": "<e>",
                    "k": 1.0,
                },
                "expected": 3.965406456500188,
            },
            {
                "name": "larger_check_train",
                "input": {
                    "sentence": ["in", "sunset", "sky", "is", "red"],
                    "n_gram_counts": {
                        ("-1", "-1"): 4,
                        ("-1", "in"): 1,
                        ("in", "sunset"): 1,
                        ("sunset", "sky"): 1,
                        ("sky", "is"): 1,
                        ("is", "red"): 1,
                        ("red", "-2"): 1,
                        ("-1", "i"): 1,
                        ("i", "like"): 1,
                        ("like", "a"): 2,
                        ("a", "cat"): 2,
                        ("cat", "-2"): 2,
                        ("-1", "this"): 1,
                        ("this", "dog"): 1,
                        ("dog", "is"): 1,
                        ("is", "like"): 1,
                        ("-1", "really"): 1,
                        ("really", "really"): 1,
                        ("really", "long"): 1,
                        ("long", "sentence"): 1,
                        ("sentence", "."): 1,
                        (".", "it"): 1,
                        ("it", "is"): 1,
                        ("is", "very"): 1,
                        ("very", "long"): 1,
                        ("long", "indeed"): 1,
                        ("indeed", ";"): 1,
                        (";", "so"): 1,
                        ("so", "long"): 1,
                        ("long", "..."): 1,
                        ("...", "-2"): 1,
                    },
                    "n_plus1_gram_counts": {
                        ("-1", "-1", "-1"): 4,
                        ("-1", "-1", "in"): 1,
                        ("-1", "in", "sunset"): 1,
                        ("in", "sunset", "sky"): 1,
                        ("sunset", "sky", "is"): 1,
                        ("sky", "is", "red"): 1,
                        ("is", "red", "-2"): 1,
                        ("-1", "-1", "i"): 1,
                        ("-1", "i", "like"): 1,
                        ("i", "like", "a"): 1,
                        ("like", "a", "cat"): 2,
                        ("a", "cat", "-2"): 2,
                        ("-1", "-1", "this"): 1,
                        ("-1", "this", "dog"): 1,
                        ("this", "dog", "is"): 1,
                        ("dog", "is", "like"): 1,
                        ("is", "like", "a"): 1,
                        ("-1", "-1", "really"): 1,
                        ("-1", "really", "really"): 1,
                        ("really", "really", "long"): 1,
                        ("really", "long", "sentence"): 1,
                        ("long", "sentence", "."): 1,
                        ("sentence", ".", "it"): 1,
                        (".", "it", "is"): 1,
                        ("it", "is", "very"): 1,
                        ("is", "very", "long"): 1,
                        ("very", "long", "indeed"): 1,
                        ("long", "indeed", ";"): 1,
                        ("indeed", ";", "so"): 1,
                        (";", "so", "long"): 1,
                        ("so", "long", "..."): 1,
                        ("long", "...", "-2"): 1,
                    },
                    "vocabulary_size": 21,
                    "start_token": "-1",
                    "end_token": "-2",
                    "k": 1,
                },
                "expected": 6.137396479150367,
            },
            {
                "name": "larger_check_test",
                "input": {
                    "sentence": ["i", "like", "a", "cat"],
                    "n_gram_counts": {
                        ("-1", "-1"): 4,
                        ("-1", "in"): 1,
                        ("in", "sunset"): 1,
                        ("sunset", "sky"): 1,
                        ("sky", "is"): 1,
                        ("is", "red"): 1,
                        ("red", "-2"): 1,
                        ("-1", "i"): 1,
                        ("i", "like"): 1,
                        ("like", "a"): 2,
                        ("a", "cat"): 2,
                        ("cat", "-2"): 2,
                        ("-1", "this"): 1,
                        ("this", "dog"): 1,
                        ("dog", "is"): 1,
                        ("is", "like"): 1,
                        ("-1", "really"): 1,
                        ("really", "really"): 1,
                        ("really", "long"): 1,
                        ("long", "sentence"): 1,
                        ("sentence", "."): 1,
                        (".", "it"): 1,
                        ("it", "is"): 1,
                        ("is", "very"): 1,
                        ("very", "long"): 1,
                        ("long", "indeed"): 1,
                        ("indeed", ";"): 1,
                        (";", "so"): 1,
                        ("so", "long"): 1,
                        ("long", "..."): 1,
                        ("...", "-2"): 1,
                    },
                    "n_plus1_gram_counts": {
                        ("-1", "-1", "-1"): 4,
                        ("-1", "-1", "in"): 1,
                        ("-1", "in", "sunset"): 1,
                        ("in", "sunset", "sky"): 1,
                        ("sunset", "sky", "is"): 1,
                        ("sky", "is", "red"): 1,
                        ("is", "red", "-2"): 1,
                        ("-1", "-1", "i"): 1,
                        ("-1", "i", "like"): 1,
                        ("i", "like", "a"): 1,
                        ("like", "a", "cat"): 2,
                        ("a", "cat", "-2"): 2,
                        ("-1", "-1", "this"): 1,
                        ("-1", "this", "dog"): 1,
                        ("this", "dog", "is"): 1,
                        ("dog", "is", "like"): 1,
                        ("is", "like", "a"): 1,
                        ("-1", "-1", "really"): 1,
                        ("-1", "really", "really"): 1,
                        ("really", "really", "long"): 1,
                        ("really", "long", "sentence"): 1,
                        ("long", "sentence", "."): 1,
                        ("sentence", ".", "it"): 1,
                        (".", "it", "is"): 1,
                        ("it", "is", "very"): 1,
                        ("is", "very", "long"): 1,
                        ("very", "long", "indeed"): 1,
                        ("long", "indeed", ";"): 1,
                        ("indeed", ";", "so"): 1,
                        (";", "so", "long"): 1,
                        ("so", "long", "..."): 1,
                        ("long", "...", "-2"): 1,
                    },
                    "vocabulary_size": 21,
                    "start_token": "-1",
                    "end_token": "-2",
                    "k": 1,
                },
                "expected": 5.0931554910158665,
            },
        ]
        for test_case in test_cases:
            result = target(**test_case["input"])
            self.assertEqual(True, np.isclose(result, test_case["expected"]))

if __name__ == '__main__':
    unittest.main()
