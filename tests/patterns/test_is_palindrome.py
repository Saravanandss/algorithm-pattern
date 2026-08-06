import pytest

from patterns.is_palindrome import is_palindrome


# -------test_is_palindrome
@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),  # given example
        ("race a car", False),  # given example
        ("Panama", False),  # not a palindrome — expectation re-derived
        ("20man n-am02", True),  # digits participate
        ("", True),  # vacuously true, by convention
        (".,", True),  # all punctuation — the IndexError trap
        ("n", True),  # single char
        ("nn", True),  # even length
        ("a.", True),  # skip drives pointers together
        (".a", True),
        ("0P", False),  # two alnums that differ ('0' vs 'p')
        ("Aa", True),  # case-insensitive
        ("12321", True),  # pure digits
        ("ab,,,,ba c", False),  # punctuation run mid-string
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected

