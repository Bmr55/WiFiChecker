import urllib.request

def wifi_connected(timeout=5):
    try:
        response = urllib.request.urlopen("https://www.google.com/", timeout=timeout)
        return True
    except:
        return False
