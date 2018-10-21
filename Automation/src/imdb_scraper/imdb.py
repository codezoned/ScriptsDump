import requests  #for imdb movie requests.

from bs4 import BeautifulSoup  #Beautifulsoup for desktop notif.

print('Enter movie/Tv series name')

movie = input()

print()

url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=all'  #imdb's search API.

def get_title(movie_url):
    source_code = requests.get(movie_url)   #getting movie imdb page url from user input.
    plain_text = source_code.text #convert to plain text
    soup = BeautifulSoup(plain_text, 'lxml')
    for title in soup.findAll('div', {'class': 'title_wrapper'}):
        return title.find('h1').text.rstrip()

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')
for td in soup.findAll('td', {'class': 'result_text'}):
    href = td.find('a')['href']  #find movie page in imdb
    movie_page = 'http://www.imdb.com' + href
    break


movie_name = get_title(movie_page)

def get_movie_data(movie_url):  #getting movie data like reviews and genre.
    source_code = requests.get(movie_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for div in soup.findAll('div', {'class': 'ratingValue'}):
        print('Imdb rating of the movie/Tv Series "' + movie_name + '" is: ', end = '') #showing movie rating as a desktop notification
    print(div.text)
    print()
    for div in soup.findAll('div', {
        'class': 'summary_text'
        }):
        print('Summary of the movie/Tv series:')  #showing summary of movie as desktop notif.
        print(div.text.lstrip())

get_movie_data(movie_page)

'''print_genre = soup.findAll('
div ',{'
class ':'
subtext '})

for div in print_genre:

  for genre in print_genre.findAll('a'):

  print(genre.text, end = ' |')   #showing genre.

print()
'''
