#!/usr/bin/env python3

import os
import subprocess

class colors:
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    RESTORE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def error(str):
    print(colors.RED + (len(str) + 6) * '-' + '\n' + 'ERROR: ' + str + '\n' + (len(str)+6) * '-' + colors.RESTORE)
    exit()

def warn(str):
    print(colors.YELLOW + len(str) * '-' + '\n' + str + '\n' + len(str) * '-' + colors.RESTORE)

def info(str):
    print(colors.BLUE + len(str) * '-' + '\n' + str + '\n' + len(str) * '-' + colors.RESTORE)

for p in ['lib32-gcc-libs', 'git', 'gnupg', 'flex', 'bison', 'gperf', 'sdl', 'wxgtk2', 'squashfs-tools', 'curl', 'ncurses', 'zlib', 'schedtool',
			'perl-switch', 'zip', 'unzip', 'libxslt', 'bc', 'rsync', 'lib32-zlib', 'lib32-ncurses', 'lib32-readline', 'lzop', 'pngcrush', 'imagemagick', 'jdk8-openjdk']:
	os.system('sudo pacman -S --noconfirm ' + p)
	info('Installed ' + p)

for aur in ['ncurses5-compat-libs', 'lib32-ncurses5-compat-libs', 'xml2']:
	os.system('git clone https://aur.archlinux.org/' + aur + '.git' ' /tmp/' + aur)
