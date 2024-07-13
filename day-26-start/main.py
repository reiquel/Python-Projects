# This is a sample Python script.

# numbers = range(1,5)
#
# new_numbers = [n * 2 for n in numbers]
# print(new_numbers)
#
# name = "Reiquel"
#
# new_name = [letter for letter in name]
# print(name)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# upper_case_names = [nam.upper() for nam in names]
# print(upper_case_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)

# list_of_strings = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]
# new_list = [int(string) for string in list_of_strings]
# # print(new_list)
#
# result = [number for number in new_list if number % 2 == 0]
# print(result)

# with open("file1.txt") as data:
#     numbers_1 = data.readlines()
#     stripped_number = [line.strip() for line in numbers_1]
# print(stripped_number)
#
# with open("file2.txt") as data_1:
#     numbers_2 = data_1.readlines()
#     stripped_number_1 = [line.strip() for line in numbers_2]
# print(stripped_number_1)
#
# list_of_numbers = [int(num) for num in stripped_number if num in stripped_number_1]
# print(list_of_numbers)

# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 50,
#     "Diana": 70,
#     "Ethan": 88,
#     "Fiona": 69
# }
#
# passed_students = {key:value for (key, value) in students_scores.items() if value >= 70}
# print(passed_students)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items() if temp == int(temp)}

# Write your code 👇 below:



print(weather_f)