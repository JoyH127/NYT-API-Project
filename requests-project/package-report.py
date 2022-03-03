"""
rawdata should be changed into data type
I can access it. json() makes this rawdata
the dictionary data type.

"""

import requests

url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"
rawdata = requests.get(url).json()

"""
The first for loop should check
the whole keys in a dictionary.
The if statement checks whether 'rows'
keyword exists in data.
The while loop extracts the first 10
dictionary data.

"""


def extract(raw):
    data = raw
    i = 0
    for key in data:
        if 'rows' in key:
            while i < 10:
                print(f"Rank {i+1} :{data['rows'][i]}")
                i = i+1

extract(rawdata)
