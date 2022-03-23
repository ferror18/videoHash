#!/usr/bin/python

from ast import For
import os, sys

# Open a file
path = "C:/Users/murad/Desktop/videoHash/videos"
dirs = os.listdir( path )



from videohash import VideoHash

lookup_table = {}
os.chdir('videos')
# This would print all the files and directories
for file in dirs:
    vid =  VideoHash(file, frame_interval=5)
    if vid.hash in lookup_table:
        print('Collision')
        print('New: ', file, 'Old: ', lookup_table[vid.hash], 'hash: ', vid.hash)
        print('________________________________________')
        pass
    else:
        lookup_table[vid.hash] = file
        print('Name:',file,'  Hash -->', vid.hash)


def test2Vid(vid1, vid2):
    os.chdir('videos')
    print('Running Test')
    hash1 = VideoHash(vid1, frame_interval=5).hash
    hash2 = VideoHash(vid2, frame_interval=5).hash
    if hash1 == hash2:
        print('Failed')
    else:
        print('Passed')
# test2Vid('18.mp4', '22.mp4')
