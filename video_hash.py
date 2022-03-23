#!/usr/bin/python

from ast import For
import os, sys

# Open a file
path = "C:/Users/murad/Desktop/videoHash/videos"
dirs = os.listdir( path )

# This would print all the files and directories
# for file in dirs:
#    print(file)

from videohash import VideoHash
os.chdir('videos')
vid =  VideoHash('videos/0bf362fa47231a9e523f7243bc081be2.mp4')
print('Hash -->', vid.hash)
