import time
from regex import R
import requests
import threading
from bs4 import BeautifulSoup

symbol = "%5ENSEI"
def set_url(symbol):
    return f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?region=US&lang=en-US&includePrePost=false&interval=5m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
url = set_url(symbol)
# print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36'}


def get_data():
    r = requests.get(url, headers=headers)
    objects = r.text
    print(objects)


def printit():
  threading.Timer(5.0, printit).start()
  get_data()



printit()



# f = open("demofile3.txt", "w+")
# print(objects,file = 'demofile3.js')
# f.close()
