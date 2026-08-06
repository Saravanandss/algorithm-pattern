import pytest

from patterns.longest_substring import longest_substring


# -------longest_substring
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("a", 1),
        ("", 0),
        ("ab", 2),
    ],
)
def test_longest_substring(s, expected):
    assert longest_substring(s) == expected