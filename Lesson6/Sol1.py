import random
import json
import requests

fn = "hard-python/Lesson6/data/authors.json"
deezer_API_URL = "https://api.deezer.com/artist/{}"

with open(fn) as f:
    authors_json = json.load(f)

def get_random_authors():
    return [random.choice(list(authors_json.items())) for i in range(2)]

def make_question(authors):
    usr_idx = int(input(f"Which one of this two authors have published more album between '{authors[0][0]}' (1) and '{authors[1][0]}' (2)? "))
    if usr_idx not in [1, 2]:
        raise ValueError("Please insert a valid value!")
    return usr_idx

def get_album_num(author_id):
    return requests.get(deezer_API_URL.format(author_id)).json()["nb_album"]

def print_response(usr_idx, albums_num):
    other_response = len(albums_num) - usr_idx
    if albums_num[usr_idx - 1] > albums_num[other_response]:
        print("Congratulations, you win!!!!")
    else:
        print("Sorry, you loose.")

keep_asking = True
while keep_asking:    
    extracted_auth = get_random_authors()
    try:
        albums_num = [get_album_num(extracted_auth[0][1]), get_album_num(extracted_auth[1][1])]
        usr_idx = make_question(extracted_auth)
        print_response(usr_idx, albums_num)
    except ValueError as exc:
        print(exc)
    
    keep_asking = input("Do you want to try again (Y) or exit (any char)? ") == 'Y'