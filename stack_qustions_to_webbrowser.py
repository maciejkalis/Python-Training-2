"""
Script opens new tabs with questions from Stack Overflow based on provided parameters.
The program was written to practice some features from webbrowser library.

"""
import requests
import json
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days=30)

searchDate = datetime.today() - timeBefore

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": int(searchDate.timestamp()),
    "tagged": "python",
    "min": 15
}


r = requests.get("https://api.stackexchange.com/2.3/questions", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
