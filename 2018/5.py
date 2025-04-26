#!/usr/bin/env pypy3

from datetime import datetime, timedelta
from math import ceil

from lib.utils import parse, answer


def solve(woda: list[int | datetime]) -> None:
    s1 = {}
    s1 = {i[0].year: s1.get(i[0].year, 0) + i[1] for i in woda}
    s1 = max(s1, key=s1.get)

    s2 = max(map(len, ''.join(['1' if i[1] >= 10000 else '0' \
    for i in woda]).split('0')), default=0)

    s3 = {}
    for i in woda:
        if i[0].year == 2008:
            k = str(i[0].year) + '.' + str(i[0].month)
            s3[k] = s3.get(k, 0) + i[1]

    s4, x, ax = ["", 0, 0], 500_000, 500_000
    for d, i in woda:
        if x >= 800_000:
            s4[1] += 1
        s4[2] = max(s4[2], ax)
        if x > 1_000_000 and not s4[0]:
            s4[0] = d
        x = min(x, 1_000_000)
        x += i - ceil(x * 0.02)
        ax += i - ceil(ax * 0.02) 

    answer(s1, s2, s3, s4)

solve(*parse("woda"))
