#!/usr/bin/env pypy3

from math import isqrt
from typing import Generator


def gcd(a: int, b: int) -> int:
    """Greatest common divisor."""
    return gcd(b, a % b) if b else abs(a)


def lcm(a: int, b: int) -> int:
    """Least common multiple."""
    return (a * b) // (gcd(a, b))


def is_prime(n: int) -> bool:
    """Primality check."""
    if n % 2 == 0:
        if n == 2:
            return True
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def fibonacci(n: int) -> int:
    """N-th Fibonacci number."""
    def fib(p1:int, p2:int, c:int) -> int:
        return p1 if c < 1 else fib(p2, p2 + p1, c - 1)
    return fib(0, 1, n)


def primes(n: int) -> Generator[int, None, None]:
    """Primeset generator."""
    multiples = set()

    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


def factors(n: int) -> list[int]:
    """Integer factors."""
    f1, f2 = [], []

    for x in range(1, isqrt(n)):
        if n % x == 0:
            f1.append(x)
            f2.append(n // x)
    x += 1
    if x * x == n:
        f1.append(x)
    f1.extend(reversed(f2))
    return f1
