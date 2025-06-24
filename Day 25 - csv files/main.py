# with open("weather_data.csv", mode="r") as f:
#     data = f.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     next(data)
#     temperatures = []
#     for each in data:
#         temperatures.append(int(each[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(data)