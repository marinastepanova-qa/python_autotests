import requests
token = '9060da5c209aab406b8c2b6e5754f19c'

creation = requests.post('https://pokemonbattle.me:9104/pokemons', 
headers={'Content-Type': 'application/json', 'trainer_token': token}, 
json={
    "name": "Красавчик",
    "photo": "https://dolnikov.ru/pokemons/albums/013.png"
})
print(creation.text)

change = requests.put('https://pokemonbattle.me:9104/pokemons', 
headers={'Content-Type': 'application/json', 'trainer_token': token}, 
json={
    "pokemon_id": 6035,
    "name": "Котик",
    "photo": "https://dolnikov.ru/pokemons/albums/013.png"
})
print(change.text)

pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
headers={'Content-Type': 'application/json', 'trainer_token': token}, 
json={
    "pokemon_id": "6035"
})
print(pokeball.text)

