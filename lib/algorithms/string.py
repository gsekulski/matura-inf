#!/usr/bin/env pypy310

def caesar(s: str, key: int, encode: bool = True) -> str:
    """Caesar cipher."""
    key %= 26
    def shift(c:chr) -> str:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            offset = key if encode else -key
            return chr((ord(c) - base + offset) % 26 + base)
        return c
    return ''.join(shift(c) for c in s)


def is_palindrome(s: str) -> bool:
    """Palindrome."""
    return s == s[::-1]
