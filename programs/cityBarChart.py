import matplotlib.pyplot as plt

#bar chart program

x_cities = ['Toronto', 'Vancouver', 'London', 'Tokyo', 'Chicago']
y_temps = [-12, 0, 5, 14, 7]

plt.title('City Temp Bar Chart')

plt.xlabel('Cities')
plt.ylabel('Temperature')

plt.bar(x_cities, y_temps)
plt.show()