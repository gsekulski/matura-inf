#!/usr/bin/env pypy3

from collections import Counter

from lib.utils import parse, answer


def solve(instrukcje:list[str]) -> None:
    s2, s4 = [instrukcje[0][0], 1, instrukcje[0][0], 1], ""

    for i in instrukcje:
        if s2[0] == i[0]: s2[1] += 1
        else:
            if s2[1] > s2[3]: s2[2], s2[3] = s2[0], s2[1]
            s2[0], s2[1] = i[0], 1
        match i[0]:
            case "DOPISZ":
                s4 += i[1]
            case "ZMIEN":
                s4 = s4[:-1] + i[1]
            case "USUN":
                s4 = s4[:-1]
            case "PRZESUN":
               s4 = s4.replace(i[1], chr((ord(i[1]) - 64) % 26 + 65), 1)

    s1, s2 = len(s4), s2[2:]

    s3 = Counter("".join(i[1] for i in instrukcje if i[0] == "DOPISZ")).most_common(1)

    answer(s1, s2, s3, s4)

solve(*parse("instrukcje"))
