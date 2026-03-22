dictionary = {
    "player": "Messi",
    "entrepeneur" : "Elon Musk",
    "artist": "Chris martin",
    "President": "Donald Trump" 
}

keys_to_delete = ["player", "artist"]

for element in keys_to_delete:
    dictionary.pop(element, None)

print(dictionary)