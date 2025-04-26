#!/usr/bin/env pypy3

from lib.utils import parse, answer
from lib.algorithms.string import caesar


def solve(
    a:list[str],
    b:list[int | str],
    c:list[str]
) -> None:  
    s1 = [caesar(i, 107) for i in a]

    s2 = [caesar(i[0], i[1], False) for i in b]

    s3 = [p for p, q in c if len({(ord(x) - ord(y)) % 26 for x, y in zip(p, q)}) != 1]

    answer(s1, s2, s3)

solve(*parse("dane_6_1", "dane_6_2", "dane_6_3"))
