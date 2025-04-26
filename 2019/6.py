#!/usr/bin/env pypy3

from datetime import datetime

from lib.utils import parse, answer


def solve(
    marki: list[str],
    perfumy: list[int | str],
    sklad: list[str]
) -> None:
    sklady = {}
    for i in sklad: sklady[i[0]] = sklady.get(i[0], []) + [i[1]]
    marki = {i[0]: i[1] for i in marki}

    s1 = [i[1] for i in perfumy if "absolut jasminu" in sklady[i[0]]]

    s2 = {}
    for i in perfumy:
        if i[3] not in s2:
            s2[i[3]] = ["", float('inf')]
        if i[4] < s2[i[3]][1]:
            s2[i[3]][0] = i[1]
            s2[i[3]][1] = i[4]

    answer(s1, s2)

solve(*parse("marki", "perfumy", "sklad"))
