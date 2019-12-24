from requests import get
from json import loads


SHODAN_API_KEY = 'XXXXX'
URL = 'https://api.shodan.io/shodan/host/search'


params = {
    'key': SHODAN_API_KEY,
    'query': 'ics'
}
url = 'https://api.shodan.io/shodan/host/search?key=' + SHODAN_API_KEY + '&query=ics'
res = get(URL, params=params)
res = loads(res.text)['matches']
print(str(len(res)) + ' matches')
for el in res:
    print(el['isp'])
    print(el['ip_str'])
    print(el['port'])
    try:
        if 'compromised' in el['tags']:
            print('Compromised')
    except KeyError:
        print('Not Compromised')
    print()

