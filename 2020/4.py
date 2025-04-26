#!/usr/bin/env pypy3

from lib.utils import parse, answer
from lib.algorithms.numbers import primes


def solve(pary:list[int]) -> None:
    def longest_common(w:str) -> tuple[str, int]:
        best, cur = "", ""
        for c in w:
            cur = cur + c if cur and c == cur[-1] else c
            if len(cur) > len(best): best = cur
        return best, len(best)

    s1, p, nums = [], list(primes(100))[1:], [i[0] for i in pary]
    for i in nums:
        best = ()
        for j in p:
            b = i - j
            if b in p and j <= b:
                if not best or b - j > best[2] - best[1]:
                    best = (i, j, b)
        if best:
            s1.append(best)

    words = [i[1] for i in pary]
    s2 = [longest_common(w) for w in words]

    s3 = min((x, s) for x, s in pary if x == len(s))

    answer(s1, s2, s3)

solve(*parse("pary"))
