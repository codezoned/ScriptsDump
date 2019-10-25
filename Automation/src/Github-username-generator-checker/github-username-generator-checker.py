import requests
from random_word import RandomWords
print("Wait while the script is loading...")

r = RandomWords()
words = r.get_random_words(includePartOfSpeech="adjective",limit=5)
name = input('Enter your name (Make sure you include space between first and last name):\n')

parts = name.split(' ')

usernames = []

def combinations():
	if(len(parts)==1):
		usernames.append(parts[0])
		usernames.append(parts[0][::-1])
		usernames.append(parts[0][::2])
		usernames.append(parts[0]+parts[0][::-1])
		for word in words:
			usernames.append(parts[0]+word)

	if(len(parts)==2):
		usernames.append(parts[0])
		usernames.append(parts[1])
		usernames.append(parts[0]+parts[1])
		usernames.append(parts[0]+'-'+parts[1])
		usernames.append(parts[1][0]+parts[0])
		usernames.append(parts[1][0]+'-'+parts[0])
		usernames.append(parts[0]+parts[1][0])
		usernames.append(parts[0]+'-'+parts[1][0])
		usernames.append(parts[0][0]+parts[1][1:])
		usernames.append(parts[1][0]+parts[0][1:])

	if(len(parts)>2):
		usernames.append(''.join([part[0] for part in parts]))
		usernames.append(''.join([part[:2] for part in parts]))
		usernames.append((''.join([part[:2] for part in parts])[::-1]))
		usernames.append((''.join([part[0] for part in parts]))[::-1])
		usernames.append(parts[0]+''.join(['-'+part[0] for part in parts[1:]]))
		usernames.append(parts[0]+''.join([part[0] for part in parts[1:]]))
combinations()
print('List of generated usernames are:')
print(usernames)
print('')

for username in usernames:
    res = requests.get('https://github.com/'+username)
    if res.status_code == 404:
        print(username+' is available')
    else:
    	print(username+' is already taken')