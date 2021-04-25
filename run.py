#!/usr/bin/python3

from pytube import YouTube
from termcolor import colored
from banner import banner

url = input(colored('enter url:', 'blue'))
yt = YouTube(url)

print(colored(f'file name:{yt.title}', 'green'))
print(colored(f'sample picture:{yt.thumbnail_url}', 'green'))

dorn = input('''start Download:
    1-yes
    2-no!
    3-start again!
    :''')
if dorn == '1':
    yt.streams.first().download()
elif dorn == '2':
    print('good bye!')
    pass
elif dorn == '3':
    url = input('enter url:')
    yt = YouTube(url)
    yt.streams.first().download()
