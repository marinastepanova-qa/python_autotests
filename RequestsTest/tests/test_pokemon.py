import pytest
import requests

def test_status_code():
    response = requests.get('https://pokemonbattle.me:9104/pokemons')
    assert response.status_code == 200

def test_name_trainers():
    response = requests.get('https://pokemonbattle.me:9104/trainers', 
    params = {'trainer_id' : 3364})
    assert response.json()['trainer_name'] == 'Mari'