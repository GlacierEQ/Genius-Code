"""Reference and deliberately broken sort implementations for property challenges."""
from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def correct_sort(xs: List[T]) -> List[T]:
    """Correct sorted copy (stable relative to Python's Timsort semantics for equal keys)."""
    return sorted(xs)


def broken_sort_drop_last(xs: List[T]) -> List[T]:
    """Deliberately broken: drops the last element when len > 1."""
    if len(xs) <= 1:
        return list(xs)
    return sorted(xs[:-1])


def broken_sort_not_permutation(xs: List[T]) -> List[T]:
    """Deliberately broken: corrupts an element so output is not a permutation."""
    if not xs:
        return []
    out = sorted(xs)
    if len(out) >= 2:
        out[0] = out[-1]  # type: ignore[assignment]
    return out
