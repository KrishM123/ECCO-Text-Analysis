import urllib.request


def getHTMLPage(link):
    response = urllib.request.urlopen(link)
    player_dir = response.read()
    return str(player_dir)

