#!/usr/bin/python3
import json
import sys

args = sys.argv


def GetAPI(url=None):
    from urllib.request import urlopen

    if url is None:
        return None

    with urlopen(url) as response:
        body = response.read()
    return body


if __name__ == '__main__':
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
    for value in ToDoDoneData:
        print("\t{}".format(value.get("title", "no name")))
