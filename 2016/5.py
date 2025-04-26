#!/usr/bin/env pypy3

from collections import Counter

from lib.utils import parse, answer


def solve(
    studenci: list[str],
    meldunek: list[str],
    wypozyczenia: list[str]
) -> None:
    studenci = {i[0]: i[1:] for i in studenci}
    studenci = dict(sorted(studenci.items(), key=lambda i: i[1][0]))
    
    s1 = {}
    for i in wypozyczenia: s1[i[1]] = s1.get(i[1], []) + [i[2]]
    x = sorted(s1.items(), key=lambda i: len(i[1]))[-1]
    s1 = [studenci[x[0]], x[1]]

    x = {}
    for i in meldunek: x[i[1]] = x.get(i[1], 0) + 1
    s2 = round(sum(x.values()) / len(x), 4)

    x = sum(1 for i in studenci if int(str(i)[-2]) % 2 == 0)
    s3 = {"m": len(studenci) - x, "k": x}

    x = set()
    for i in meldunek: x.add(i[0])
    s4 = [studenci[i] for i in studenci if i not in x]

    m = {i[0]: i[1] for i in meldunek}
    x = {}
    for i in wypozyczenia: x[i[2]] = x.get(i[2], []) + [i[1]]
    s5 = 0
    for i in x:
        for n, j in enumerate(x[i]):
            if j in m:
                x[i][n] = int(m[j])
    s5 = len(wypozyczenia) - \
    sum(sum(c - 1 for c in Counter(v).values() if c > 1) for v in x.values())

    answer(s1, s2, s3, s4, s5)
        
solve(*parse("studenci", "meldunek", "wypozyczenia"))
