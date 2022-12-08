from itertools import count


cityTemp = open("cityTemp.csv")

rec1 = cityTemp.readline()
city, temperature, unit = rec1.split(',')
prev_city = city


cityTemp.seek(0)

tempSum = 0.0
count = 0
avgTemp = 0.0

for records in cityTemp:
    records = records.rstrip('\n')
    city, temperature, unit = records.split(',')

    if unit == "C":
        temperature = (float(temperature) * 9/5) + 32
    
    if city != prev_city:
        avgTemp = tempSum/count
        print(prev_city + " " + str(round(avgTemp, 2)))
        prev_city = city
        tempSum = 0.0
        count = 0
        avgTemp = 0.0
    tempSum = tempSum + float(temperature)
    count = count + 1

else:
    avTemp = tempSum/count
    print(prev_city + " " + str(round(avgTemp, 2)))


