# import json package
import json 

# open the file with precipitation measurements
with open('precipitation.json') as file:
    precipitation = json.load(file)

# create an empty dictionary for measurements for Seattle
seattle_measurements =[]


# loop over all the measurements data and append the ones with a seattle station code to the seattle_measurement dictionary
for measurement in precipitation: 
    if measurement ['station'] == 'GHCND:US1WAKG0038': 
        seattle_measurements.append(measurement)

# print seattle_measurments to check 
print (seattle_measurements)  
import string 
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

print (seattle_monthly)

total_monthly_precipitation = []
for month in seattle_monthly: 
    total_monthly_precipitation.append (sum (seattle_monthly[month]))

print (total_monthly_precipitation)

# This is where we actually open the file and write to it
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(total_monthly_precipitation, file)



