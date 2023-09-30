from urllib import response
import requests
import json

def PokeRequest():
    # 1 - Request Pokemon to find
    PokeReq = input("What Pokémon would you like to see? ")

    # 2 - Build API call URL combining PokeAPI main link + endpoint (PokeReq)
    PokeURL = "https://pokeapi.co/api/v2/pokemon/" + PokeReq
    
    ## Process Notifications ##
    print("Gotcha! Searching for " + PokeReq)
    print("...")
    print("...")
    print("...")
    print("...")

    # 3 - Make API request and save generated data in PokeRes var
    response = requests.get(PokeURL).json()
    
    # 4 - Save response into JSON file
    jsonName = "pokeapi/JSON_Files/PokeResult.json"
    save_to_file(response, jsonName)
    print("Found it! Here's the information retreived for " + PokeReq)

    # 5 - Read JSON file and display content
    PokeRes = read_from_file(jsonName)
    print(PokeRes)

def save_to_file(ApiData, jsonPath):
    filename = jsonPath
    with open(filename, 'w') as write_file:
        json.dump(ApiData, write_file, indent=2)

def read_from_file(filename):
    with open(filename, 'r') as read_file:
        PokeInfo = json.load(read_file)
    return PokeInfo

PokeRequest()