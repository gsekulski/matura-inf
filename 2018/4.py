#!/usr/bin/env pypy3

from lib.utils import parse, answer


def solve(sygnaly:list[str]) -> list[any]:
    s1 = "".join([sygnaly[i][9] for i in range(len(sygnaly)) if i % 40 == 39])

    s2 = max(sygnaly, key=lambda v: len(set(v)))

    s3 = [i for i in sygnaly if all(abs(ord(a) - ord(b)) <= 10 
    for a in i for b in i)]

    answer(s1, s2, s3)

solve(*parse("sygnaly"))
