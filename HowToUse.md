## Python Unit testing

The link to unittest module: `https://docs.python.org/3/library/unittest.html`

If we have the Class with name Calculator we should create the file with name test_Calculator.

`class TestCalc(unittest.TestCase):`

Here Class name can by whatever, but the best practice is naming Test+something like testing class name.

Methods should have name `test_`+ what method they test. For example: `test_add`.

To run tests:
```
python test_Calculator.py
```
or
```
python -m unittest test_Calculator
```
or
```
python -m unittest -v test_Calculator
```
`-v` means more verbose output
or
```
python -m coverage run test_Calculator.py
```
to start tests with coverage. Little bit later about it.