#!/usr/bin/env pypy3

from datetime import datetime

from lib.utils import parse, answer


def solve(
    gracze:list[int | str | datetime],
    klasy:list[int | str],
    jednostki:list[int | str]
) -> None:
    x = {i[1]: sum(1 for j in gracze if j[1] == i[1] and j[2].year == 2018) for i in gracze}
    s1 = sorted(x.items(), key=lambda item: item[1], reverse=True)[:5]

    x = {i[0]: i[2] for i in klasy if "elf" in i[0]}
    s2 = {k: 0 for k in x}
    s2 = {k: sum(x[j[2]] for j in jednostki if j[2] == k) for k in s2}

    x = {}
    for i in jednostki: x[i[1]] = x.get(i[1], []) + [i[2]] 
    s3 = sorted({i for i in x if "artylerzysta" not in x[i]})

    answer(s1, s2, s3)

solve(*parse("gracze", "klasy", "jednostki"))
