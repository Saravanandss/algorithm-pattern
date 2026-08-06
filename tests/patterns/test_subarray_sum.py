"""Tests for the pattern drills.

House rule: every case is an (input, expected) pair — expectations are
written down, never held in the head. Suites deliberately include inputs
that exit loops in unexpected ways, because that is where the bugs lived.
"""

import pytest

from patterns.subarray_sum import subarray_sum


# -------subarray_sum
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3], 3, 2),  # given example
        ([1, 2, 4, 1, -8, 1, 3], 4, 3),  # negatives in the middle
        ([3, 1, -1], 3, 2),
        ([-1, 1, 3], 3, 2),
        ([1, -1, 2], 0, 1),  # k == 0: the self-match trap
        ([-3, 1], -3, 1),  # negative target is legal
        ([0, 0, 0], 0, 6),  # every slice of zeros counts
        ([], 5, 0),  # empty input
        ([5], 5, 1),  # single element hit
        ([5], 3, 0),  # single element miss
    ],
)
def test_subarray_sum(nums, k, expected):
    assert subarray_sum(nums, k) is expected


