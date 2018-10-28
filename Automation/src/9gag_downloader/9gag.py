import requests
from StringIO import StringIO
from PIL import Image

no_of_memes = 100

data = requests.get("https://9gag.com/v1/group-posts/group/default/type/hot")
datajson = data.json()
posts = datajson['data']['posts']
image_links = [elem['images']['image700']['url'] for elem in posts]
last_code = image_links[-1].split("/")[-1].split("_")[0]

for i in range((no_of_memes)/10):
	for elem in image_links:
		resp = requests.get(elem)
		fil = StringIO(resp.content)
		img = Image.open(fil)
		img.save(elem.split("/")[-1])
	data = requests.get("https://9gag.com/v1/group-posts/group/default/type/hot"+"?after="+last_code)
	datajson = data.json()
	posts = datajson['data']['posts']
	image_links = [elem['images']['image700']['url'] for elem in posts]
	last_code = image_links[-1].split("/")[-1].split("_")[0]
