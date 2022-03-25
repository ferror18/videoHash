from videohash import VideoHash as vh

def video_hash(path, fi=5):
    return vh(path, frame_interval=fi).hash_hex