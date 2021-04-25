#!/usr/bin/python3

from pytube import YouTube

url = input('enter url:')
yt = YouTube(url)

def url():
    url 
    yt
    print(f'file name:{yt.title}')
    print(f'sample pictur:{yt.thumbnail_url}')

url()

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
    url()
