# Popular category in New york Times

The project uses the New York Times' most popular endpoint API and prints mainly pie charts and CSV using Python's packages such as matplotlib and CSV packages. My project statistically examines what kind of news categories were shared through Facebook by viewers. The project will have pie charts of shared news categories' frequency based on a day, a week, and a month, with CSV files showing all data collection. Therefore, the results show that the type of category New York Times viewers want to share and the importance.

<br>

# Code Walkthrough

- collection package <br>
  The Counter class in Python's collections module was used to combine all data, including zero for each period.
- requests <br>
  The requests package imports JSON information from the New York Times page through HTTP request processing.
- matplotlib <br>
  The Matplotlib package visualizes data in pie charts in this project.
- csv <br>
  The csv package lists all collections of categories' values as a CSV file.

<br>

## extract_nyt function

![](https://i.ibb.co/HCh6Jh9/01first-extraction-function.png)

The extract_nyt function hides Json data shared on Facebook through the New York Times' most popular endpoint. The date factor takes 1 day, seven days, and 30 days as integers from the user so that the user who uses the code can set the date of Url. As a result, the API that the data imports depends on the period user wants to see—finally, the function extracts raw data and returns essential results items.

<br>

## refine_nyt function

![](https://i.ibb.co/dcX1XGf/02refine-nyt.png)

The refine_nyt function imports each segment in rawdata[results] to create a section list. Category clears duplicate sections by assign a section value as a set. The category contains keywords of sections that are shared at least once. For loop counts all values in the section with the category data as the keyword. Finally, it returns a dictionary called frequency that contains section keys and frequency values.

<br>

## totalize_csv function

![](https://i.ibb.co/xLkFn1B/03csv.png)

Totalize_csv is a function that cleans up the number of category shares for all periods, including 1, 7, and 30 days, and outputs them to CSV. For your information, the category appointed here is different from the category in the previous function. The refine and extract functions assign data for all periods as raw_day,raw_week,raw_month, respectively. Categories combine all days, weeks, and months through **, creating criteria for pure categories by making all values zero integers. 

>for example, {'health': 2, 'style': 2, 'business': 2, } -> {'health': 0, 'style': 0, 'business': 0}.

Combine each day, week, and month with the raw attached with the category to create a dictionary containing values of zero. 

>for example, {'new york': 1, 'health': 3, 'u.s.': 5} ->
{'new york': 1, 'health': 3, 'u.s.': 5,'magazine': 0, 'opinion': 0,  'arts': 0}

Each for loop extracts values for all periods and writes the last CSV code as a CSV file

<br>

## draw_pie function

![](https://i.ibb.co/TMzwFr9/04-pie.png)

The draw pie function visualizes the data according to the user's argument input as a pie chart. The label contains the keys from frequency. Each for loop assigns the frequency dictionary's keys and values to the pie chart as ratio and label. The color subsequently is assigned the color from the colorlist according to the number of labels. The last Ratio loop calculates the value of the data as a percentage and represents it in the ratio. Finally, it stylizes the pie chart and executes a function that shows the image.

<br>

# Summary of Results

The project's goal is to check what categories are shared mainly by New York Times Viewers. The CSV file lists the shared categories at the top and writes the number of category shares for each period accordingly. The pie chart shows the percentage of each section visually. According to these results, the U.S. category was the most shared across all numbers. The Health and Business categories are the second rank.  I can see that most people's interests focus on news related to especially u.s, health, and business.

<br>

![](https://i.ibb.co/3C1LDDC/excel-result.png)
excel
![](https://i.ibb.co/KrMJGG2/01.png)
one
![](https://i.ibb.co/jwD6htS/07.png)
week
![](https://i.ibb.co/9nmN265/30.png)
month

# What I Would do Next

To develop this code further, I want to create a code that makes a more organized CSV file and makes it a pie chart from that data directly. Also, if I adjust the pie chart style to make it easier to see, it will be a better data source. Later, the new step is to create a menu tab that allows users to set all periods through Gui and a new chart to enable users to view total data to create user-friendly features and designs.

# Your full python script

```python
from collections import Counter
import requests
import matplotlib.pyplot as plt
import csv


def extract_nyt(date):
    # get date from user's input and assign date into url which
    # will give you data depending on period.
    HEAD = "Your name APP.v.0.0.1"
    key = "Your key"
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

```