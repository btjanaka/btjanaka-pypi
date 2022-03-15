# btjanaka

Bryon Tjanaka in a Python package!

|                       Source                        |                                                    PyPI                                                    |                                                                                                    CI/CD                                                                                                    |
| :-------------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [GitHub](https://github.com/btjanaka/btjanaka-pypi) | [![PyPI](https://img.shields.io/pypi/v/btjanaka?style=flat&color=blue)](https://pypi.org/project/btjanaka) | [![Test and Deploy](https://github.com/btjanaka/btjanaka-pypi/workflows/Test%20and%20Deploy/badge.svg?branch=master)](https://github.com/btjanaka/btjanaka-pypi/actions?query=workflow%3A"Test+and+Deploy") |

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
btjanaka.website()  # "https://btjanaka.net"
btjanaka.website(browser=True)  # Opens the website in a browser.
```

### Internationalization

```python
btjanaka.british()  # "oi Bryon!"
btjanaka.canadian()  # "Bryon Tjanaka eh"
btjanaka.chinese()  # "张学龙"
```

## Credits

Inspired by [five](https://pypi.org/project/five/).
