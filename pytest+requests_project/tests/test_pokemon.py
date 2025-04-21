import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
trainer_token = 'Тут нужно вставить свой токен'
HEADER = {'Content-Type' : 'application/json', 
          'trainer_token' : trainer_token}
trainer_id = '28614'
trainer_name = 'HardStyle'

def test_get_trainers():
    trainers_response = requests.get (url = f'{URL}/trainers', headers = HEADER)
    assert trainers_response.status_code == 200


def test_get_trainer_name():
    responce_get = requests.get (url = f'{URL}/trainers', headers = HEADER, params =  {'trainer_id' : trainer_id})
    assert responce_get.json()['data'][0]['trainer_name'] == trainer_name
