'''
My project reads updated 24 articles related to the keyword "gun"
from news Reddit sites and reports the amount these gun news
to see how gun plays a role in the United States.
'''

import requests
from unidecode import unidecode
import csv
global HEAD
HEAD = "Hee Hwang App.v.0.0.1"


def news_extraction(reddit="news"):
    '''Returns specific part of rawdata from a given reddit news site.'''
    
    # global variable is assigned to use as string literals can not change.
    # Set the necessary header information to extract successfully.

    if reddit is "news":
        reddit = "https://www.reddit.com/r/news/.json"
        head = {"user-agent": HEAD}
        rawdata = requests.get(reddit, headers=head).json()

    else if reddit is None:
        reddit = "https://www.reddit.com/r/worldnews.json"
        head = {"user-agent": HEAD}
        rawdata = requests.get(reddit, headers=head).json()

    

    # Returns raw news data

    return rawdata['data']


def get_lowercase_titles(dataset):
    ''' Based on extract news data, narrow down every news
    title data and refined the data.'''

    # While loop is going to get every article titles and
    # append function will add only titles in the list and
    # refine contents of titles.
    i = 0
    title = []
    lowtitle = []
    while i < 25:
        title.append(dataset['children'][i]['data']['title'])
        lowtitle.append(unidecode(title[i].lower().
            replace('  ', ' ').replace(',', ' ')))
        i += 1
    # The for loop traverse lowtitle list to check whether
    # the list has the keyword "gun" or not. If a list has the term,
    # it will increase the count.
    # and count will be appended at the end of the list

    return lowtitle


def gun_in_articles_cvs(title):
    ''' Write whole news titles given by daily news reddit and
        the number of 'gun' mentioned and make a cvs file,containg
        title, word count for each titles, and Gun count.
    '''
    # gunresult.csv file will be written.
    # it shows the about 25 article titles and
    # the number of mentions about 'gun' in the titles.
    # the chart will be listed in a row.
    # "import cvs" makes possible to list a cvs, using writerow
    # which can handle the list in a row and column.
    # writerow will set up the main contents named Title, Word count,
    # and 'Gun Count'.
    count = 0
    with open("gunresult.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Title', 'Word count', 'Gun Count'])
        for i in range(0, len(title)):
            if 'gun' in title[i]:
                count += 1
                writer.writerow([title[i], len(title[i]), count])
            else:
                writer.writerow([title[i], len(title[i]), 0])

gun_in_articles_cvs(get_lowercase_titles(news_extraction()))
