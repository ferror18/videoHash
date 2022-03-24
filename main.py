#!/usr/bin/python

import os, sys

# Open a file
path = "C:/Users/murad/Desktop/videoHash/data"
dirs = os.listdir( path )



from videohash import VideoHash

# lookup_table = {}
# os.chdir('videos')
# # This would print all the files and directories
# for file in dirs:
#     vid =  VideoHash(file, frame_interval=5)
#     if vid.hash_hex in lookup_table:
#         print('Collision')
#         print('New: ', file, 'Old: ', lookup_table[vid.hash_hex], 'hash: ', vid.hash_hex)
#         print('________________________________________')
#         pass
#     else:
#         lookup_table[vid.hash_hex] = file
#         print('Name:',file,'  Hash -->', vid.hash_hex)


def test2Vid(vid1, vid2, fi=5):
    print('Running Test')
    hash1 = VideoHash(vid1, frame_interval=fi).hash_hex
    hash2 = VideoHash(vid2, frame_interval=fi).hash_hex
    if hash1 == hash2:
        print('Failed')
    else:
        print('Passed')
# test2Vid('18.mp4', '22.mp4')
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 

print(video_hash(path+'/25.mp4'))
print(photo_hash('art.jpg'),'photo hash')