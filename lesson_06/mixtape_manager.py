#6J - Variables, Keys, and Creating Dictionaries

# mixtapes = [] → Creates a list, represented by square brackets.
# new_mixtape = {} → Creates a dictionary, represented by curly braces.
# mixtapes.append(new_mixtape) → Puts the dictionary inside the list.

mixtapes = []

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