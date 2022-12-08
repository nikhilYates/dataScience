import matplotlib.pyplot as plt

# create a python pie graph

f = open('agedata2.csv', 'r')

ageFile = f.readlines()

ageList = []

for records in ageFile:
    age, city = records.split(sep = ',')
    ageList.append(city)

from collections import Counter
city_count = Counter(ageList)

city_names = list(city_count.keys())
city_values= list(city_count.values())


plt.pie(city_values, labels=city_names, autopct='%.2f%%')

plt.show()
