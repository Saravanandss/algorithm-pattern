import pytest

from graph.universal_sink import find_universal_sink


@pytest.mark.parametrize(
    "graph, expected",
    [
        (
            [
                [0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
            ],
            3,
        ),
        (
            [
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 1, 1],
            ],
            None,
        ),
        ([[1, 1, 1, 1], [1, 0, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]], 3),
        ([[0]], 0),
        ([[0, 1], [0, 0]], 1),
        ([], None),
    ],
)
def test_find_universal_sink(graph, expected):
    assert find_universal_sink(graph) == expected
