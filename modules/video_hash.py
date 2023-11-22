from videohash import VideoHash as vh

def video_hash(key, path):
    return (key,vh(path, frame_interval=1).hash_hex)
# , frame_interval=fi