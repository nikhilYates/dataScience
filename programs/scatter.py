import matplotlib.pyplot as plt
from collections import Counter

# create a scatterplot

f = open('salesdata2.csv', 'r')

salefile = f.readlines()

saleList = []

s_list = []
c_list = []

for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))


#scatter plotting
plt.subplot(2, 2, 1)
plt.title('Scatterplot Sales Vs Cost')
plt.xlabel('Sale')
plt.ylabel('Cost')
plt.scatter(s_list, c_list)


#box plotting
plt.subplot(2, 2, 1)
plt.title('Box Plot')
plt.ylabel('Cost (USD)')
plt.boxplot(saleList)

#pie plot
plt.subplot(2, 2, 1)
city_count = Counter(saleList)
city_names = list(city_count.keys())
city_values= list(city_count.values())
plt.pie(city_values, labels=city_names, autopct='%.2f%%')

#bar chart
plt.xlabel('Sale')
plt.ylabel('Cost')
plt.bar(s_list, c_list)


# show plots
plt.show()


