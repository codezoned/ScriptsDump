import cfscrape
import re
import urllib.request
import os

def link_finder(master_page):
    button_regex = re.compile(r'<a href="(.*)"><span>.*</span></a')
    page_source = scraper.get(master_page)
    issues_ = button_regex.findall(page_source.text)
    issues = ["http://readcomiconline.to" + issue + "&readType=1" for issue in issues_]
    return issues
def image_finder(issue_link):
    image_regex = re.compile(r'lstImages.push\("(\S+)"\)')
    page_source = scraper.get(issue_link)
    image_links = list(image_regex.findall(page_source.text))
    return image_links
def downloader_main(image_links):
    for x in range(0, len(image_links)):
        urllib.request.urlretrieve(image_links[x], str(x)+".png")

scraper = cfscrape.create_scraper()

def link_finder(master_page):
    scraper = cfscrape.create_scraper()
    button_regex = re.compile(r'href="(/Comic/.+/Issue.+)"')
    page_source = scraper.get(master_page)
    issues_ = button_regex.findall(page_source.text)
    issues = ["http://readcomiconline.to" + issue + "&readType=1" for issue in issues_]
    return issues

def image_finder(issue_link):
    scraper = cfscrape.create_scraper()
    image_regex = re.compile(r'lstImages.push\("(\S+)"\)')
    page_source = scraper.get(issue_link)
    image_links = list(image_regex.findall(page_source.text))
    return image_links

def downloader_main(name, master_page):
    cwd = os.getcwd()
    download_location = os.path.join(cwd, name)
    if not os.path.exists(download_location):
        os.makedirs(download_location)
    issues = link_finder(master_page)
    print(issues)
    for number in range(0, len(issues)):
            print("Currently Downloading Issue {}".format(str(number+1)))
            image_links = image_finder(issues[number])
            issue_location = os.path.join(download_location, "Issue "+str(number + 1))
            if not os.path.exists(issue_location):
                os.makedirs(issue_location)
            for x in range(0, len(image_links)):
                print("Downloading Page {}".format(str(x)))
                urllib.request.urlretrieve(image_links[x], os.path.join(issue_location, "Page" + str(x) + ".png"))

# To use, call the function downloader_main('Folder name you want the comic to be in', 'comic link')
# downloader_main('Infinity Countdown', 'http://readcomiconline.to/Comic/Infinity-Countdown')
