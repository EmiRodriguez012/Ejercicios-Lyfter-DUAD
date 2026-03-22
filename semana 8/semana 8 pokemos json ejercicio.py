import json

def open_file(file_path):
    with open (file_path, "r") as file:
        data = json.load(file)
    return data

def get_pokemon_data():

    name = input("Please enter Pokemon namen: ")
    poke_type = input("Please enter Pokemon type: ")

    hp= int(input("Please enter Pokemon HP: "))
    attack= int(input("Please enter Pokemon attack: "))
    defense= int(input("Please enter Pokemon defense: "))
    sp_attack= int(input("Please enter Pokemon speed attack: "))
    sp_defense= int(input("Please enter Pokemon speed defense: "))
    speed= int(input("Please enter Pokemon speed: "))

    new_pokemon= {
        "name": {
            "english": name
        },
        "type": [poke_type],
        "base": { 
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed 
        } 
    return new_pokemon
}

def save_new_pokemon():
    with open("pokemons.json", "w") as file:
    json.dump(data, file, indent=4)

def main():

    file_path = "pokemons.json"

    data = open_file(file_path)

    new_pokemon = get_pokemon_data()

    data.append(new_pokemon)

    save_new_pokemon(file_path, data)

    print("Pokemon added successfully!")

main()



