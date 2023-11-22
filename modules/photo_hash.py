from PIL import Image
import imagehash
import numpy
def binary_array_to_hex(arr):
	"""
	internal function to make a hex string out of a binary array.
	"""
	bit_string = ''.join(str(b) for b in 1 * arr.flatten())
	width = int(numpy.ceil(len(bit_string)/4))
	return '{:0>{width}x}'.format(int(bit_string, 2), width=width)

def photo_hash(key,path):
    types = {
        "a" : imagehash.average_hash,
        "d" : imagehash.dhash,
        "c" : imagehash.colorhash,
        "p" : imagehash.phash
    }
    img = Image.open(path)
    hs = types['p'](img)
    hs = binary_array_to_hex(hs.hash.flatten())
    return key,'0x'+hs

# print(photo_hash('C:/Users/murad/Desktop/videoHash/data/20201126_123457.jpg'))