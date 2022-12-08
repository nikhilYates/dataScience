# create histogram of ages

import matplotlib.pyplot as plt

f = open('agedata.csv', 'r')

agefile = f.readlines()

age_list = []

for records in agefile:
    age_list.append(int(records))
    

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


plt.title('Age Histogram')
plt.xlabel('Group')
plt.ylabel('Age')
           
plt.hist(age_list, histtype='bar', rwidth=0.9)

plt.show()