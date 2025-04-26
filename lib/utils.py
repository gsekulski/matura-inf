#!/usr/bin/env pypy3

import os
import inspect
from datetime import datetime


def process(
    data:list[any],
    header:bool,
    delimeter:str,
    n_col:int
) -> list[any]:
    def is_date(s:str) -> str | None:
        date_fmts = [
            "%Y-%m-%d %H:%M:%S",
            "%d-%m-%Y %H:%M:%S",
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%Y.%m.%d %H:%M:%S",
            "%d.%m.%Y %H:%M:%S",
            "%Y.%m.%d",
            "%d.%m.%Y",
        ]

        for fmt in date_fmts:
            try:
                datetime.strptime(s, fmt)
                return fmt
            except ValueError:
                pass
        return None

    def is_float(s:str) -> float | bool:
        try:
            return float(s.replace(',', '.'))
        except ValueError:
            return False

    def is_int(s:str) -> int | bool:
        return int(s) if s.lstrip('-').isdigit() else False

    if n_col == 1 and not header:
        return [is_int(row[0]) or is_float(row[0]) or row[0] for row in data]

    if header:
        data = data[1:]
    
    t_cols = [
        ('date', fmt) if (fmt := is_date(data[0][i]))
        else ('int', None) if is_int(data[0][i]) is not False
        else ('float', None) if is_float(data[0][i]) is not False
        else ('string', None)
        for i in range(n_col)
    ]

    for row in data:
        for i, val in enumerate(row):
            t_col, fmt = t_cols[i]
            row[i] = (
                datetime.strptime(val, fmt) if t_col == 'date' else
                is_int(val) if t_col == 'int' else
                is_float(val) if t_col == 'float' else
                val
            )

    return data


def parse(*files) -> list[any]:
    def get_base() -> str:
        frame = inspect.stack()[2]
        return os.path.dirname(os.path.abspath(frame.filename))

    def get_data(base:str) -> str:
        for e in os.scandir(base):
            if "dane" in e.name.lower():
                return e.path
        return None

    def get_delimeter(line) -> str:
        d = [';', '\t', ' ']
        return max(d, key=line.count)

    def is_header(line:list[str]) -> bool:
        keywords = {"id", "numer", "czas", "rodzaj", "pesel", "imie",
        "nazwisko", "lp", "id_pok", "tytul", "data", "kod", "panstwo",
        "jezyk", "nazwa", "dzien"}
        return any(any(keyword in w.lower() for keyword in keywords) for w in line)
    
    res = []
    data_path = get_data(get_base())
    for file in files:
        filepath = os.path.join(data_path, file + ".txt")
        with open(filepath, 'r', encoding='windows-1250') as f:
            lines = f.readlines()
            first_line = lines[0].strip()
            delimeter = get_delimeter(first_line)
            n_col = len(first_line.split(delimeter))
            header = is_header(first_line.split(delimeter))
            res.append(process([line.strip().split(delimeter) for line in
            lines], header, delimeter, n_col))
    return res


def answer(*args) -> None:
    def get_filename() -> str:
        frame = inspect.stack()[2]
        filename = os.path.basename(frame.filename)
        return os.path.splitext(filename)[0]

    filename = get_filename()
    for i, arg in enumerate(args, 1):
        print(f"{filename}.{i}:\n{arg}", end="")
        if i != len(args): print('\n')
