import pytest

from graph.count_islands import count_islands, count_islands_v2, count_islands_v3


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]], 3),
        ([[1, 1, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 1, 0]], 2),
        ([[1]], 1),
        ([[0]], 0),
        ([], 0),
    ],
)
def test_count_islands(grid, expected):
    assert count_islands(grid) == expected
    assert count_islands_v2(grid) == expected
    assert count_islands_v3(grid) == expected

