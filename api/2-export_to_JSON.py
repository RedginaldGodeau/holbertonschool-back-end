#!/usr/bin/python3
"""
    Python script to export data in the JSON format.
"""
import json
import sys

args = sys.argv


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
    # ARGV (For UserID)
    UserId = sys.argv[1]

    # API URLS
    UserUrl = UserUrl = "https://jsonplaceholder.typicode.com/users/{}"
    ToDoUrl = "https://jsonplaceholder.typicode.com/todos?userId={}"

    # * UserData (LISTE USER DATA MATCH WITH USERID)
    # * ToDoData (LISTE TODATA DATA MATCH WITH USERID)
    UserData = json.loads(GetAPI(UserUrl.format(UserId)))
    ToDoData = json.loads(GetAPI(ToDoUrl.format(UserId)))

    Username = UserData.get("username", "Guest")

    data_dict = {"{}".format(UserId): []}

    # Write data to json file for use in tests.
    # This is a list of dictionaries that are passed to data_
    for value in ToDoData:
        Title = value.get("title", "no name")
        IsCompleted = value.get("completed", False)
        data = {"task": Title, "completed": IsCompleted, "username": Username}
        data_dict[UserId].append(data)

    with open("{}.json".format(UserId), "w") as file:
        json.dump(data_dict, file)
