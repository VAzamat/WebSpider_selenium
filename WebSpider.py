#!/usr/bin/env python3

import os
import time

from bs4 import BeautifulSoup
import requests

import logging

from selenium import webdriver
import pyautogui


main_logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
    )

main_logger.info("запускаю основную программу")

main_logger.info("запускаю графический просмотр через браузер")
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-profile')
firefox_options.add_argument(os.environ.get('FirefoxProfilePath'))

firefox_options.set_preference("browser.download.dir", os.environ.get('FirefoxDestDir'))
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html, application/xhtml+xml")

browser = webdriver.Firefox(firefox_options)
time.sleep(2)


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
links.sort()

main_logger.info( links )

for item_url in links:
    main_logger.info(item_url)
    browser.get(item_url)
    time.sleep(2)

    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)

    filename = os.path.basename(item_url)
    filename_only = os.path.splitext(filename)[0]

    pyautogui.write(filename_only)
    pyautogui.press('enter')
    time.sleep(10)
