import pytest

from patterns.product_of_array import product_of_array, product_of_array_v2


# -------product_of_array
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([1, 0, 3, 4], [0, 12, 0, 0]),
        ([7], [1]),
        ([-1, 2, 3], [6, -3, -2]),
        ([1, 1, 1], [1, 1, 1]),
        ([1, 1, 0], [0, 0, 1]),
        ([], []),
    ],
)
def test_product_of_array(nums, expected):
    assert product_of_array(nums) == expected
    assert product_of_array_v2(nums) == expected

