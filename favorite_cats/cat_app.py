"""
Simple application written to practice working with public APIs.
This particular app allows you to draw random cat image from publicly available,
training API available at https://thecatapi.com/.

Next, user authenticated via personal api key through header
is able to add the drawn cat to favorites and eventually delete desired item.

The app will work after adding your personal api key acquired
on https://thecatapi.com/ and pasting it into credentials.py.

"""
import requests
import json
import webbrowser
import credentials

from pprint import pprint


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Invalid format", response.text)
    else:
        return content


def get_favorite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get("https://api.thecatapi.com/v1/favourites/",
                     params, headers=credentials.headers)

    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search",
                     headers=credentials.headers)

    return get_json_content_from_response(r)


def add_favorite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }

    r = requests.post("https://api.thecatapi.com/v1/favourites/",
                      json=catData, headers=credentials.headers)

    return get_json_content_from_response(r)


def remove_cat_from_favorites(catToRemoveId):

    r = requests.delete("https://api.thecatapi.com/v1/favourites/" +
                        catToRemoveId, headers=credentials.headers)

    return get_json_content_from_response(r)


print("Hello, log in - enter your login and password")
# get login and password
# checking if the login and password are correct
# login was successful
# getting from the database userId and name - username

userId = "agh2m"
name = "Arkadiusz"

print("Hello " + name)
favoriteCats = get_favorite_cats(userId)
print("Your favorite cats are ", favoriteCats)
randomCat = get_random_cat()
print("A cat was drawn: ", randomCat[0]["url"])

webbrowser.open_new_tab(randomCat[0]["url"])

addToFavorites = input("Would you like to add it to your favorites? Y/N ")

if (addToFavorites.upper() == "Y"):
    pprint(add_favorite_cat(randomCat[0]["id"], userId))

else:
    print("The cat will not be added to favorites")

catsInFavorites = {
    favoriteCat['id']: favoriteCat['image']['url']
    for favoriteCat in favoriteCats
}

print(catsInFavorites)

catToRemoveId = input(
    "Enter ID of the cat you want to remove from favorites: ")

remove_cat_from_favorites(catToRemoveId)
