"""Property-based tests for sorting — challenge ch-property-sort-001."""
from __future__ import annotations

import sys
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from implementations.reference.sorts import (  # noqa: E402
    broken_sort_drop_last,
    correct_sort,
)


def is_sorted(xs: list) -> bool:
    return all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1))


def is_permutation(a: list, b: list) -> bool:
    return sorted(a) == sorted(b)


@settings(max_examples=100, deadline=None)
@given(st.lists(st.integers()))
def test_correct_sort_is_sorted_and_permutation(xs):
    out = correct_sort(xs)
    assert is_sorted(out)
    assert is_permutation(xs, out)


@settings(max_examples=50, deadline=None)
@given(st.lists(st.integers(), min_size=2))
def test_broken_sort_detected(xs):
    """Property should fail for the deliberately broken implementation."""
    out = broken_sort_drop_last(xs)
    ok = is_sorted(out) and is_permutation(xs, out)
    assert not ok, "broken_sort_drop_last unexpectedly satisfied both properties"


def test_broken_sort_fails_under_pytest():
    """Example-driven confirmation that a broken implementation violates properties."""
    xs = [1, 2, 3]
    out = broken_sort_drop_last(xs)
    assert not (is_sorted(out) and is_permutation(xs, out))
