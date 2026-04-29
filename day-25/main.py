# with open("weather_data.csv") as weather_file:
#     weather = weather_file.readlines()
#     print(weather)

# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temprature = []
#     for row in data:
#         temprature.append(row[1])
#         print(row[1])

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# import pandas
# from pandas import DataFrame
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# # Get data in columns
# print(data.condition)
# print(data["condition"])
#
# # Get Data in Row
# print(data[data.day == "Monday"])


# high_temp = data["temp"].max()
# print(high_temp)

# high_temp = 0
# for temp in data["temp"]:
#     if temp > high_temp:
#         high_temp = temp
# print(high_temp)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = ( monday_temp * 9/5) + 32
# print(monday_temp_F)
#

# create a dataframe from scratch
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_dict = pandas.DataFrame(data_dict)
# data_dict.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color " : ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")