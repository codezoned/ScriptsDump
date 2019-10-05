import stackapi
from html2text import html2text
import sys
import requests

class Stackoverflow_Top_Tags():
    def __init__(self, stackexchange_id):
        self.id = int(stackexchange_id)
        self.top_tags = ''
        self.post_text =''

    def get_user_info(self):
        url = 'http://api.stackexchange.com/2.2/users/'+str(self.id) +'?order=desc&sort=reputation&site=stackoverflow'
        response = requests.get(url)
        json = response.json()
        print('\nTotal medals = {}'.format(json['items'][0]['badge_counts']['gold']+json['items'][0]['badge_counts']['silver']+json['items'][0]['badge_counts']['bronze']))
        print('Bronze = {}'.format(json['items'][0]['badge_counts']['bronze']))
        print('Silver = {}'.format(json['items'][0]['badge_counts']['silver']))
        print('Gold = {}'.format(json['items'][0]['badge_counts']['gold']))
        print('Current reputation = {}'.format(json['items'][0]['reputation']))
        print('Reputation change today = {}'.format(json['items'][0]['reputation_change_day']))
        print('Reputation change this week = {}'.format(json['items'][0]['reputation_change_week']))

    def get_top_tags(self):
        site = stackapi.StackAPI('stackoverflow')
        fields = site.fetch('users/{ids}/top-tags' , ids=[self.id])
        top_fields = fields['items'][:10]
        str = ""
        print("\nTOP TAGS:")
        for field in list(top_fields):
            str += field['tag_name'] + " ; "
        print(str + '\n')

    def get_posts_with_top_votes(self):
        site = stackapi.StackAPI('stackoverflow' , client_id = "15775")
        site.max_pages = 1
        site.page_size = 10
        fields = site.fetch('users/{ids}/posts' , ids=[int(self.id)] , site="stackoverflow",sort='votes' , filter='withbody' ,order="desc")['items']
        print("\nREPUTATION: %d \n" %fields[0]["owner"]["reputation"])
        for field in fields:
            print("POST TYPE: %sPOST CONTENT:\n%s" %(html2text(field['post_type']), html2text(field['body'])))

if (__name__ == "__main__"):
    try:
        obj = Stackoverflow_Top_Tags(sys.argv[1])
        obj.get_user_info()
        obj.get_top_tags()
        obj.get_posts_with_top_votes()
    except:
        print('Invalid user ID!')