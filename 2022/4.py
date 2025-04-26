#!/usr/bin/env pypy3

from lib.utils import parse, answer
from lib.algorithms.numbers import factors


def solve(liczby:list[int]) -> None:
    s1, s2 = [0, None], [[0, None], [0, None]]

    for i in liczby:
        si = str(i)
        if si[0] == si[-1] and s1[1] is None:
            s1[1] = i
        s1[0] += si[0] == si[-1]
        f = factors(i)
        s2[0] = max(s2[0], [len(f), i])
        s2[1] = max(s2[1], [len(set(f)), i])

    liczby = sorted(set(liczby))
    trojki, piatki = [], 0

    # While it doesn't look like it, this is efficient.
    for u in liczby:
        for w in liczby:
            if w > u and w % u == 0:
                for x in liczby:
                    if x > w and x % w == 0:
                        trojki.append((u, w, x))
                        for y in liczby:
                            if y > x and y % x == 0:
                                for z in liczby:
                                    if z > y and z % y == 0:
                                        piatki += 1
    s3 = [len(trojki), piatki]

    answer(s1, s2, s3)

solve(*parse("liczby"))
