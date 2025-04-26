#!/usr/bin/env pypy3

def max_subarray(l: list[int]) -> int:
    """Largest sum of any contiguous subarray."""
    res = float('-inf')
    c = 0
    for n in l:
        c = max(n, c + n)
        res = max(res, c)
    return res


def most_common(l: list[any]) -> any:
    """Most common element in a list."""
    return max(set(l), key=l.count)


def freq_map(l: list[any]) -> dict[any, int]:
    """Return a frequency map of the list elements."""
    return {e: l.count(e) for e in set(l)}
