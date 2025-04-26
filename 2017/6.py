#!/usr/bin/env pypy3

from itertools import groupby

from lib.utils import parse, answer
from lib.algorithms.string import is_palindrome


def solve(dane:list[list[int]]) -> None:
    s1 = [max(map(max, dane)), min(map(min, dane))]

    s2 = len(dane) - sum(1 for i in dane if i == i[::-1]) 

    s3 = 0
    for i in range(len(dane)):
        for j in range(len(dane[0])):
            v = dane[i][j]
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(dane) and 0 <= nj < len(dane[0]):
                    if abs(v - dane[ni][nj]) > 128:
                        s3 += 1
                        break

    s4 = 0
    for i in zip(*dane):
        s4 = max(s4, max(len(list(j)) for _, j in groupby(i)))

    answer(s1, s2, s3, s4)

solve(*parse("dane"))
