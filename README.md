# REEU in Digital Agriculture at Purdue - Applications of Digital Agriculture: Using Python to Predict Field Outcomes
Weather is unpredictable and the “volume” of tactical decisions so large that farmers often make decisions about their field operations only using  instinct as informed by short-term weather predictions. This project will create a simulation framework and environment that analyzes weather data (past and forecasts), field/soil characteristics, and intended farming operations to provide farmers with suggestions backed by data. Initial use of this program will require an input of field/soil characteristics and location from the farmer. From there the farmer can run the simulator to receive predicted outcomes. Using different field data as well as weather data, a Python script was developed in order to provide a simulation of field outcomes including the date and order in which certain field operations should be performed. This simulation was created with the intent of helping farmers have handy and rapid access data-based recommendations. This project will further advancements in precision farming in terms of time efficiency as the script will output the most effective sequence  according to the various inputs such as weather and desired application. 

The files that are imported into the script are .csv files that contain data about the fields that this code was tested on collected from the USDA Web Soil Survey as well as data about weather collected from the Fort Wayne international airport because this was the closest available location to collect past daily weather data from NOAA. The field data files contains the following rows: field number, soil type, drainage class rating, minimum percent slope, maximum percent slope, average percent slope, percent of field, and acres. The weather data file must include but is not limited to: date and precipitation.

Some assumptions/limitations that were made in developing this script:

1 - The fields are level (Elevation was not considered)

2 - Weather conditions are the same for all fields

3 - USDA Web Soil Survey is 100% accurate

4 - The farming equipment is all uniform (There is no change in how dry the soil must be in order to drive on it)

Going forward, we hope to eliminate some of these assumptions and implement them into the script.

Katie Krick and Morgan Abraham

Faculty Adviser: Dr. Dennis Buckmaster
