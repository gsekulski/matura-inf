#!/usr/bin/env pypy3

from datetime import datetime

from lib.utils import parse, answer


def solve(
    kierowcy:list[str],
    wyscigi:list[int | str],
    wyniki:list[int | str]
) -> None:
    k = {i[0]: i[1:] for i in kierowcy}

    w = {i[0]: f"{i[1]} {i[2]}" for i in wyscigi}
    x = {}
    for i in wyniki: x[w[i[2]]] = x.get(w[i[2]], 0) + (i[1] if i[0] == "z45" else 0)
    s1 = max(x, key=x.get)
    
    s2 = {}
    for i in w: s2[w[i].split(' ')[1]] = s2.get(w[i].split(' ')[1], 0) + 1
    s2 = min(s2, key=s2.get)

    w00, w06, w12 = {}, {}, {}
    for i in wyniki:
        match w[i[2]][:4]:
            case "2000":
                w00[i[0]] = w00.get(i[0], 0) + i[1]
            case "2006":
                w06[i[0]] = w06.get(i[0], 0) + i[1]
            case "2012":
                w12[i[0]] = w12.get(i[0], 0) + i[1]

    s3 = [k[max(w00, key=w00.get)], k[max(w06, key=w06.get)], k[max(w12, key=w12.get)]]
    x = {i[0] for i in wyscigi if i[1] == 2012}
    y = {i[0] for i in wyniki if i[2] in x}

    s4 = {}
    for i in y: s4[k[i][2]] = s4.get(k[i][2], 0) + 1

    answer(s1, s2, s3, s4)

solve(*parse("Kierowcy", "Wyscigi", "Wyniki"))
