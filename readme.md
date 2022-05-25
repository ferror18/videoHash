Collection-Organizer
===

This project is a collection organizer that helps you organize large video and photo collections by moving and renaming files, and detecting duplicates.

How to use it?
===
To use this software, you must have FFmpeg installed. Please read how to install FFmpeg if you don't already know how.

### Windows 

1. To use this software, you must have FFmpeg installed. Please read how to install FFmpeg if you don't already know how. 
2. Download the EXE file and put it in a folder that is is on the same level or higher than your collection.
 




## Install FFmpeg on Linux

  - APT (Debian, and Debian-based like Ubuntu)
```bash
sudo apt install ffmpeg
```

  - dnf (Fedora)
```bash
sudo dnf install ffmpeg
```

  - pacman (Arch Linux)
```bash
pacman -S ffmpeg
```

  - Termux (Android)
```bash
pkg install -y ffmpeg
```

  - Snap
> :warning: **Do not use Snap if you don't want to pass a storage_path while creating the VideoHash object.**: videohash stores instance generated files in the /tmp directory and snaps by design can't access the /tmp directory but only your /home and /snap.
```bash
sudo snap install ffmpeg
```

## Install FFmpeg on Windows
Steps are [based on video.stackexchange.com/a/20496](https://video.stackexchange.com/a/20496), note that the download site in the answer is outdated as of October 2021.
  - Download the `ffmpeg-git-full` variant from <https://www.gyan.dev/ffmpeg/builds/>. The direct link of the 7z archive is <https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z>.
  - Uncompress the archive.
  - Copy the bin directory from the decompressed folder, and paste inside `C:\Program Files\ffmpeg\`.
  - Right-click on "This PC" and navigate to `Properties > Advanced System Settings > Advanced tab > Environment Variables`.
  - In the Environment Variables window, click the "Path" row under the "Variable" column, then click Edit.
  - Click New and add `C:\Program Files\ffmpeg\bin\`to the list.
  - Click Ok on all the windows we opened. (Answer positive)

If you still have doubts read the answer <https://video.stackexchange.com/a/20496>, it has images.

Prefer video? <https://www.youtube.com/watch?v=qjtmgCb8NcE>.

## Install FFmpeg on macOS

  - Homebrew
```bash
brew install ffmpeg
```
</p>
</details>
