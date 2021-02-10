import os
def download(url,download_playlist):
    if download_playlist == True:
        download_cmd = "--yes-playlist "
    else:
        download_cmd = "--no-playlist "
    CMD = "youtube-dl " + download_cmd + url
    os.system(CMD)

if __name__ == "__main__":
    download("https://www.youtube.com/watch?v=rMlk97ecKUw",False)