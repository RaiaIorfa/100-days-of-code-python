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

import pandas as pd
import os

# script_dir = os.path.dirname(__file__)  # folder where main.py is located
# file_path = os.path.join(script_dir, "./weather_data.csv")

# data = pandas.read_csv(file_path)
# # temperature = data["temp"]
# # print(data)
# # print(temperature)


# # print(temperature.mean())
# # print(temperature.max())
# # print(data[temperature == temperature.max()])
# monday = data[data.day == "Monday"]
# # print(monday)
# monday_temp = (monday.temp * 1.8) + 32
# print(f"{monday_temp} F")

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data = df["Primary Fur Color"].value_counts()

fur_color = pd.DataFrame(data)
print(fur_color)
fur_color.rename(columns={'Primary Fur Color': 'Fur Color', 'count': 'Count'})
print(fur_color)
fur_color.to_csv("squirrel_count.csv")

adult_squirrels = df[df["Age"] == "Adult"]
print(adult_squirrels.value_counts())

# Fur Color, Count
# grey, 2473
# red, 392
# black, 103