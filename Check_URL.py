from urllib.request import urlopen
import threading
def Check_Url(url):
    try:
        print("檢查網址")
        urlopen(url)
    except:
        return False
    else :
        return True
        print("網址正確")
        