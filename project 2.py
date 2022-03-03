import requests
import matplotlib.pyplot as plt
import numpy as np


def extraction(date):
    HEAD = "Hee Hwang APP.v.0.0.1"
    key ="AzUGePhSRqxf7SvGNsfcj2cM2bnYwgTc"
    url = f"https://api.nytimes.com/svc/mostpopular/v2/shared/{date}/facebook.json?api-key={key}"
    head = {'user-agent': HEAD}
    rawdata = requests.get(url, headers=head).json()

    return rawdata['results']

def refine(rawdata):
    i=0
    count = 0 
    j = 0
    subsection = []
    section = []
    frequency = {}
    while i < len(rawdata):
        section.append(rawdata[i]['section'].lower())
        i += 1
    
    section_set = set(section)
    section_set = list(section_set)
    
    for section_set in section:
        frequency[section_set] = frequency.get(section_set,0) + 1

    return frequency  



data = extraction(1)   
category = refine(data)

print(category)

i=0
j=0
colorlist = ['purple','gold', 'yellowgreen','pink', 'lightcoral', 'lightskyblue','red','yellow','grey']
labels = []
original_ratio = []
colors = []
ratio = []

for key in category.keys():
    labels.append(key)

for value in category.values():
    original_ratio.append(value)

for i in range(0,len(labels)):
    colors.append(colorlist[i])
for i in range(0,len(original_ratio)):
    ratio.append(int(original_ratio[i]*100/sum(original_ratio)))
print(ratio)
print(colors)

plt.pie(ratio,labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=10)
plt.show()
    

