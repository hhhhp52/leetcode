from problems.algorithms import function
from tests.algorithms import algorithms_dataset as dataset


def test_two_sum():
    data = dataset.get_two_sum_dataset()

    for test in data:
        assert function.two_sum(test.get("nums"), test.get("target")) == test.get("result")
