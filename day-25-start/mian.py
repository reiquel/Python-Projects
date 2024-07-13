# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
#
# temp_average = temp_sum / len(temp_list)
# print(round(temp_average))
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])

# monday_temp = data[data.day == "Monday"]
# temp_to_fahrenheit = (monday_temp.temp[0] * 9/5) + 32
# print(temp_to_fahrenheit)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
#
# data = pandas.DataFrame(data_dict)
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240515.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_1 = pandas.DataFrame(data_dict)
data_1.to_csv("squirrel_count.csv")