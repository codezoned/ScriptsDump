from requests import get
from urllib.parse import urljoin
from os import path, getcwd
import os
from bs4 import BeautifulSoup as soup
from sys import argv
import os,sys

def get_page(base_url):
    req= get(base_url)
    if req.status_code==200:
        return req.text
    raise Exception('Error {0}'.format(req.status_code))

def get_all_links(html):
    bs= soup(html,"html.parser")
    links= bs.findAll('a')
    print(links)
    return links

def get_pdf(base_url, base_dir):
    html= get_page(base_url)
    links= get_all_links(html)
    if len(links)==0:
        raise Exception('No links found on the webpage')
    n_pdfs= 0
    os.chdir('output_pdfs')
    for link in links:
        print(link)
        break
        if link['href'][-4:]=='.pdf':
            n_pdfs+= 1
            content= get(urljoin(base_url, link['href']))
            #if content.status==200 and content.headers['content-type']=='application/pdf':
            with open(link.text+'.pdf', 'wb') as pdf:
                pdf.write(content.content)
    if n_pdfs==0:
        raise Exception('No pdfs found on the page')
    #print "{0} pdfs downloaded and saved in {1}".format(n_pdfs, base_dir)


if __name__ == "__main__":
	
	
	if(len(sys.argv)!=2):
		print("Invalid number of Arguments")
		raise SystemExit
	else:
		url_path = sys.argv[1]
		output_path=os.getcwd()
		get_pdf(url_path,output_path)