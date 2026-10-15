print("""PYTHON MIXTAPE MANAGER

1. View saved mixtapes
2. Add a new mixtape
3. Search by artist
4. Exit
""")

choice = input("Choose an option: ")

if choice == "1":
    print("Viewing saved mixtapes...")
elif choice == "2":
    print("Adding a new mixtape...")
elif choice == "3":
    print("Searching by artist...")
elif choice == "4":
    print("Goodbye!")
else:
    print("Invalid option. Please try again.")
