"""Tests for btjanaka."""
import btjanaka


def test_calls():
    """Try calling every method."""
    for name, method in btjanaka.__dict__.items():
        if not name.startswith("_") and callable(method):
            method()
