#!/usr/bin/env pypy3

from collections import Counter

from lib.utils import parse, answer


def solve(liczby:list[int]) -> None:
    s1 = sum(1 for i in [dict(Counter(str(n))) for n in liczby] \
    if i.get('0', 0) > i.get('1', 0))

    s2 = {
    '2': sum(1 for i in liczby if not (i & 1)),
    '8': sum(1 for i in liczby if not (i & 7))
    }

    s3 = {
    "min:": liczby.index(min(liczby)) + 1,
    "max:": liczby.index(max(liczby)) + 1
    }

    answer(s1, s2, s3)

solve(*parse("liczby"))
