#!/usr/bin/python3
"""  """
import requests


if __name__ == '__main__':
    html = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(html.content.decode("utf-8"))))
    print("\t- content: {}".format(html.content.decode("utf-8")))
