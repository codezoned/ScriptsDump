#Displays Lyrics of song directly in terminal
#usage: python lyricsFetch.py [Artist_name] [song_name]
from bs4 import BeautifulSoup
import os
import sys
import requests
import webbrowser
import urllib2

if len(sys.argv)>1:
	detail='/'.join(sys.argv[1:])
else:
	print('Please try again')
	sys.exit(1)


songurl='http://www.azlyrics.com/lyrics/'+detail+'.html'
page=urllib2.urlopen(songurl)

soup=BeautifulSoup(page,'lxml')

name_box=soup.find('div',attrs={'class':'lyricsh'})
name=name_box.text.strip()

print '\n'
print name
print '\n'

for foo in soup.find_all('div',attrs={'class':'col-xs-12 col-lg-8 text-center'}):
	lyric_box=foo.find('div',attrs={'class':None})
	lyric=lyric_box.text.strip()
	print lyric


