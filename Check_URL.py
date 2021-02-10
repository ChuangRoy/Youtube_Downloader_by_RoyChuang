from urllib.request import urlopen
def Check_Url(url):
    try:
        urlopen(url)
        return True
    except:
        return False
        