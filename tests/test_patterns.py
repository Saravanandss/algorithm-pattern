"""Tests for the pattern drills.

House rule: every case is an (input, expected) pair — expectations are
written down, never held in the head. Suites deliberately include inputs
that exit loops in unexpected ways, because that is where the bugs lived.
"""

import pytest

from dp.climbing_stairs import climbing_stairs
from patterns.is_palindrome import is_palindrome
from patterns.longest_substring import longest_substring
from patterns.product_of_array import product_of_array, product_of_array_v2
from patterns.remove_duplicates import remove_duplicates
from patterns.subarray_sum import subarray_sum


#-------subarray_sum
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3], 3, 2),                    # given example
        ([1, 2, 4, 1, -8, 1, 3], 4, 3),       # negatives in the middle
        ([3, 1, -1], 3, 2),
        ([-1, 1, 3], 3, 2),
        ([1, -1, 2], 0, 1),                   # k == 0: the self-match trap
        ([-3, 1], -3, 1),                     # negative target is legal
        ([0, 0, 0], 0, 6),                    # every slice of zeros counts
        ([], 5, 0),                           # empty input
        ([5], 5, 1),                          # single element hit
        ([5], 3, 0),                          # single element miss
    ],
)
def test_subarray_sum(nums, k, expected):
    assert subarray_sum(nums, k) is expected

#-------remove_duplicates
@pytest.mark.parametrize(
    "nums, expected_count, expected_prefix",
    [
        ([1, 1, 2, 3, 3], 3, [1, 2, 3]),      # given example
        ([], 0, []),                          # empty
        ([3], 1, [3]),                        # single element
        ([2, 2, 2, 2], 1, [2]),               # all duplicates
        ([1, 2], 2, [1, 2]),                  # all unique — the stale-count trap
        ([1, 2, 3], 3, [1, 2, 3]),            # all unique, longer
        ([1, 1, 2], 2, [1, 2]),               # unique at the very end
        ([-3, -1, 0, 0, 2], 4, [-3, -1, 0, 2]),  # negatives, sorted
    ],
)
def test_remove_duplicates(nums, expected_count, expected_prefix):
    count = remove_duplicates(nums)
    assert count is expected_count
    # The expectation is the array gets mutated in place with unique values.
    assert nums[:count] == expected_prefix

#-------test_is_palindrome
@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),   # given example
        ("race a car", False),                      # given example
        ("Panama", False),                          # not a palindrome — expectation re-derived
        ("20man n-am02", True),                     # digits participate
        ("", True),                                 # vacuously true, by convention
        (".,", True),                               # all punctuation — the IndexError trap
        ("n", True),                                # single char
        ("nn", True),                               # even length
        ("a.", True),                               # skip drives pointers together
        (".a", True), 
        ("0P", False),                              # two alnums that differ ('0' vs 'p')
        ("Aa", True),                               # case-insensitive
        ("12321", True),                            # pure digits
        ("ab,,,,ba c", False),                      # punctuation run mid-string
    ]                   )
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected

#-------climbing_stairs
@pytest.mark.parametrize(
    "n, expected",
    [
        (-1, 0),
        (0, 0),
        (1, 1),
        (2, 2),
        (4, 5),
        (6, 13),
    ])
def test_climbing_stairs(n, expected):
    assert climbing_stairs(n) == expected

#-------longest_substring
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("a", 1),
        ("", 0),
        ("ab", 2),
    ]
)
def test_longest_substring(s, expected):
    assert longest_substring(s) == expected

#-------product_of_array
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1,2,3,4], [24, 12, 8, 6]),
        ([1,0,3,4],[0, 12, 0, 0]),
        ([7], [1]),
        ([-1,2,3], [6, -3, -2]),
        ([1,1,1], [1, 1, 1]),
        ([1,1,0], [0, 0, 1]),
        ([], []),
    ]
)
def test_product_of_array(nums, expected):
    assert product_of_array(nums) == expected
    assert product_of_array_v2(nums) == expected