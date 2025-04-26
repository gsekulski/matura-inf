#!/usr/bin/env pypy3

from collections import defaultdict
from datetime import datetime
from math import ceil

from lib.utils import parse, answer


def solve(cukier:list[int | str | datetime], cennik:list[int | float]) -> None:
    cennik = {int(i[0]): i[1] for i in cennik}  
    volume = {}
    for i in cukier: volume[i[1]] = volume.get(i[1], 0) + i[2]
    
    s1 = sorted(volume.items(), key=lambda item: item[1], reverse=True)[:3]

    s2 = round(sum(i[2] * cennik[i[0].year] for i in cukier), 2)

    s3 = {}
    for i in cukier: s3[i[0].year] = s3.get(i[0].year, 0) + i[2]

    d, s4 = defaultdict(int), 0
    for _, c, kg in cukier:
        d[c] += kg
        s4 += kg * (20 if d[c] >= 10000 else 10 if d[c] >= 1000 else 5 \
        if d[c] >= 100 else 0)

    s5, cur, y, m = 1, 5000, None, None
    for d, _, kg in cukier:
        if (d.year, d.month) != (y, m) and y is not None:
            p = ceil(max(0, 5000 - cur) / 1000)
            s5 += p >= 4
            cur += p * 1000
        y, m = d.year, d.month
        cur -= kg

    answer(s1, s2, s3, s4, s5)

solve(*parse("cukier", "cennik"))
