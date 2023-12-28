
# Online Python - IDE, Editor, Compiler, Interpreter
from Poke import Pokemon
from Battle import Battle
from Gui import GUI
import requests   


def reqPokemon(target):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{target.lower()}')    

    if response.status_code != 200:
        raise Exception("Pokemon name must be valid")
    
    json = response.json()
    resultName = json['name']
    resultType = json['types'][0]['type']['name']
    resultHealth = json['stats'][0]['base_stat']
    resultAttack = json['stats'][1]['base_stat']
    resultDefense = json['stats'][2]['base_stat']
    resultSpeed = json['stats'][5]['base_stat']

    print(f"You selected {target} who is a {resultType} type!")

    response = requests.get(f"https://pokeapi.co/api/v2/type/{resultType}/")
    json = response.json()
        
    damage_relations = json['damage_relations']["double_damage_from"]
    weaknesses = []

    for entry in damage_relations:
        weaknesses.append(entry['name'])

    print(weaknesses)


    return Pokemon(resultName, resultType, 1, resultHealth, resultAttack, resultDefense, resultSpeed, weaknesses)

def Main():
    print("Welcome to the pokemon battler.")
    interface = GUI()

    # input_one = input("Please enter a pokemon name: ")
    # pokemon_one = reqPokemon(input_one)

    # input_two = input("Please enter a second pokemon name: ")
    # pokemon_two = reqPokemon(input_two)
    
    # battle = Battle(pokemon_one, pokemon_two)
    # battle.run_battle()

    
Main()


