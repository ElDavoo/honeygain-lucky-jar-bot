import json
import requests
import datetime
from time import sleep
from random import randint


def getAuth():
    auth = open("auth.txt", "r").read()
    auth = auth.replace('\n', '')
    auth = auth.replace('\t', '')
    return auth


def getHeaders():
    return json.loads(open("./headers.json", 'r').read())


def main():
    api_url = "https://dashboard.honeygain.com/api/v1/contest_winnings"
    headers = getHeaders()

    headers["authorization"] = "Bearer " + getAuth()

    r = requests.post(url=api_url, headers=headers)
    print(f"{r.text}")


while True:
    try:
        main()
        sleep((60 * 60 * 23)+randint(1000,6000))  # Every 24 hours more or less
    except:
        print("Some sort of error occoured!")
        sleep(300)
