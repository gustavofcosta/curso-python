import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O Site PUDIM não está acessível no momento')
else:
    print('O Site PUDIM está acessível')
