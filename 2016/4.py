#!/usr/bin/env pypy3

from math import pi

from lib.utils import parse, answer


def circle_state(x: int, y: int) -> int:
    pos = pow(x - 200, 2) + pow(y - 200, 2)
    
    if pos < 40000: return 1
    elif pos == 40000: return 2
    return 0


def solve(punkty: list[int]) -> None:
    s1 = [
        len([i for i in punkty if circle_state(i[0], i[1]) == 1]),
        [i for i in punkty if circle_state(i[0], i[1]) == 2]
    ]

    k = [0, 0, 0, 0] 
    s2, s3 = [], []
    for i, v in enumerate(punkty):
        k[circle_state(v[0], v[1])] += 1
        k[3] = round(((k[1] + k[2]) * 4) / (k[0] + k[1] + k[2]), 4)
        if i in [999, 4999, len(punkty) - 1]:
            s2.append(k[3])
        if i in [999, 1699]:
            s3.append(round(abs(pi - k[3]), 4))

    answer(s1, s2, s3)

solve(*parse("punkty"))
