"""Bryon Tjanaka in a Python Package!"""
__version__ = "0.1.1"

import webbrowser

## Basics


def name():
    """Just the name."""
    return "Bryon Tjanaka"


def yell():
    """Yell the name!"""
    return "BRYON TJANAKA"


def website(browser: bool = False):
    """Return the website or open in a browser if browser=True."""
    url = "https://btjanaka.net"
    if browser:
        webbrowser.open(url)
    return url


## Internationalization


def chinese():
    """Chinese name."""
    return "张学龙"


def canadian():
    """Eh."""
    return "Bryon Tjanaka eh"
