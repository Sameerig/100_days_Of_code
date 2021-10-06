#     data=data_file.readlines()
#     print(data)


# import csv
# with open("weather_data.csv.csv") as data_file:
#     data =csv.reader(data_file)
#     temprature =[]
#     for row in data:
#         if row[1]!="temp":
#             temprature.append(int(row[1]))
#     print(temprature)
import pandas
data = pandas.read_csv("weather_data.csv.csv")
# print(data["temp"])


# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data["temp"].tolist()
# sum =0
# for item in temp_list:
#     sum =item+sum
# percentage = round(sum / len(temp_list),2)

# print(f"The avg percentage is {percentage}%")



# '''or'''

# print (data["temp"].mean()) 

# # print(data["temp"].max())


# print(data[data["temp"]==data["temp"].max()])

print(data[data["temp"]==data["temp"].max()])

print("\n")
print("\n")
print("\n")
print("\n")

monday = data[data["day"]=="Monday"]

print(int(monday["temp"]))