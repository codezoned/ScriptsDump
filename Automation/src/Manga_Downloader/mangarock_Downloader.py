#needs polishing
#Downloader From MangaRock!
#Searches and downloads the top Manga result page by page from https://mangarock.com/

import requests
from bs4 import BeautifulSoup
import os
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  


chapter=1
page=1
MangaName=''
website='https://mangarock.com/'


    

def downloadImg(url):
    r=requests.get(url)
    data=r.text
    soup = BeautifulSoup(data, "lxml")
    for  link in soup.find_all('img'):
        img=link.get("src")
        #print(img)
        response=requests.get(img)
        filename=os.path.split(img)[1]
        #print(filename)
        with open("%s.jpg" %filename,'wb')as f:
                for chunk in response.iter_content(4096):
                    f.write(chunk)
while True:
    try:
        chapter=1
        page=1
        MangaName=input('Enter the manga that you want to download : ')
        os.mkdir(MangaName)


        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        driver = webdriver.Chrome(  chrome_options=chrome_options)
        driver.get("https://www.mangapanda.com/search")
        searchBar = driver.find_element_by_xpath('//*[@id="searchinput"]')
        searchBar.send_keys(MangaName)
        searchBar.send_keys(Keys.RETURN)
        print(driver.current_url)
    
        resp=requests.get(driver.current_url)
        d=resp.text

        s=BeautifulSoup(d,"lxml")
        lis=s.find_all('a',href=True)
        manga=lis[7]['href']




        url=website+manga+'/'+str(chapter)+ '/'+str(page)

        check=requests.get(url)
        #print (check)
        cwd=os.getcwd()
        cwd=cwd+'/'+MangaName
        os.chdir(cwd)
        print("Downloading...")
        while check:
            downloadImg(url)
            page=page+1
            url=website+manga+'/'+str(chapter)+ '/'+str(page)
            print(manga+'/'+str(chapter)+'/'+str(page))
            check=requests.get(url)
    except FileExistsError:
        print("Manga already exists")
