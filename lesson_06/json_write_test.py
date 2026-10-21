import json

test_album = {
    "artist": "Project Pat",
    "title": "Mista Don't Play",
    "rating": 8
}
with open("lesson_06/test_output.json", "w") as file:
    json.dump(test_album, file, indent=4)