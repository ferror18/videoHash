from videohash import VideoHash as vh

def video_hash(path, fi=10):
    # return vh(path=path, frame_interval=fi, ffmpeg_path="C:\\Users\\murad\\Desktop\\videoHash\\ffmpeg\\bin").hash_hex
    return vh(path, frame_interval=fi).hash_hex