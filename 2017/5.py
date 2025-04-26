#!/usr/bin/env pypy3

from datetime import datetime

from lib.utils import parse, answer


def solve(
    druzyny:list[int | str],
    sedziowie:list[str],
    wyniki:list[int | datetime | str]
) -> None:
    x = [i[0] for i in druzyny if "Kucykowo" in i[2] and "Galop" not in i[2]]
    s1 = [{'T': 0, 'L': 0, 'P': 0}, {}]
    for t in wyniki:
        if t[3] in x:
            s1[0][t[1]] += 1
            if t[0].year not in s1[1]:
                s1[1][t[0].year] = 0
            s1[1][t[0].year] += 1
    s1[1] = max(s1[1], key=s1[1].get)

    w = {}
    for i in wyniki: w[i[3]] = w.get(i[3], 0) + (i[5] - i[6])
    s2 = [druzyny[i - 1] for i in [k for k, v in w.items() if v == 0]]

    s3 = {'P': 0, 'R': 0, 'W': 0}
    for i in wyniki:
        if i[5] > i[6]:
            s3['W'] += 1
        elif i[5] == i[6]:
            s3['R'] += 1
        else:
            s3['P'] += 1

    sedziowie, k = [i[0] for i in sedziowie], set()
    for i in wyniki:
        if i[4] in sedziowie and i[1] == 'P':
            k.add(i[4])
    s4 = len(sedziowie) - len(k)

    answer(s1, s2, s3, s4) 

solve(*parse("druzyny", "sedziowie", "wyniki"))
