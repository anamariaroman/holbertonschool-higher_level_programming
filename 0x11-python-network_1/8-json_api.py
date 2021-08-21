#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        query = argv[1]
    else:
        query = ""

    url = "http://0.0.0.0:5000/search_user"
    request = requests.post(url, data={"q": query})
    try:
        resp = request.json()
        if len(resp) == 0:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except:
        print("Not a valid JSON")
