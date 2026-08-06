import pytest

from dp.climbing_stairs import climbing_stairs


@pytest.mark.parametrize(
    "n, expected",
    [
        (-1, 0),
        (0, 0),
        (1, 1),
        (2, 2),
        (4, 5),
        (6, 13),
    ],
)
def test_climbing_stairs(n, expected):
    assert climbing_stairs(n) == expected
