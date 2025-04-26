#!/usr/bin/env pypy3

from datetime import datetime

from lib.utils import parse, answer


def solve(
    panstwa: list[float | str],
    jezyki: list[str],
    uzytkownicy: list[float | str]
) -> None:
    rodziny = {}
    for i in jezyki: rodziny[i[1]] = rodziny.get(i[1], []) + [i[0]]

    s1 = {k: len(v) for k, v in sorted(rodziny.items(), key=lambda x: len(x[1]),
    reverse=True)}

    x = [
        [i[1] for i in uzytkownicy if i[3] == "nie"],
        [i[1] for i in uzytkownicy if i[3] == "tak"]
    ]
    s2 = len([i[0] for i in jezyki if i[0] in x[0] and i[0] not in x[1]])

    """x = {}
    for i in uzytkownicy: x[i[1]] = x.get(i[1], []) + i[0]
    for k, v in x: x[k] 
    s3 = [k for k, v in x if len(v) >= 4]"""

    answer(s1, s2)

solve(*parse("panstwa", "jezyki", "uzytkownicy"))
