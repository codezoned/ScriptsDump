"""

	Written by Sagar Vakkala @ionicc
	Original repository: https://github.com/ionicc/Youtube-mp3-downloader-light

"""

import re, urllib, os, sys
import urllib.request
import urllib.parse

user_input = input
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()
urlopen = urllib.request.urlopen

def get_title(url):
    website = urlopen(url).read()
    title = str(website).split('<title>')[1].split('</title>')[0]
    return title

def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def init_message():
    print("Built with <3 By Sagar Vakkala (^^) \n")
    print("YOUTUBE MP3 DOWNLOADER LIGHT \n \n")

def exit_message(t):
    print("\n %s Has been downloaded" % t)


def download(song=None):
    if not song:
        song = user_input('Enter the name of the song or the URL: ')

    if "youtube.com/" not in song:

        try:
            query = encode({"search_query" : song})
            web_content = urlopen("http://www.youtube.com/results?" + query)
            results = re.findall(r'href=\"\/watch\?v=(.{11})', web_content.read().decode())
        except:
            print("There's some problem in your network")
            return none

        command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + results[0]

    else:
        command = 'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + song[song.find("=")+1:]
        song = get_title(song)
        print(song)

    try:
        print("Downloading %s" % song)
        os.system(command)
        exit_message(song)
        download()
    except:
        print('Error downloading %s' %song)
        return None

def main():
    try:
        screen_clear()
        init_message()
        download()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
    exit(0)
