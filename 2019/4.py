#!/usr/bin/env pypy3

from math import factorial, gcd

from lib.utils import parse, answer


def factorial_digit_sum(n:int) -> int:
    n = list(str(n))
    return sum(factorial(int(d)) for d in n)


def solve(liczby:list[int]) -> None:
    def longest_subsequence(i=0, best=(0, 0, 0)) -> tuple[int, int, int]:
        if i >= len(liczby): return best
        g, j = liczby[i], i
        while j < len(liczby) and (g := gcd(g, liczby[j])) > 1:
            j += 1
        if j - i > best[1]:
            best = (liczby[i], j - i, g)
        return longest_subsequence(i + 1, best)

    three_powers = [pow(3, i) for i in range(12)] 
    s1 = sum(1 for i in liczby if i in three_powers)
    
    s2 = [i for i in liczby if i == factorial_digit_sum(i)]

    s3 = longest_subsequence()

    answer(s1, s2, s3)

solve(*parse("liczby"))
