"""Bryon Tjanaka in a Python Package!"""
__version__ = "0.4.0"

import webbrowser

## Basics


def firstname():
    """First name only."""
    return "Bryon"


def lastname():
    """Last name only."""
    return "Tjanaka"


def name():
    """Full name."""
    return "Bryon Tjanaka"


def yell():
    """Yell the name!"""
    return "BRYON TJANAKA"


## Info


def email():
    """Email address."""
    return "bryon@tjanaka.net"


def github():
    """GitHub username."""
    return "btjanaka"


def linkedin():
    """LinkedIn username."""
    return "btjanaka"


def twitter():
    """Twitter handle."""
    return "btjanaka"


def webdemo(browser: bool = False):
    """Returns the web demo URL or opens in a browser if browser=True."""
    url = "https://pages.btjanaka.net/btjanaka-pypi"
    if browser:
        webbrowser.open(url)
    return url


def website(browser: bool = False):
    """Returns the website URL or opens in a browser if browser=True."""
    url = "https://btjanaka.net"
    if browser:
        webbrowser.open(url)
    return url


## Internationalization


def british():
    """Oi."""
    return "oi Bryon!"


def canadian():
    """Eh."""
    return "Bryon Tjanaka eh"


def chinese():
    """Chinese name."""
    return "张学龙"
