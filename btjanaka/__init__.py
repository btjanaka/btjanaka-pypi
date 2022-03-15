"""Bryon Tjanaka in a Python Package!"""
__version__ = "0.2.0"

import webbrowser

## Basics


def name():
    """Just the name."""
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


def website(browser: bool = False):
    """Return the website or open in a browser if browser=True."""
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
