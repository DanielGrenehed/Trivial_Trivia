import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib2 import urlopen

class Web_Util:

    def __init__(self):
        pass

    @staticmethod
    def LoadPage(url):
        return urlopen(url).read()
