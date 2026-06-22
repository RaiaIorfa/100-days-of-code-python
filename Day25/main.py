# with open("./weather_data.csv") as data:
#     weather_data = data.readlines()

# print(weather_data)

# import csv

# with open("./weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

import pandas
import os

script_dir = os.path.dirname(__file__)  # folder where main.py is located
file_path = os.path.join(script_dir, "./weather_data.csv")

data = pandas.read_csv(file_path)
temperature = data["temp"]
print(data)
print(temperature)


print(temperature.mean())
print(temperature.max())
