from HTMLParser
import HTMLParser

import requests

links = []

class MyHTMLParser(HTMLParser):

   def handle_starttag(self, tag, attrs):

   if tag == "a": #checks whether anchor tag is present

for name, value in attrs: #name is href and value is url

if name == "href":

   links.append(value) # adds url to the array

search = raw_input("Enter a word to search : ")

r = requests.get("http://www.google.com/search?q=%s" % search)

# gets the search results webpage of google

htmlsource = r.text
# here if you print r.text it will show the whole html source code of the page so we need to extract the < a href = ..tags and print the value of the text

parser = MyHTMLParser()

parser.feed(htmlsource)# feed the html code to the parser

for i in range(0, len(links) - 1): #printing the list of links

print "#", i + 1, "  ", links[i]
