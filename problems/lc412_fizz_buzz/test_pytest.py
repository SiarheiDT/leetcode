import pytest
from problems.lc412_fizz_buzz.solution import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["1"]),
        (2, ["1", "2"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
              "11", "Fizz", "13", "14", "FizzBuzz"]),
        (16, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
              "11", "Fizz", "13", "14", "FizzBuzz", "16"]),
    ],
)
def test_fizzbuzz_examples(n, expected):
    assert Solution().fizzBuzz(n) == expected


def test_fizzbuzz_output_length():
    n = 30
    out = Solution().fizzBuzz(n)
    assert len(out) == n


def test_validation_type_error():
    with pytest.raises(TypeError):
        Solution().fizzBuzz("15")  # not int


def test_validation_value_error_zero():
    with pytest.raises(ValueError):
        Solution().fizzBuzz(0)


def test_validation_value_error_negative():
    with pytest.raises(ValueError):
        Solution().fizzBuzz(-1)