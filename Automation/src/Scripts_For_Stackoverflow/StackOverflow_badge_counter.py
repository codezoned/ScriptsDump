user_id = '22656'
url = 'http://api.stackexchange.com/2.2/users/'+user_id+'?order=desc&sort=reputation&site=stackoverflow'
import requests
response = requests.get(url)
json = response.json()
print('Total medals = {}'.format(json['items'][0]['badge_counts']['gold']+json['items'][0]['badge_counts']['silver']+json['items'][0]['badge_counts']['bronze']))
print('Bronze = {}'.format(json['items'][0]['badge_counts']['bronze']))
print('Silver = {}'.format(json['items'][0]['badge_counts']['silver']))
print('Gold = {}'.format(json['items'][0]['badge_counts']['gold']))
print('Current reputation = {}'.format(json['items'][0]['reputation']))
print('Reputation change today = {}'.format(json['items'][0]['reputation_change_day']))
print('Reputation change this week = {}'.format(json['items'][0]['reputation_change_week']))
