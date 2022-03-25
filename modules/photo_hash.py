from pprint import pprint
from PIL import Image
import imagehash

def photo_hash(path, type='p'):
    types = {
        "a" : imagehash.average_hash,
        "d" : imagehash.dhash,
        "c" : imagehash.colorhash,
        "p" : imagehash.phash
    }
    img = Image.open(path)
    return types[type](img)