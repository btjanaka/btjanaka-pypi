"""Bryon Tjanaka in a Python Package!"""
__version__ = "0.1.0"

import webbrowser


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
