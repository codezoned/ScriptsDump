import requests
from bs4 import BeautifulSoup
import os

query = input('What manga would you like to search for?: ')
website = 'https://www.mangareader.net' 

def download_image(url, manga_name):
    response = requests.get(url)
    file_name = os.path.split(url)[1]

    if (not os.path.exists('manga')):
        os.makedirs('manga')

    if (not os.path.exists('manga/%s' % manga_name)):
        os.makedirs('manga/%s' % manga_name)

    with open("manga/%s/%s" % (manga_name, file_name), 'wb') as f:
        for chunk in response.iter_content(4096):
            f.write(chunk)

 
# Get the search page with query and find all results
search_results = BeautifulSoup(
    requests.get('%s/search/?w=%s' % (website, query)).text,
    'html.parser'
).find_all("div", class_="manga_name")

# Use list comprehension to create an array of the manga names/hrefs
manga_list = [manga.contents[1].contents[1].contents[0] for manga in search_results]

# If array is less than one, no results were found
if (len(manga_list) > 1):
    [print('%i) %s' % (i, manga.text)) for i, manga in enumerate(manga_list)]
    choice = int(input('Choose which manga you would like to download: '))
    chosen_manga = manga_list[choice]
elif (len(manga_list)):
    chosen_manga = manga_list[0]
else:
    print('Sorry but no search results were found.')
    exit()

# Create a recursive function to scrape through manga pages
def scrape_pages(url, manga_name):
    # Get page and target the imgholder element's first a tag
    image = BeautifulSoup(
        requests.get(url).text,
        'html.parser'
    ).find(id='imgholder').a

    # If the tag was found, and there is an image with the id image, there is a link and image to scrape
    if (image and image.find(id='img')):
        download_image(image.find(id='img').get('src'), manga_name)
        scrape_pages('%s%s' % (website, image.get('href')), manga_name)
    else:
        print('No more pages found!')

# Call recursive function
scrape_pages('%s%s/1' % (website, chosen_manga.get('href')), chosen_manga.text)
