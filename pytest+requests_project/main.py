import requests

URL = 'https://api.pokemonbattle.ru'

trainer_token = '4aec91b10e9a2a91cc56534c60c4ec82'

HEADER = {'Content-Type' : 'application/json', 
          'trainer_token' : '49bd5830941b58208b1ecda1f28e5376'}

create_body = {
    "name": "Кот",
    "photo_id": -1
}

response_create = requests.post (url = f'{URL}/v2/pokemons', headers = HEADER ,  json = create_body)
print (response_create.text)

resp_pok_id = response_create.json() ['id']

change_body = {
    'pokemon_id': resp_pok_id,
    'name': "Пес",
    'photo_id': -1
}

response_change = requests.put (url = f'{URL}/v2/pokemons', headers = HEADER ,  json = change_body)
print (response_change.text)

add_pok_resp = requests.post (url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER ,  json = {'pokemon_id' : resp_pok_id})

print (add_pok_resp.text)