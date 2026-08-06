import pytest

from patterns.kth_largest_element import (
    find_kth_largest_max_heap,
    find_kth_largest_min_heap,
    find_kth_largest_quickselect,
)


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, 6),
        ([8, 7, 6, 5, 4, 3, 2, 1], 3, 6),
        ([-1, -2, -3, -4, -5, -6, -7, -8], 3, -3),
    ],
)
def test_find_kth_largest_max_heap(nums, k, expected):
    assert find_kth_largest_min_heap(nums, k) == expected
    assert find_kth_largest_quickselect(nums, k) == expected
    assert find_kth_largest_max_heap(nums, k) == expected

@pytest.mark.parametrize(
    "nums, k",
    [
        ([], 3),  # empty array
        ([3, 2], 3),  # k larger than len(nums)
        ([3, 2], 0),  # k below 1
    ],
)
def test_find_kth_largest_value_error(nums, k):
    with pytest.raises(ValueError):
        find_kth_largest_max_heap(nums, k)
    with pytest.raises(ValueError):
        find_kth_largest_min_heap(nums, k)
    with pytest.raises(ValueError):
        find_kth_largest_quickselect(nums, k)

