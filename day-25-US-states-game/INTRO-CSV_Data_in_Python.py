import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    print(data) # returns an object <_csv.reader object at 0x000002044D965420>

    # Get all temperatures
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures) # [12, 14, 15, 14, 21, 22, 24]
    # Too convoluted. The process is easier with pandas


#------------------------------PANDAS------------------------------#

import pandas

data = pandas.read_csv("weather_data.csv") # one step, no need for 'with open()' statement

print(data) # returns a Data Frame (table):
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

print(data["temp"]) # returns a Series with temperature values (single column):
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64

# Check the documentation here: https://pandas.pydata.org/docs/reference/index.html

# Transform the Data Frame to a dictionary with .to_dict()
data_dict = data.to_dict()
print(data_dict) # {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}


#------------------------------COLUMNS------------------------------#

# Get data in columns:
option_1 = data["temp"]
option_2 = data.temp

# Transform a Series to a list with .to_list()
temp_list = data["temp"].to_list()
print(temp_list) # [12, 14, 15, 14, 21, 22, 24]

# Using methods to calculate or return certain values:
average = data["temp"].mean() # 17.428571428571427
max_value = data["temp"].max() # 24


#------------------------------ROWS------------------------------#

# Get data in a row:
row = data[data.day == "Monday"]    # Row data for Monday. What this does:
                                    # 1. Get hold of the entire data table: data[]
                                    # 2. Inside, get hold of the column to search through: data[data.day]
                                    # 3. Once in the column, filter per value: data[data.day == "Monday"]
                                    # What this returns:
                                    #       day  temp condition
                                    # 0  Monday    12     Sunny

row2 = data[data.temp == data.temp.max()]
    # Row data for the day with the highest temperature:
    #       day  temp condition
    # 6  Sunday    24     Sunny


#------------------------------SINGLE VALUES------------------------------#

monday = data[data.day == "Monday"]
print(monday.temp)  # 0    12
                    # Name: temp, dtype: int64

# Transform temperature to Fahrenheit
monday_temp_C = monday.temp[0] # To get the first value in the series, use index 0 [0]: 12
monday_temp_F = monday_temp_C * 9/5 + 32 # 53.6


#------------------------------CREATE DATAFRAME AND SAVE AS CSV------------------------------#

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)  # Creates a DataFrame:
                                    #   students  scores
                                    # 0      Amy      76
                                    # 1    James      56
                                    # 2   Angela      65

data.to_csv("new_data.csv") # Saves the DataFrame as CSV in a new document