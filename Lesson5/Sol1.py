import json

fn = "hard-python/Lesson5/data/01_data.json"

with open(fn) as f:
    persons = json.load(f)

for person in persons:
    print(person['email'])