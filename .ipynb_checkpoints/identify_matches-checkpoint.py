import requests
import urllib.request

start_match = 6710
end_match = 7026
list_of_possible_match_ids = list(range(start_match, end_match + 1))
full_url_list = []


for match_id in list_of_possible_match_ids:
    url = "http://live.fanfooty.com.au/chat/"
    extension = ".txt"
    full_url = "{}{}{}".format(url, match_id, extension)
    full_url_list.append(full_url)

for url in full_url_list:
    # response = urllib.request.urlopen(url)
    response = requests.get(url)
    print(url, " ", response.status_code)


