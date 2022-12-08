import matplotlib.pyplot as plt


x_days = [1, 2, 3, 4, 5]
y_price1 = [9, 9.5, 10.1, 10, 12]
y_price2 = [11, 12, 10.5, 13, 30]

# defining chart elements

plt.title('Stock Movement')
plt.xlabel('Date')
plt.ylabel('Price (CAD)')

plt.plot(x_days, y_price1, label ='Stock 1')
plt.plot(x_days, y_price2, label='Stock 2')

plt.legend(loc=2, fontsize=12)

plt.show()



