# REEU simulation project
# Katie Krick
# Morgan Abraham
# Dr. Dennis Buckmaster

import pandas as pd
import math 
from datetime import timedelta
from datetime import datetime

# FIELD CHARACTERIZATION
# This is where the farmer will import a data file with field characteristics
# Our file includes field number, soil type, water capacity, slope percentage, 
# percentage of field, and acreage.

fields = pd.read_csv("allfieldsdata.csv")

# WEATHER DATA
# This is where we intend to pull in weather data about the area in which the
# fields are located. 
# The data currently being used is weather data reported from the Fort Wayne 
# International Airport provided to us through NOAA.The data needs to be daily
# data in order to produce accurate suggestions. 

weather = pd.read_csv("weather.csv", parse_dates = True)
weather["DATE"] = pd.to_datetime(weather["DATE"])

# INPUTS
# This is where we will ask the user to provide information about their fields

date = input("What is today's date?\nPlease enter as M/D/YYYY: ")
operations = input("What operation (plant, till, spray, or harvest) do you " 
                   "intend to do to your fields?: ")

# CALCULATIONS

# Determining whether it will rain that day
wdate = weather.loc[weather["DATE"] == date]
# pulls the row of data from weather that match the date input
prcp = float(wdate["PRCP"]) #defines the value for precipitation
if prcp == 0:
    print("It will not rain today. You may ",operations," your fields.")
else:
    print("It is going to rain today. You may not ",operations," your fields.")
 
# Creating empty lists for drainage rates for each field
rate1 = []
rate2 = []
rate3 = []
rate4 = []
rate5 = []
rate6 = []

# Defining drainage rate for soils in field 1 
for index, row in fields.iterrows():
    if row.loc["FIELDNUMBER"]== 1:
        if row.loc["RATING"] <= 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 1
        elif row.loc["RATING"] > 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 4
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 3
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 2
        rate1.append(rate)
# Defining drainage rate for soils in field 2 
for index, row in fields.iterrows():
    if row.loc["FIELDNUMBER"]== 2:
        if row.loc["RATING"] <= 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 1
        elif row.loc["RATING"] > 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 4
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 3
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 2
        rate2.append(rate)
# Defining drainage rate for soils in field 3 
for index, row in fields.iterrows():
    if row.loc["FIELDNUMBER"]== 3:
        if row.loc["RATING"] <= 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 1
        elif row.loc["RATING"] > 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 4
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 3
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 2
        rate3.append(rate)
# Defining drainage rate for soils in field 4 
for index, row in fields.iterrows():
    if row.loc["FIELDNUMBER"]== 4:
        if row.loc["RATING"] <= 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 1
        elif row.loc["RATING"] > 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 4
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 3
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 2
        rate4.append(rate)
# Defining drainage rate for soils in field 5 
for index, row in fields.iterrows():
    if row.loc["FIELDNUMBER"]== 5:
        if row.loc["RATING"] <= 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 1
        elif row.loc["RATING"] > 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 4
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 3
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 2
        rate5.append(rate)
# Defining drainage rate for soils in field 6 
for index, row in fields.iterrows():
    if row.loc["FIELDNUMBER"]== 6:
        if row.loc["RATING"] <= 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 2
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 1
        elif row.loc["RATING"] > 4:
            if row.loc["AVGPERCENTSLOPE"] < 3:
                rate = 4
            elif row.loc["AVGPERCENTSLOPE"]>3 and row.loc["AVGPERCENTSLOPE"]<6:
                rate = 3
            elif row.loc["AVGPERCENTSLOPE"] > 6:
                rate = 2
        rate6.append(rate)

# Selecting the largest rate(longest time to dry) for each field
rate1 = max(rate1)
rate2 = max(rate2)
rate3 = max(rate3)
rate4 = max(rate4)
rate5 = max(rate5)
rate6 = max(rate6)

# Determining whether or not the field has moist spots
NewWeather = weather.loc[weather["DATE"] <= date]
dates1 = []
dates2 = []
dates3 = []
dates4 = []
dates5 = []
dates6 = []

for index, row in NewWeather.iterrows():
    if row.loc["PRCP"] > 0:
        days2dry1 = math.ceil(rate1*row.loc["PRCP"])
        days2dry2 = math.ceil(rate2*row.loc["PRCP"])
        days2dry3 = math.ceil(rate3*row.loc["PRCP"])
        days2dry4 = math.ceil(rate4*row.loc["PRCP"])
        days2dry5 = math.ceil(rate5*row.loc["PRCP"])
        days2dry6 = math.ceil(rate6*row.loc["PRCP"])
        dried1 = row.loc["DATE"] + timedelta(days = days2dry1)
        dried2 = row.loc["DATE"] + timedelta(days = days2dry2)
        dried3 = row.loc["DATE"] + timedelta(days = days2dry3)
        dried4 = row.loc["DATE"] + timedelta(days = days2dry4)
        dried5 = row.loc["DATE"] + timedelta(days = days2dry5)
        dried6 = row.loc["DATE"] + timedelta(days = days2dry6)
        dates1.append(dried1)
        dates2.append(dried2)
        dates3.append(dried3)
        dates4.append(dried4)
        dates5.append(dried5)
        dates6.append(dried6)

drytime1 = max(dates1)
drytime2 = max(dates2)
drytime3 = max(dates3)
drytime4 = max(dates4)
drytime5 = max(dates5)
drytime6 = max(dates6)
    
# OUTPUTS
#This is where we will provide the user with suggestions for what they should
# do to their fields
date = datetime.strptime(date, "%m/%d/%Y")

if drytime1 > date:
    print("Field 1 is too wet to ",operations,". It should be dry on ", drytime1,".")
else:
    print("Field 1 is dry. You may ",operations," your field.")
    
if drytime2 > date:
    print("Field 2 is too wet to ",operations,". It should be dry on ", drytime2,".")
else:
    print("Field 2 is dry. You may ",operations," your field.")
    
if drytime3 > date:
    print("Field 3 is too wet to ",operations,". It should be dry on ", drytime3,".")
else:
    print("Field 3 is dry. You may ",operations," your field.")

if drytime4 > date:
    print("Field 4 is too wet to ",operations,". It should be dry on ", drytime4,".")
else:
    print("Field 4 is dry. You may ",operations," your field.")
    
if drytime5 > date:
    print("Field 5 is too wet to ",operations,". It should be dry on ", drytime5,".")
else:
    print("Field 5 is dry. You may ",operations," your field.")

if drytime6 > date:
    print("Field 6 is too wet to ",operations,". It should be dry on ", drytime6,".")
else:
    print("Field 6 is dry. You may ",operations," your field.")    
