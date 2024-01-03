import requests 
from Poke import Pokemon

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
    resultSprites = (json['sprites']['front_default'], json['sprites']['back_default'])


    print(f"You selected {target} who is a {resultType} type!")

    response = requests.get(f"https://pokeapi.co/api/v2/type/{resultType}/")
    json = response.json()
        
    damage_relations = json['damage_relations']["double_damage_from"]
    weaknesses = []

    for entry in damage_relations:
        weaknesses.append(entry['name'])


    return Pokemon(resultName, resultType, 1, resultHealth, resultAttack, resultDefense, resultSpeed, weaknesses, resultSprites)

class Data:
    num_selected = 0
    pk1 = ""
    pk2 = ""
    battle_over_text = ""
    winner = ""
    print("data init")

    @classmethod
    def create_new_instance(cls):
        # Class method to create a new instance
        return cls()

    def delete_self(self):
        # Optionally, you can perform some cleanup before deleting
        print(f"Deleting instance with name data")

        # Remove the instance from the instances list
        # Data.instances.remove(self)

        # Delete the instance
        del self

        return Data.create_new_instance()

data = Data()

