import requests
import pymongo
import json
from pymongo import MongoClient, InsertOne

#Mongo initializing
client = pymongo.MongoClient("localhost:27017")
db = client.pokemonDB
collection = db.pokemon
requesting = []
pokemonList = []

#Pokemon API initializing
baseUrl = "https://pokeapi.co/api/v2/pokemon/"


for i in range(1,152):
    tempUrl = baseUrl + str(i)
    response = requests.request("GET", tempUrl)
    pokemonList.append(response.json())

for pokemon in pokemonList:
    requesting.append(InsertOne(pokemon))

result = collection.bulk_write(requesting)
client.close()