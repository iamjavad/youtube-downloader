#!/usr/bin/python3

from pytube import YouTube

url = YouTube('https://www.youtube.com/watch?v=ulNswX3If6U')

print(url.title)

print(url.thumbnail_url)

print(url.streams.first().download())
