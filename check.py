import urllib.request

def wifi_connected():
    try:
        response = urllib.request.urlopen("https://www.google.com/", timeout=5)
        return True
    except:
        return False
