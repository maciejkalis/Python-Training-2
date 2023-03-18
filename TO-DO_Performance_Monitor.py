"""
A simple program that gets data from the server in JSON format
and converts it into Python format.
The data are taken from test JSON placeholder service and contains,
among others, list of users with tasks to do.
The program counts the tasks performed by users and selects the user
with the highest number of completed tasks.

"""
import requests
import json
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_task_frequency(tasks):
    completedTaskFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if (entry["completed"] == True):
            completedTaskFrequencyByUser[entry["userId"]] += 1

    return completedTaskFrequencyByUser


def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())

    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Incorrect format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(
        completedTaskFrequencyByUser)


# Version 1

r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    if (user["id"] in usersWithTopCompletedTasks):
        print("Users with biggest amount of completed tasks is:", user["name"])

# Version 2

for userId in usersWithTopCompletedTasks:

    r = requests.get("https://jsonplaceholder.typicode.com/users/",
                     params="id=" + str(userId))
    user = r.json()
    print("Users with biggest amount of completed tasks is:", user[0]["name"])


# Version 3


def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = str("")

    lastIteration = len(my_list)
    i = 0
    for record in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(key) + "=" + str(record)
        else:
            conj_param += str(key) + "=" + str(record) + "&"

    return conj_param


conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks, "id")

r = requests.get(
    "https://jsonplaceholder.typicode.com/users/", params=conj_param)

users = r.json()

for user in users:
    print("Users with biggest amount of completed tasks is:", user["name"])
