#!/usr/bin/env pypy3

from collections import defaultdict
from datetime import datetime

from lib.utils import parse, answer


def solve(
    komputery: list[str],
    awarie: list[int | str],
    naprawy: list[int | str]
) -> None: 
    x = {int(i[0]): i[1] for i in komputery}
    sekcje = defaultdict(set)
    for k, v in x.items(): sekcje[v].add(k)

    s1 = {i[2]: sum(1 for j in komputery if j[2] == i[2]) for i in komputery}
    s1 = sorted(s1.items(), key=lambda item: item[1], reverse=True)[:10]

    # Fix me.
    t = {i[0] for i in komputery if i[1] == 'A'}
    s2 = {}
    a = {i[0]: i[1:] for i in naprawy}
    for i in naprawy:
        if i[0] in t and i[2] == "wymiana":
            s2[i[0]] = s2.get(i[0], 0) + 1
    s2 = {k: v for k, v in s2.items() if v >= 10}

    s3 = 0
    d = defaultdict(set)
    for _, k, t, _ in awarie:
        k = int(k)
        if k in x:
            d[t.date(), x[k]].add(k)
    for (m, n), z in d.items():
        if z == sekcje[n]:
            s3 = (m, n)
            break

    x = {int(i[0]): i[2] for i in awarie}
    t = defaultdict(list)
    for i, j, _ in naprawy:
        t[int(i)].append(j)
    s4 = max(
        ((i, x[i], max(t[i])) for i in x if i in t),
        key=lambda j: (j[2] - j[1]).total_seconds()
    )

    critical = {i[1] for i in awarie if i[3] >= 8} 
    s5 = sum(1 for i in komputery if i[0] not in critical)

    answer(s1, s2, s3, s4, s5)

solve(*parse("komputery", "awarie", "naprawy"))
