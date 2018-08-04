#!/usr/bin/env python3

import os

class colors:
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    RESTORE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def error(str):
    print(colors.RED + len(str) * "-" + "\n" + str + "\n" + len(str) * "-" + colors.RESTORE)
    exit()

def warn(str):
    print(colors.YELLOW + len(str) * "-" + "\n" + str + "\n" + len(str) * "-" + colors.RESTORE)

def info(str):
    print(colors.BLUE + len(str) * "-" + "\n" + str + "\n" + len(str) * "-" + colors.RESTORE)

