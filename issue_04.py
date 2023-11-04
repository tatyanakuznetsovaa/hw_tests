from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    "iterbl,result",
    [
        (
            ["Moscow", "New York", "Moscow", "London"],
            [
                ("Moscow", [0, 0, 1]),
                ("New York", [0, 1, 0]),
                ("Moscow", [0, 0, 1]),
                ("London", [1, 0, 0]),
            ],
        ),
        ([], []),
        # ("Moscow", 2, [("Moscow", [0, 1]), (2, [1, 0])]),
        ([1, 2, 3], [(1, [0, 0, 1]), (2, [0, 1, 0]), (3, [1, 0, 0])]),
    ],
)
def test_fit_transform_iter(iterbl, result):
    assert fit_transform(iterbl) == result


def test_fit_transform_noniter():
    assert fit_transform("Moscow", 2) == [("Moscow", [0, 1]), (2, [1, 0])]


def test_fit_transform_with_exception():
    with pytest.raises(Exception):
        fit_transform(2, "Moscow")
