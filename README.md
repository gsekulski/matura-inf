Solutions to practical parts of previous years' Polish Matura exams. They may serve as valuable resources for this year's or upcoming years' exams.

Most, if not all, solutions currently available on GitHub use Excel/Calc and Access/SQL, as tasks 5 and 6 are typically designed to be solved with these tools. However, in this project, all tasks were solved exclusively in Python.

All solutions are implemented in a concise but clear way. Modules are used, but in fact, every task could be solved without them without increasing the code's complexity -- except for simulation tasks, where it would be rather difficult to avoid using the `datetime` and `timedelta` classes from the `datetime` module, considering the limited time available.

The solutions meet the requirements of the CKE. Which are provided here: https://arkusze.pl/informatory/informator-maturalny-informatyka-2015.pdf

All necessary algorithms and techniques, divided into categories and sorted according to their frequency of use in the project, are placed as submodules in `lib/algorithms`. Some of them were not used yet, but remain in the project for possible future use.

The sheets and data used are available on the website arkusze.pl. Note: in one file (`2016/dane_6_2.txt`), there is an error -- the decryption key is missing in some columns. Also, in one of the 2017 data files, the date format is incorrect (Time XX:XX:65, supposedly in format HH:MM:SS).

At the time of writing this README, most of the solutions for sheets from 2015-2022 have been implemented. In the future, solutions from earlier years may also be added.

To minimize repetitive code, functions responsible for parsing input and printing results have been placed in `lib/utils.py`.

To run the code:
`pypy3.10 -m 20XX.X` 

For instance:
`pypy3.10 -m 2015.4`

## Contribute
Feel free to [contribute](CONTRIBUTING.md) to matura-inf.
