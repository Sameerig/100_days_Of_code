import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squrills_count =len(data[data["Primary Fur Color"] =="Gray"])
red_squrills_count =len(data[data["Primary Fur Color"] =="Cinnamon"])
black_squrills_count =len(data[data["Primary Fur Color"] =="Black"])
print(grey_squrills_count)
print(red_squrills_count)
print(black_squrills_count)


data_dict ={
    "Fur color": ["Gray","Cinnamon","Black"],
    "Count": [grey_squrills_count,red_squrills_count,black_squrills_count]
}

print(data_dict)

df =pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")