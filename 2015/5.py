#!/usr/bin/env pypy3

from math import floor

from lib.utils import parse, answer


def solve(kraina:list[int | str]) -> None:
    s1 = {}
    for i in kraina: s1[i[0][3]] = s1.get(i[0][3], 0) + i[1] + i[2]

    s2 = {}
    for i in kraina:
        if i[3] > i[1] and i[4] > i[2]:
            s2[i[0][3]] = s2.get(i[0][3], 0) + 1    

    s3 = [0, 0, 1]
    growth_rates = []
    years = {2013: [i[1] + i[2] for i in kraina], 2014: [i[3] + i[4] for i in kraina]}
    for i in kraina:
        growth_rates.append(floor((i[3] + i[4]) / (i[1] + i[2]) * 10000) / 10000)
    for i in range(2015, 2026):
        years[i] = []
        for j in range(50):
            if years[i - 1][j] > (2 * years[2013][j]) and growth_rates[j] != 1:
                years[i].append(years[i - 1][j])
                growth_rates[j] = 1
                s3[2] += 1
            else:
                years[i].append(int(floor(growth_rates[j] * years[i - 1][j])))
    s3[0] = sum(years[2025])
    s3[1] = years[2025].index(max(years[2025])) + 1

    answer(s1, s2, s3)

solve(*parse("kraina"))
