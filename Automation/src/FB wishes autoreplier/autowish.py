import sys
from urllib import urlencode
import requests
from urlparse import urlparse, parse_qs
from random import choice
import re
from datetime import datetime, date, time
import calendar

#settings

#your birthday: datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
bday = datetime(2014, 8, 25, 12, 30, 0)

#access_token: Generate one at https://developers.facebook.com/tools/explorer
access_token = "CAACEdEose0cBAO2yzpGTncORU3gUGZBcwAqj0ZAI5OSF2ZC2IBOh3LJa23Xso62tih2ZB74vOq4UF6YyDf3ktpoxQRWbrKZAd16OZCBaZAHMpexeklDhBSM4lOdSU9e6syLZA3uZBtbb5ZCQ6pIQx4kZBMZACxrDHKcZBxIIZBuGlnXuQ6SSbZCRw74zZCmbS8CmB9reaUrb4XMr7IZAc7lD2FZC6s6lE3dZBQbZBYmbPz8ZD"

#set true to like posts on your wall
like = False;

#set true to comment thank you
comment = True;

#the list of messages from which you want a random message to be selected
message_set = ['Thank you very much', 'Thanks a lot', 'Thank you!']

#if false, repies to every message. Make it false if you are sure every wish posted on your wall is a birthday message
use_filter = True

#keywords to respond to. Comment only on posts containing at lease one of these words
bdaywords = ["happy", "bday", "b\'day", "birthday","hbd", "wish", "returns", u"cumpleaños".encode("utf-8"),"anniversaire","compleanno","Geburtstag"]

#proxy settings
http_proxy = "https://proxy61.iitd.ernet.in:3128"
http_proxy = "https://proxy61.iitd.ernet.in:3128"
ftp_proxy = "proxy61.iitd.ernet.in:3128"

#do not change anything beyond this line

#calculate utc timestamp
epoch=datetime(1970,1,1)
td = bday - epoch
utc_bday = int((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6)

#create proxy dictionary
proxy_dict = {
    "http" : http_proxy,
    "https" : http_proxy,
    "ftp" : ftp_proxy
}

#get birthday wishes
def get_posts(url, wishes=None):
    #check if we are done
    if wishes is None:
        wishes = []
        stop = False
    else:
        until = parse_qs(urlparse(url).query).get('until')
        stop = int(until[0]) < utc_bday

    if stop:
        return wishes
    else:
        print url
        req = requests.get(url, proxies=proxy_dict)
        if req.status_code == 200:
            
            content = req.json()
            
            #keep only relevant fields from post data
            feed = []
            for post in content['data']:
                feed.append({'id': post['id'],'from': post['from']['name'],'message': post.get('message', ''),'type': post['type']})

            #keep only posts relevant to birthday. Make sure you reply your friends who post happy birthday pictures on your timeline or posts in local language
            for post in feed:
                if post['type']=='status' and is_birthday(post['message'], use_filter) :
                    wishes.append(post)
            
            next_url = content['paging']['next']
            
            return get_posts(next_url, wishes)
        else:
            print "Unable to connect. Check if session is still valid"

def confirm(prompt=None, resp=False):
    if prompt is None:
        prompt = 'Confirm'
    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False

def is_birthday (message, filter):
    if filter == False:
        return True
    for keyword in bdaywords:
        if keyword in message:
            return True
    return False

if __name__ == '__main__':
    
    #get bithday wishes
    base_url = 'https://graph.facebook.com/v2.1/me/feed'
    params = {'since': utc_bday, 'access_token': access_token}
    url = '%s?%s' % (base_url, urlencode(params))
    posts = get_posts(url)
    
    #confirm before posting
    usersignal = confirm('Found %s birthday wishes. Ready to thank them?' % (len(posts)))
    
    #post if user said yes
    if usersignal is True:
        for post in posts:

            #thank the user
            if comment:
                reply = choice(message_set)
                print 'Replying %s to %s' % (reply, wish['from'])
                url = 'https://graph.facebook.com/%s/comments?access_token=%s' % (wish['id'], access_token)
                requests.post(url, data={'message': reply}, proxies=proxy_dict)

            if like:
                url = 'https://graph.facebook.com/%s/likes?access_token=%s' % (wish['id'], access_token)
requests.post(url, data="", proxies=proxy_dict)