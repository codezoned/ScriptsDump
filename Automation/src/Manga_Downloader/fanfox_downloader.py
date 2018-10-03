# ============================================================================
# Author: Rodolfo Ferro Pérez
# GitHub: RodolfoFerro
# Twitter: @FerroRodolfo
#
# Script: Searches and downloads the top Manga result page
# by page from http://fanfox.net/. Script based on:
# github.com/codezoned/ScriptsDump/tree/master/Automation/src/Manga_Downloader
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ============================================================================


import requests
from bs4 import BeautifulSoup
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chapter = 1
page = 1
volume = 1
MangaName = ''
website = 'http://fanfox.net'


def downloadImg(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    for link in soup.find_all('img'):
        img = link.get("src")
        # print(img)
        response = requests.get(img)
        filename = os.path.split(img)[1]
        # print(filename)
        with open("%s.jpg" % filename, 'wb')as f:
            for chunk in response.iter_content(4096):
                f.write(chunk)


# need to change to phantom.js
# driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver = webdriver.Chrome()
driver.get(website)
searchBar = driver.find_element_by_xpath('//*[@id="lookupwords"]')
searchBar.send_keys(MangaName)
searchBar.send_keys(Keys.RETURN)
sleep(5)
selector = driver.find_element_by_xpath('//*[@id="searchbar"]/ol/li/select/option[text()="begin"]').click()
otherBar = driver.find_element_by_xpath('//*[@id="searchbar"]/ol/li/button[2]')
otherBar.send_keys(Keys.RETURN)
print(driver.current_url)

resp = requests.get(driver.current_url)
d = resp.text

s = BeautifulSoup(d, "lxml")
lis = s.find_all('a', href=True, class_='manga_img series_preview top')
manga = lis[0]['href']

url_base = 'http:' + manga
print(url_base)
vol = 'v{}'.format(volume)
chap = '/c{:03d}'.format(chapter)
pp = '/{}.html'.format(page)
url = url_base + vol + chap + pp

check = requests.get(url)
print(check)

while check:
    downloadImg(url)
    page = page + 1
    pp = '/{}.html'.format(page)
    url = url_base + vol + chap + pp
    print(url)
    check = requests.get(url)
