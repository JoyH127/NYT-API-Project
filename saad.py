'''
This script returns the stories from the Today I Learned Reddit Feed along
with their URLs
'''

import requests
from unidecode import unidecode
HEAD = {'user-agent': "Taylor Dupree"}


def reddit_extract(url="https://www.reddit.com/r/worldnews.json"):
    '''Returns useful data about Reddit posts from a given subreddit'''

    # Checks to see if a url was passed in as a parameter and Sets the
    # necessary header information
    rawdata = requests.get(url, headers=HEAD).json()

    # Return just the data of interest.
    return rawdata['data']


def reddit_transform(dataobj):
    '''Takes raw data from reddit extraction and returns a curated string
    object of the title and url.'''
    num = 0
    titleurl = []
    # indentifies and cleans the title and url
    for i in dataobj['children']:
        rawtitle = dataobj['children'][num]['data']['title']
        cleantitle = unidecode(
            rawtitle.lower().replace(' ', ' ').replace(',', ''))

        rawurl = dataobj['children'][num]['data']['url_overridden_by_dest']
        cleanurl = unidecode(
            rawurl.lower().replace(' ', ' ').replace(',', ''))

        titleurl.append(f"{cleantitle},{cleanurl}")
        num += 1
    return(titleurl)


def reddit_load_to_csv(title):
    '''Writes spreadsheet-style data to a CSV, title and associated URL.'''
    with open("newdatasource.csv", "w") as outputfile:
        # Write all the rows to file
        nl = "\n"
        num = 0
        for i in title:
            outputfile.write(f"{title[num]}{nl}")
            num = num + 1

reddit_load_to_csv(reddit_transform(reddit_extract(
    "https://www.reddit.com/r/todayilearned/.json")))