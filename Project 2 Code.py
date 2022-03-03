from collections import Counter
import requests
import matplotlib.pyplot as plt
import csv


def extract_nyt(date):
    # get date from user's input and assign date into url which
    # will give you data depending on period.
    HEAD = "Hee Hwang APP.v.0.0.1"
    key = "AzUGePhSRqxf7SvGNsfcj2cM2bnYwgTc"
    url = f"https://api.nytimes.com/svc/mostpopular/v2/shared/{date}/facebook.json?api-key={key}"
    head = {'user-agent': HEAD}
    rawdata = requests.get(url, headers=head).json()

    return rawdata['results']


def refine_nyt(rawdata):
    # Get all sections from rawdata['results'].
    section = []
    frequency = {}
    for i in range(0, len(rawdata)):
        section.append(rawdata[i]['section'].lower())
    # 'set' section will erase repeated data, so will get
    # category data which will use as keywords to count frequency.
    category = set(section)
    category = list(category)

    # count each category's frequency from raw section data
    # by checking category data as keywords
    for category in section:
        frequency[category] = frequency.get(category, 0) + 1

    return frequency


def totalize_csv():

    # collect all collection of categories.
    section = ['Category :']
    raw_day = refine_nyt(extract_nyt(1))
    raw_week = refine_nyt(extract_nyt(7))
    raw_month = refine_nyt(extract_nyt(30))
    category = {**raw_day, **raw_week, **raw_month}

    # make all 0 values each category.
    category = dict.fromkeys(category, 0)
    week = {**category, **Counter(raw_week)}
    day = {**category, **Counter(raw_day)}
    month = {**category, **Counter(raw_month)}

    # add up category list and raw week's raw data
    # to make a whole list of week.
    day_values = ['Day :']
    week_values = ['Week :']
    month_values = ['Month :']

    # make value lists depending on the period.
    for key in category.keys():
        section.append(key)
    for value in day.values():
        day_values.append(value)
    for value in week.values():
        week_values.append(value)
    for value in month.values():
        month_values.append(value)

    # write data as a csv sequentially in a row.
    with open("mostpopular.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(section)
        writer.writerow(day_values)
        writer.writerow(week_values)
        writer.writerow(month_values)

totalize_csv()


def draw_pie(frequency):
    #  The label contains the keys from frequency.
    # Each for loop assigns the frequency dictionary's keys
    # and values to the pie chart as ratio and label.

    colorlist = ['azure', 'gold', 'yellowgreen', 'pink',
    'lightcoral', 'lightskyblue', 'greenyellow', 'yellow',
    'lightsalmon', 'linen', 'orange', 'green', 'violet',
    'gold', 'yellowgreen', 'pink', 'lightcoral', 'lightskyblue', 'blue']
    labels = []
    original_ratio = []
    colors = []
    ratio = []

    for key in frequency.keys():
        labels.append(key)

    for value in frequency.values():
        original_ratio.append(value)

    # assign colors depending on the number of labels.
    # make a ratio as a percentage.
    for i in range(0, len(labels)):
        colors.append(colorlist[i])
    for i in range(0, len(original_ratio)):
        ratio.append(int(original_ratio[i]*100/sum(original_ratio)))

    # style pie chart and show the result.
    plt.pie(ratio, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=10)
    plt.show()

# ask user input to get date argument.
draw_pie(refine_nyt(extract_nyt(date=input("Choose period from example \n ex)1,7,30 \n : "))))
