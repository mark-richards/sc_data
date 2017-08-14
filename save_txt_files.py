import urllib.request


def return_list_of_urls(match_id):
    full_url_list = []
    for match in match_id:
        url = "http://live.fanfooty.com.au/chat/"
        extension = ".txt"
        full_url = "{}{}{}".format(url, match, extension)
        full_url_list.append(full_url)
    return full_url_list


matches = [
    6163,
    6164,
    6165,
    6166,
    6167,
    6168,
    6169,
    6170,
    6171,
    6172,
    6173,
    6174,
    6175,
    6176,
    6177,
    6178,
    6179,
    6180
]

list_of_urls = return_list_of_urls(matches)

for list in list_of_urls:
    print(list)

for url in list_of_urls:
    response = urllib.request.urlopen(url)
    webContent = response.read()
    filename = url[-8:]
    f = open("C:/Users/Ken/PycharmProjects/supercoach_data/files/{}".format(filename), 'wb')
    f.write(webContent)
    print(filename)
