#!/usr/bin/env pypy3

from datetime import datetime

from lib.utils import parse, answer


def solve(
    klasa: list[str],
    uczen: list[int | str],
    ewidencja: list[int | str | datetime]
) -> None:
    uczen = {i[0]: i[1:] for i in uczen}

    x = {i[0] for i in klasa if "biologiczno-chemiczny" in i[1]}
    s1 = sum(1 for i in ewidencja if uczen[i[1]][0][-1] == 'a'
    and uczen[i[1]][2] in x)

    x = {i[1] for i in ewidencja if i[2].day == 6}
    s4 = {(uczen[i][0], uczen[i][1]) for i in uczen if i not in x}

    answer(s1, s4)

solve(*parse("klasa", "uczen", "ewidencja"))
