#!/usr/bin/python3

from pytube import YouTube

url = input('enter url:')
#url = YouTube('https://www.youtube.com/watch?v=ulNswX3If6U')
yt = YouTube(url)

print(f'file name:{yt.title}')

print(yt.thumbnail_url)

yt.streams.first().download()
