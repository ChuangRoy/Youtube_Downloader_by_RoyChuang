import subprocess as sp
# import os


def download(url,download_playlist):
    if download_playlist == True:
        download_cmd = "--yes-playlist "
    else:
        download_cmd = "--no-playlist "
    CMD = "youtube-dl " + download_cmd + ' " '  + url + ' " '
    print(CMD)
    # os.system(CMD)
    process = sp.Popen(CMD)
    process.wait()
    return process.returncode
    

if __name__ == "__main__":
    download("https://www.youtube.com/watch?v=rMlk97ecKUw",False)