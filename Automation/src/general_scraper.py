from bs4 import BeautifulSoup as bs
from requests import get

class Scraper:
	
	def __init__(self, url, parser=None, headers=None):
		self.url = url
		self.parser = parser
		self.headers = headers

	def headers():
	    ua_one = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
	    ua_two = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	    headers = {'User-Agent': ua_one + ua_two}
	    return headers

	def get_piece(self, element, attribute, attribute_name, operation=None):
		header = Scraper.headers() if self.headers == None else self.headers
		parser = 'lxml' if self.parser == None else self.parser
		soup = bs(get(self.url, headers=header).text, parser)
		result = soup.find_all(element, { attribute : attribute_name})
		
		return operation(result) if operation != None else result 


# EXAMPLE
def lprint(this):
	for i in this:
		print(i.img)

Scraper('https://www.elfenix.com/').get_piece("div", "class", "coleql_height", operation=lprint)
