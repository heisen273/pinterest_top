import requests
from operator import itemgetter

token = raw_input('\nenter access token:  ')

board = raw_input('\nenter board:  ')
link = 'https://api.pinterest.com/v1/boards/' + board + '/pins/?access_token='+token+'&fields=counts%2Curl'
#link = 'https://api.pinterest.com/v1/boards/' + board + '/pins/?access_token='+token+'&fields=counts'
r = requests.get(link)
data = r.json()

result = [] 
page = data['data']

while True:
    for item in page:
        result.append([item['url'], item['counts']['likes'] + item['counts']['comments'] + item['counts']['repins']])
    if data['page']['next'] != None:
        r = requests.get(data['page']['next'])
        data = r.json()
        page = data['data']
    else:
        break

print sorted(result, key=itemgetter(1))
#print result
