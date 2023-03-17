"""
It's a simple website validator that takes the name of a file
that stores website URLs and checks their availability.

"""
import requests


def site_validator():
    fileName = input(
        "Type the name of file which contains websites to check against availability: ")

    sitesList = []
    validSites = []
    invalidSites = []

    with open(fileName + ".txt", "r", encoding="UTF-8") as file:
        for line in file:
            sitesList.append(line.replace("\n", ""))

        try:
            for site in sitesList:
                response = requests.get(site)

                if response.status_code == 200:
                    validSites.append(site)

                elif ((response.status_code == 404) or (response.status_code == 403)):
                    invalidSites.append(site)

        except requests.exceptions.MissingSchema:
            pass

    with open("valid_sites.txt", "a+", encoding="UTF-8") as file:
        for site in validSites:
            file.write(site + "\n")

    with open("invalid_sites.txt", "a+", encoding="UTF-8") as file:
        for site in invalidSites:
            file.write(site + "\n")


site_validator()
