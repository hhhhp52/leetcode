from problems.algorithms import function
from tests.algorithms import algorithms_dataset as dataset


def test_two_sum():
    data = dataset.get_two_sum_dataset()

    for test in data:
        assert function.two_sum(test.get("nums"), test.get("target")) == test.get("result")


def test_add_two_number():
    data = dataset.get_add_two_number_dataset()

    for test in data:
        assert function.add_two_number(test.get("l1"), test.get("l2")) == test.get("result")


def test_longest_substring_without_repeating_characters():
    data = dataset.get_longest_substring_without_repeating_characters()

    for test in data:
        assert function.longest_substring_without_repeating_characters(test.get("s")) == test.get("result")


def test_string_to_integer():
    data = dataset.get_string_to_integer_dataset()

    for test in data:
        assert function.string_to_integer(test.get("s")) == test.get("result")


def test_roman_to_integer():
    data = dataset.get_roman_to_integer_dataset()

    for test in data:
        assert function.roman_to_integer(test.get("s")) == test.get("result")


def test_longest_common_prefix():
    data = dataset.get_longest_common_prefix_dataset()

    for test in data:
        assert function.longest_common_prefix(test.get("strs")) == test.get("result")


def test_valid_parentheses():
    data = dataset.get_valid_parentheses_dataset()

    for test in data:
        assert function.valid_parentheses(test.get("s")) == test.get("result")

