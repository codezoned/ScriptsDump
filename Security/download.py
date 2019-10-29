import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")
    with open(file_name[-1], "wb") as outfile:
        outfile.write(get_response.content)



download("https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fst.motortrend.com%2Fuploads%2Fsites%2F5%2F2017%2F11%2F2020-Tesla-Roadster-11.jpg&f=1")
