#!/usr/bin/python3
from termcolor import colored

def banner():
    from pyfiglet import Figlet
    text = "Youtube Downloader"
    print(colored(Figlet(font="slant").renderText(text), 'yellow'))
banner()
