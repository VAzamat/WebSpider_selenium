#!/usr/bin/env python3

import os

from bs4 import BeautifulSoup
import requests


def getAllLinks(url, include_only_parent=True):
    filename = os.path.basename(url)
    parent_path = url.replace(filename,"")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    a_tags = soup.find_all('a', href=True)

    links = [ os.path.join(parent_path,a.get('href')) for a in soup.find_all('a') if a.get('href').find(".html")>-1 ]
    return list( set(links) )

url = os.environ.get('MainSpiderUrl')
links = getAllLinks(url)
print( links )