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


#### How to run commands
`python3 -m unittest` run all tests from the folder

`python3 -m unittest -v` with verbose mode 

`python3 -m unittest discover -v -p "test_*"`  find all testswith mask and run with verbose mode


## Coverage
The best way is using tools:
```
http://nose.readthedocs.io/en/latest/plugins/cover.html
```
```
https://www.saltycrane.com/blog/2012/04/test-coverage-nose-and-coveragepy/
```
and
```commandline
https://pypi.org/project/pytest-cov/ 
```
***For example:***
`pip uninstall pytest-cov`

```commandline
py.test --cov-report term-missing --cov=Examples
```
- show result in command line
```commandline
py.test --cov-report html --cov=Examples
```
- get HTML result

To exclude some files from coverage it is necessary to use config file:
```commandline
nano .coveragerc

[run]
omit = Examples/test_*
```

