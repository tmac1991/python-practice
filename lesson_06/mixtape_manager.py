#6J-O - Variables, Keys, Persistent storage, json, and Creating Dictionaries

import json

# mixtapes = [] → Creates a list, represented by square brackets.
# new_mixtape = {} → Creates a dictionary, represented by curly braces.
# mixtapes.append(new_mixtape) → Puts the dictionary inside the list.

#! with open("mixtapes.json", "r") as file: 
#!     mixtapes = json.load(file)  
try:
    with open("mixtapes.json", "r") as file:
        mixtapes = json.load(file)
except FileNotFoundError:
    mixtapes = []    
# except json.JSONDecodeError:
#     print("SWOUP! This JSON is more fucked up than DJ Paul's hand!")    
except json.JSONDecodeError:
    print("SWOUP! This JSON is corrupted!")
    raise

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
    