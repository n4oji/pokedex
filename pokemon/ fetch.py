import requests


url = 'https://pokeapi.co/api/v2/'
select = 0

options = ['pokemon/', 'type/']

if select == 0:
    url += options[0]
    for i in range(1):
        response = requests.get(url+str(i+1))
        if response.status_code == 200:
            json = response.json()
            # print(json['name'], json['abilities'], json['height'], json['weight'],
            #   json['id'], json['sprites'], json['stats'], json['types'])
            print(json['abilities'])
