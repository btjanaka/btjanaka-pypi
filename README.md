# btjanaka

Bryon Tjanaka in a Python package!

|                       Source                        |                       Demo                       |                                                    PyPI                                                    |                                                                                                    CI/CD                                                                                                    |
| :-------------------------------------------------: | :----------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [GitHub](https://github.com/btjanaka/btjanaka-pypi) | [Demo](https://pages.btjanaka.net/btjanaka-pypi) | [![PyPI](https://img.shields.io/pypi/v/btjanaka?style=flat&color=blue)](https://pypi.org/project/btjanaka) | [![Test and Deploy](https://github.com/btjanaka/btjanaka-pypi/workflows/Test%20and%20Deploy/badge.svg?branch=master)](https://github.com/btjanaka/btjanaka-pypi/actions?query=workflow%3A"Test+and+Deploy") |

## Demo

To try the btjanaka package in the browser (courtesy of
[Pyodide](https://pyodide.org/)), visit
[this page](https://pages.btjanaka.net/btjanaka-pypi)

## Installation

To install from PyPI, run:

```bash
pip install btjanaka
```

To install from source, clone this repo, cd into it, and run:

```bash
pip install .
```

`btjanaka` is tested on Python 3.7+. Earlier Python versions may work but are
not guaranteed.

## Usage

```python
import btjanaka
```

### Basics

```python
btjanaka.firstname()  # "Bryon"
btjanaka.lastname()  # "Tjanaka"
btjanaka.name()  # "Bryon Tjanaka"
btjanaka.yell()  # "BRYON TJANAKA"
```

### Info

```python
btjanaka.email()  # "bryon@tjanaka.net"
btjanaka.github()  # "btjanaka"
btjanaka.linkedin()  # "btjanaka"
btjanaka.twitter()  # "btjanaka"
btjanaka.webdemo()  # "https://pages.btjanaka.net/btjanaka-pypi"
btjanaka.webdemo(browser=True)  # Opens the web demo in a browser.
btjanaka.website()  # "https://btjanaka.net"
btjanaka.website(browser=True)  # Opens the website in a browser.
```

### Internationalization

```python
btjanaka.british()  # "oi Bryon!"
btjanaka.canadian()  # "Bryon Tjanaka eh"
btjanaka.chinese()  # "张学龙"
```

### Counting

```python
len(btjanaka.name()) - len(btjanaka.yell())  # 0
len(btjanaka.name()) // len(btjanaka.yell())  # 1
btjanaka.firstname().count("o") + len(btjanaka.name()[0])  # 2
btjanaka.lastname().count("a")  # 3
btjanaka.website().count("/") + btjanaka.website().count("n")  # 4
len(btjanaka.firstname())  # 5
btjanaka.name().count("n") * btjanaka.email().count("n")  # 6
len(btjanaka.lastname())  # 7
btjanaka.canadian().index("y")**len(btjanaka.chinese())  # 8
len(btjanaka.british())  # 9
len(btjanaka.email().replace(".", "").split("@")[1])  # 10
```

## Credits

Inspired by [five](https://pypi.org/project/five/).
