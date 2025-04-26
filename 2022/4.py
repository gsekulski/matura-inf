#!/usr/bin/env pypy3

from lib.utils import parse, answer
from lib.algorithms.numbers import factors


def solve(liczby: list[int]) -> None:
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
    n = len(liczby)

    # 6.3 ~O(k*n^2) with negligible k = 5, as it's a constant.
    nexts = {x: [] for x in liczby}
    for i, x in enumerate(liczby):
        for y in liczby[i+1:]:
            if y % x == 0:
                nexts[x].append(y)

    dp = {x: [0]*6 for x in liczby}
    for x in liczby:
        dp[x][0] = 1
    for i in range(1, 6):
        for x in liczby:
            for y in nexts[x]:
                dp[x][i] += dp[y][i - 1]

    s3 = [
        sum(dp[x][2] for x in liczby),
        sum(dp[x][4] for x in liczby)
    ]

    answer(s1, s2, s3)

solve(*parse("liczby"))
