"""Tests for btjanaka."""
import btjanaka


def test_calls():
    """Try calling every method."""
    for name, method in btjanaka.__dict__.items():
        if not name.startswith("_") and callable(method):
            method()


def test_counting():
    """Test counting - copy this to README."""
    nums = [
        len(btjanaka.name()) - len(btjanaka.yell()),  # 0
        len(btjanaka.name()) // len(btjanaka.yell()),  # 1
        btjanaka.firstname().count("o") + len(btjanaka.name()[0]),  # 2
        btjanaka.lastname().count("a"),  # 3
        btjanaka.website().count("/") + btjanaka.website().count("n"),  # 4
        len(btjanaka.firstname()),  # 5
        btjanaka.name().count("n") * btjanaka.email().count("n"),  # 6
        len(btjanaka.lastname()),  # 7
        btjanaka.canadian().index("y")**len(btjanaka.chinese()),  # 8
        len(btjanaka.british()),  # 9
        len(btjanaka.email().replace(".", "").split("@")[1]),  # 10
    ]

    for i, n in enumerate(nums):
        assert i == n
