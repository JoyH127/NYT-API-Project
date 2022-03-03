"""
import requests

url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"
rawdata = requests.get(url).json()


def top_ten(new):
  
  for data in new ['rows'][:10]:
    print(new['rows'][data])

top_ten(rawdata)

"""

import requests

url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"

top_ten_lst = []

def top_ten(copy):
  rawdata = requests.get(url).json()
  for x in range(len(rawdata['rows'][:10])):
    templst = []
    for y in rawdata['rows'][:10]:
      newlst.append(y)

      top_ten_lst = [templst]

    top_ten_lst(copy)