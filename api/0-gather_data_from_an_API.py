#!/usr/bin/python3
"""
    Python script that, using this REST API, 
    for a given employee ID, 
    returns information about his/her TODO list progress.
"""
import json
import sys

args = sys.argv


def GetAPI(url=None):
    """
     Get data from API URL. This function is used to get data from the API URL. If you want to get data from a different URL you can use this function.
     
     @param url - URL of the API. Default is None in which case None is returned
     
     @return JSON string of the
    """
    """
        Function for get data of API URL 
    """
    from urllib.request import urlopen

    # Returns the URL or None if the url is None.
    if url is None:
        return None

    with urlopen(url) as response:
        body = response.read()
    return body


# Summary of Employee is done.
if __name__ == '__main__':
    """_summary_
    """
    # ARGV (For UserID)
    UserId = sys.argv[1]

    # API URLS
    UserUrl = UserUrl = "https://jsonplaceholder.typicode.com/users/{}"
    ToDoUrl = "https://jsonplaceholder.typicode.com/todos?userId={}"

    # * UserData (LISTE USER DATA MATCH WITH USERID)
    # * ToDoData (LISTE TODATA DATA MATCH WITH USERID)
    # * ToDoDoneData (LISTE DATA MATCH WITH USERID AND IF COMPLETED)
    UserData = json.loads(GetAPI(UserUrl.format(UserId)))
    ToDoData = json.loads(GetAPI(ToDoUrl.format(UserId)))
    ToDoDoneData = json.loads(
        GetAPI(ToDoUrl.format(f"{UserId}&completed=true")))

    # GET VALUES
    Username = UserData.get("name", "Guest")
    TaskDone = len(ToDoDoneData)
    TaskMax = len(ToDoData)

    # PRINT VALUES
    print("Employee {} is done with tasks({}/{}):"
          .format(Username, TaskDone, TaskMax))
    # Print out the ToDoDoneData list of toDoDoneData
    for value in ToDoDoneData:
        print("\t{}".format(value.get("title", "no name")))
