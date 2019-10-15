import urllib.request


def return_list_of_urls(match_id):
    full_url_list = []
    for match in match_id:
        url = "http://live.fanfooty.com.au/chat/"
        extension = ".txt"
        full_url = "{}{}{}".format(url, match, extension)
        full_url_list.append(full_url)
    return full_url_list


start_match = 7101
end_match = 7109
matches = list(range(start_match, end_match + 1))

list_of_urls = return_list_of_urls(matches)

for list in list_of_urls:
    print(list)

for url in list_of_urls:
    response = urllib.request.urlopen(url)
    webContent = response.read()
    filename = url[-8:]
    # f = open("C:/Users/Ken/PycharmProjects/supercoach_data/files/{}".format(filename), 'wb')
    f = open("C:/Users/Richa/PycharmProjects/sc_data/files/{}".format(filename), 'wb')
    f.write(webContent)
    print(filename)
