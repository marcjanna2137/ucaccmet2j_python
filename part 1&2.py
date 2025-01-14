# import json package
import json 

# import string 
import string 

# open the file with precipitation measurements
with open('precipitation.json') as file:
    precipitation = json.load(file)

# create an empty dictionary for measurements for Seattle
seattle_measurements =[]

#loop over all the measurements data and append the ones with a seattle station code to the seattle_measurement dictionary
for measurement in precipitation: 
    if measurement ['station'] == 'GHCND:US1WAKG0038': 
        seattle_measurements.append(measurement)

# create an empty list for each month 
january = []
february = []
march = []
april = []
may = []
june = []
july = []
august = []
september = []
october = []
november = []
december = []

# create dictionary with lists corresponding to each month created above with keys being the names of each month
seattle_monthly = {
    'January': january, 
    'February' : february, 
    'March' : march, 
    'April': april, 
    'May': may, 
    'June': june, 
    'July' : july, 
    'August': august, 
    'September' : september, 
    'October': october, 
    'November' : november, 
    'December': december
    }

# loop over the precipitation data filtered for settle measurements to assign the measurements to a list corresponding to a month in which these measurements were taken
for measurement in seattle_measurements: 
    if measurement ['date'].startswith ('2010-01'): 
        january.append (measurement ['value'])
    else: 
        if measurement ['date'].startswith ('2010-02'): 
            february.append (measurement ['value'])
        else: 
            if measurement ['date'].startswith ('2010-03'): 
                march.append (measurement ['value'])
            else: 
                if measurement ['date'].startswith ('2010-04'): 
                    april.append (measurement ['value'])
                else: 
                    if measurement ['date'].startswith ('2010-05'): 
                        may.append (measurement ['value'])
                    else: 
                        if measurement ['date'].startswith ('2010-06'): 
                            june.append (measurement ['value'])
                        else: 
                            if measurement ['date'].startswith ('2010-07'): 
                                july.append (measurement ['value'])
                            else: 
                                if measurement ['date'].startswith ('2010-08'): 
                                    august.append (measurement ['value'])
                                else: 
                                    if measurement ['date'].startswith ('2010-09'): 
                                        september.append (measurement ['value'])
                                    else: 
                                        if measurement ['date'].startswith ('2010-10'): 
                                            october.append (measurement ['value'])
                                        else: 
                                            if measurement ['date'].startswith ('2010-11'): 
                                                november.append (measurement ['value'])
                                            else: 
                                                december.append (measurement ['value'])


# create an empty list for total monthly precipitation
total_monthly_precipitation = []

# calculate the total precipitation for each month
for month in seattle_monthly: 
    total_monthly_precipitation.append (sum (seattle_monthly[month]))

# calculate the total yearly precipitation for Seattle by adding up total monthly values 
total_yearly_precipitation = sum (total_monthly_precipitation)

# create an empty list for relative monthly precipitation
relative_monthly_precipitation = []

# loop over the total values for each month and divide it by total yearly precipitation and append it to the relative precipitation list
for monthly_value in total_monthly_precipitation: 
    relative_monthly_precipitation.append (monthly_value/total_yearly_precipitation)

# create a dictonary that summarizes the results 
results = {'Total Monthly': total_monthly_precipitation, 'Relative Monthly': relative_monthly_precipitation}

# write the results in a json file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file)
