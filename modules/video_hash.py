from videohash import VideoHash as vh

def video_hash(key, path, fi=1):
    return (key,vh(path, frame_interval=fi).hash_hex)