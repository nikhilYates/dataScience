import matplotlib.pyplot as plt


# plotting a boxplot

f=open('agedata.csv', 'r')

ageFile = f.readlines()

ageList1 = []

for records in ageFile:
    ageList1.append(int(records))

plt.title('Age Boxplot')
plt.boxplot(ageList1)

plt.show()