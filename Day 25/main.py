# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)    

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
            
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census.csv')
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color ":["Gray", "Cinnamon", "Black"],
    "Count ": [grey_squirrels_count, cinnamon_squirrels_count,black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squrrel_count.csv")