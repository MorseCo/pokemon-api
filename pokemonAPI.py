from http.client import REQUEST_ENTITY_TOO_LARGE
from flask import Flask, render_template, request, url_for, jsonify, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pymongo
import json
from pymongo import MongoClient, InsertOne
from bson.json_util import dumps
import random
from flask_cors import CORS, cross_origin
import certifi


#Simplified Object for pokemon
class SimplePokemon:
    def __init__(self, id, name, type, height, weight):
        self.id = id
        self.name = name
        self.type = type
        self.height = height
        self.weight = weight

#========== Local Mongo ==========
# client = pymongo.MongoClient("localhost:27017")
#=================================

#========== Cloud Mongo ==========
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://guest:hackedu@cluster0.3wbon.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
#=================================

db = client["pokemonDB"]
col = db["pokemon"]

authorizedAPIKeys = ['YXNoOmtldGNodW0=']

#Flask setup
app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def status_check():
    return jsonify({"status": "UP"})


@app.route('/pokemon/<pokemon>', methods=['GET'])
def getPokemonName(pokemon):
    query = {}
    try:
        pokemonInt = int(pokemon)
        query = {"id": pokemonInt}
    except:
        query = {"name": pokemon}
    return getPokemonWithQuery(query)


@app.route('/pokemon/simple/<pokemon>', methods=['GET'])
def getSimplePokemonName(pokemon):
    query = {}
    try:
        pokemonInt = int(pokemon)
        query = {"id": pokemonInt}
    except:
        query = {"name": pokemon}
    return getSimplePokemonWithQuery(query)


@app.route('/pokemon/random/', methods=['GET'])
def getRandomPokemon():
    randomInteger = random.randint(1,151)
    query = {"id": randomInteger}
    return getPokemonWithQuery(query)


@app.route('/pokemon/simple/random/', methods=['GET'])
def getSimpleRandomPokemon():
    randomInteger = random.randint(1,151)
    query = {"id": randomInteger}
    return getSimplePokemonWithQuery(query)


def getPokemonWithQuery(myQuery):
    try:
        pokemon = col.find(myQuery)[0]
    except:
        return({"Error": "Pokemon not found"})
    return json.loads(dumps(pokemon))


def getSimplePokemonWithQuery(myQuery):
    try:
        pokemon = col.find( myQuery, {"name":1, "id": 1, "types": 1, "height": 1, "weight": 1 } )[0]
    except:
        return({"Error": "Pokemon not found"})
    typeList = []
    for types in pokemon["types"]:
        typeList.append(types["type"]["name"])
    simplePokemon = SimplePokemon(pokemon["id"], pokemon["name"], typeList, pokemon["height"], pokemon["weight"])
    return(vars(simplePokemon))
