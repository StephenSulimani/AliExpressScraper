import requests
import re
import os
import urllib.request

def aliDownload(url):
    r = requests.get(url)
    x = re.findall(r"imagePathList\":(\[.*?\])", r.text)
    title = re.findall(r"<title>(.*?) on Ali", r.text)[0]
    directory = title.replace('\\', "").replace('/', "")
    images = x[0].split(',')
    os.mkdir(f"{os.getcwd()}\{directory}")
    i = 0
    while i < len(images):
        urllib.request.urlretrieve(images[i].strip('[').strip(']').strip('"'), f"{os.getcwd()}\{directory}\image{i+1}.jpg")
        i = i + 1
    print(f"Downloaded images to {directory}")

aliDownload(input("Aliexpress URL: "))