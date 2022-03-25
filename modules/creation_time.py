import os,platform,datetime
from pprint import pprint

'''
Getting some sort of modification date in a cross-platform way is easy - just call os.path.getmtime(path) and you'll get the Unix timestamp of when the file at path was last modified.

Getting file creation dates, on the other hand, is fiddly and platform-dependent, differing even between the three big OSes:

On Windows, a file's ctime (documented at https://msdn.microsoft.com/en-us/library/14h5k7ff.aspx) stores its creation date. You can access this in Python through os.path.getctime() or the .st_ctime attribute of the result of a call to os.stat(). This won't work on Unix, where the ctime is the last time that the file's attributes or content were changed.
On Mac, as well as some other Unix-based OSes, you can use the .st_birthtime attribute of the result of a call to os.stat().
On Linux, this is currently impossible, at least without writing a C extension for Python. Although some file systems commonly used with Linux do store creation dates (for example, ext4 stores them in st_crtime) , the Linux kernel offers no way of accessing them; in particular, the structs it returns from stat() calls in C, as of the latest kernel version, don't contain any creation date fields. You can also see that the identifier st_crtime doesn't currently feature anywhere in the Python source. At least if you're on ext4, the data is attached to the inodes in the file system, but there's no convenient way of accessing it.

The next-best thing on Linux is to access the file's mtime, through either os.path.getmtime() or the .st_mtime attribute of an os.stat() result. This will give you the last time the file's content was modified, which may be adequate for some use cases.
'''

def get_time_in_seconds_from_epoch(path):
    if platform.system() == 'Windows':
        return os.path.getctime(path)
    else:
        stat = os.stat(path)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
def get_creation_time(path):
    creationTime = get_time_in_seconds_from_epoch(path)
    creationTime = datetime.datetime.fromtimestamp(creationTime)
    creationTime = creationTime.strftime('%Y-%m-%d-%H:%M:%S')
    return creationTime