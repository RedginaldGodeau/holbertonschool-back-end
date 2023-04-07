#!/usr/bin/python3
"""
    Python script to export data in the JSON format.
"""
import json


def GetAPI(url=None):
    """
     Get data from API URL.
     This function is used to get data from the API URL.
     If you want to get data from a different URL you can use this function.

     @param url - URL of the API.
     Default is None in which case None is returned

     @return JSON string of the
    """
    from urllib.request import urlopen

    # Returns the URL or None if the url is None.
    if url is None:
        return None

    with urlopen(url) as response:
        body = response.read()
    return body


# Summary of Employee is done.
# This function is called from the main module.
if __name__ == '__main__':

    # API URLS
    UserUrl = UserUrl = "https://jsonplaceholder.typicode.com/users"
    ToDoUrl = "https://jsonplaceholder.typicode.com/todos?userId={}"

    # * UserData (LISTE USER DATA)
    # * ToDoData (LISTE TODO DATA DATA)
    # Gets data from user and ToDo data and writes it to todo_all_employees.
    UserData = json.loads(GetAPI(UserUrl))

    data_dict = {}

    # Gets data from GetAPI and stores it in data_dict [ userid ]
    for user in UserData:
        UserId = user.get("id", 0)
        Username = user.get("username", "Guest")

        ToDoData = json.loads(GetAPI(ToDoUrl.format(UserId)))
        data_dict[UserId] = []

        for value in ToDoData:
            Title = value.get("title", "no name")
            IsCompleted = value.get("completed", False)
            data = {"task": Title, "completed": IsCompleted, "username": Username}
            data_dict[UserId].append(data)

    with open("todo_all_employees.json", "w") as file:
        json.dump(data_dict, file)
