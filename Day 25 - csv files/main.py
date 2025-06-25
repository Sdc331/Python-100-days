import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250625.csv")
# temp = data["temp"].to_list()

# print(data["temp"].max())

# monday = data[data["day"] == "Monday"]

gray = data["Primary Fur Color"] == "Gray"
cinnamon = data["Primary Fur Color"] == "Cinnamon"
black = data["Primary Fur Color"] == "Black" 

print(f"Gray: {gray.sum()}, Cinnamon: {cinnamon.sum()}, Black: {black.sum()}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Amount": [gray.sum(), cinnamon.sum(), black.sum()]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")
