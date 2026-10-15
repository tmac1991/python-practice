#6J- - Variables, Keys, and Creating Dictionaries

import json

# mixtapes = [] → Creates a list, represented by square brackets.
# new_mixtape = {} → Creates a dictionary, represented by curly braces.
# mixtapes.append(new_mixtape) → Puts the dictionary inside the list.

## mixtapes = []

with open("mixtapes.json", "r") as file: # <-replaces the mixtapes list for 6M (load, new inputs, append, save)
    mixtapes = json.load(file)

artist = input("Enter artist name: ")
title = input("Enter album title: ")
rating = int(input("Enter rating: "))

new_mixtape = {
    "artist": artist,
    "title": title,
    "rating": rating
}

mixtapes.append(new_mixtape)

print(mixtapes)

with open("mixtapes.json", "w") as file:
    json.dump(mixtapes, file, indent=4)
    