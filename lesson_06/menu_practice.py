import json

try:
    with open("lesson_06/mixtapes.json", "r") as file:
        mixtapes = json.load(file)
except FileNotFoundError:
    mixtapes = []
except json.JSONDecodeError:
    print("ERROR: Mixtape data is corrupted!")
    raise

while True:
    print("""PYTHON MIXTAPE MANAGER
    1. View saved mixtapes
    2. Add a new mixtape
    3. Search by artist
    4. Exit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Viewing saved mixtapes...")
        if not mixtapes:
            print("No mixtapes saved yet!")
        else:
            for mixtape in mixtapes:
                print(f"Artist: {mixtape['artist']} | Album: {mixtape['title']} | Rating: {mixtape['rating']}")
    
    elif choice == "2":
        print("Adding a new mixtape...")
        artist = input("Enter artist name: ")
        title = input("Enter album name: ")
        rating = int(input("Enter rating: "))
        new_mixtape = {
            "artist": artist,
            "title": title,
            "rating": rating
        }
        mixtapes.append(new_mixtape)
        with open("lesson_06/mixtapes.json", "w") as file:
            json.dump(mixtapes, file, indent=4)
        print(new_mixtape)
    
    elif choice == "3":
        print("Searching by artist...")
        search_artist = input("Enter artist name: ")
        print(f"Searching for: {search_artist}")
        found = False

        for mixtape in mixtapes:
            if search_artist == mixtape["artist"]:
                print(f"Artist: {mixtape['artist']} | Album: {mixtape['title']} | Rating: {mixtape['rating']}")
                found = True

        if not found:
            print(f"No mixtapes found for {search_artist}")
                
                 
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
