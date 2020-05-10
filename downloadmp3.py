
from urllib.request import Request, urlopen, urlretrieve

import requests
from bs4 import BeautifulSoup


def download_url(url):
    # assumes that the last segment after the / represents the file name
    # if the url is http://abc.com/xyz/file.txt, the file name will be file.txt
    file_name_start_pos = url.rfind("/") + 1
    file_name = url[file_name_start_pos:]

    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        print("reading url ", url)
        with open(file_name, 'wb') as f:
            for data in r:
                f.write(data)
    # download a sngle url
    # the file name at the end is used as the local file name
    # download_url("http://www.example.com")


def read_url(url):
    #url = url.replace(" ", "%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))
    for i in x:
        file_name = i.extract().get_text()
        url_new = url + file_name
        #url_new = url_new.replace(" ", "%20")
        if(file_name[-1] == '/' and file_name[0] != '.'):
            read_url(url_new)
        download_url(url_new)
        print(url_new)


read_url("http:www.example.com")
