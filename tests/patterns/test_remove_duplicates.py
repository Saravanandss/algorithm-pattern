import pytest

from patterns.remove_duplicates import remove_duplicates


# -------remove_duplicates
@pytest.mark.parametrize(
    "nums, expected_count, expected_prefix",
    [
        ([1, 1, 2, 3, 3], 3, [1, 2, 3]),  # given example
        ([], 0, []),  # empty
        ([3], 1, [3]),  # single element
        ([2, 2, 2, 2], 1, [2]),  # all duplicates
        ([1, 2], 2, [1, 2]),  # all unique — the stale-count trap
        ([1, 2, 3], 3, [1, 2, 3]),  # all unique, longer
        ([1, 1, 2], 2, [1, 2]),  # unique at the very end
        ([-3, -1, 0, 0, 2], 4, [-3, -1, 0, 2]),  # negatives, sorted
    ],
)
def test_remove_duplicates(nums, expected_count, expected_prefix):
    count = remove_duplicates(nums)
    assert count is expected_count
    # The expectation is the array gets mutated in place with unique values.
    assert nums[:count] == expected_prefix