import numpy as np

places = [
    {"name": "Miami", "description": "", "longitude": None, "email": ""},
    {"name": "New York", "description": "The greatest city in the world by far that's a fact", "longitude": 22.567686, "email": "robk@email.com"},
    {"name": "New York", "description": "The greatest city in the world", "longitude": 22.567686, "email": ""}
]


for place in places:
    required_fields = {
                "name": place['name'],
                "description": place['description'],
                "longitude": place['longitude']
            }
    word_count = np.char.count(required_fields['description'], ' ') + 1
    print(word_count)
    if not all(required_fields.values()) or word_count < 50:
        print(f"skipped {required_fields['name']}")
        continue
    print(f"{required_fields['name']} passed check")


# if not any(place.values())

# for place in places:
#     if not all(place.values()):
#     # if (place['name'] or place['description']
#     #         or place['longitude'] or place['email'] is None):

#         print("skipped this one")
#         continue
#     print(place)

# for place in places:
#     required_fields = {place["name"], place["description"], place["longitude"]}
#     if not any(required_fields.values()):
#         print("skipped this one")
#         continue
#     print(place)
