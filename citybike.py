
# coding: utf-8

# In[2]:

import requests
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import collections


# In[4]:

r = requests.get('http://www.citibikenyc.com/stations/json')


# In[5]:

#Test that you have all the fields (important for setting up a database) by 
#running the data through a loop and gathering all the fields together:
key_list = [] #unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)


# In[6]:

#Convert data into pandas dataframe
from pandas.io.json import json_normalize
df = json_normalize(r.json()['stationBeanList'])


# In[15]:

#Create static reference table
#Our first step is to create a reference table that stores the information that remains 
#static with the station ID (id) number as the key value. Here we connect to the database.
#The `connect()` method returns a connection object.
con = lite.connect('citi_bike.db')
 
#From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
cur = con.cursor()    

with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')


# In[16]:

#Populate the tables with values
#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"


# In[17]:

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, 
        #stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'], station['totalDocks'], station['city'],
                    station['altitude'], station['stAddress2'], station['longitude'],
                    station['postalCode'], station['testStation'], station['stAddress1'],
                    station['stationName'], station['landMark'], station['latitude'],
                    station['location']))


# In[18]:

#Create changing table
#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

#create the table
#in this case, we're concatentating the string and joining all the station ids 
#(now with '_' and 'INT' added)
with con:
	cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", 
	            ".join(station_ids) + ");")


# In[19]:

#Populate it with our values for available bikes
# a package with datetime objects
import time

# a package for parsing a string into a Python datetime object
from dateutil.parser import parse 

import collections

#take the string and parse it into a Python datetime object
exec_time = parse(r.json()['executionTime'])


# In[20]:

#We create an entry for the execution time by inserting it into the database:
with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', 
               (exec_time.strftime('%s'),))


# In[21]:

#iterate through the stations in the "stationBeanList"
id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

#loop through the stations in the station list
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

#iterate through the defaultdict to update the values in the database
with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + 
        " WHERE execution_time = " + exec_time.strftime('%s') + ";")
 
import time
from dateutil.parser import parse
import collections
import sqlite3 as lite
import requests

con = lite.connect('citi_bike.db')
cur = con.cursor()


for i in range(60):
    r = requests.get('http://www.citibikenyc.com/stations/json')
    exec_time = parse(r.json()['executionTime'])

    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', 
               (exec_time.strftime('%s'),))
    con.commit()

    id_bikes = collections.defaultdict(int)
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + 
                    " WHERE execution_time = " + exec_time.strftime('%s') + ";")
    con.commit()

    time.sleep(60)

con.close() #close the database connection when done


#Designing an Algorithm
hour_change = collections.defaultdict(int)
for col in df.columns:
	station_vals = df[col].tolist() #assigns the column name to station_vals
	station_id = col[1:] #trim the '_'
	station_change = 0
	for k, v in enumerate(station_vals):
		if k < len(station_vals) - 1:
			station_change += abs(station_vals[k] - station_vals[k+1])
	hour_change[int(station_id)] = station_change
	
def keywithmaxval(d):
    # create a list of the dict's keys and values; 
    v = list(d.values())
    k = list(d.keys())

    # return the key with the max value
    return k[v.index(max(v))]

# assign the max key to max_station
max_station = keywithmaxval(hour_change)

#query sqlite for reference information
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference 
            'WHERE id = ?", (max_station,))
data = cur.fetchone()
print "The most active station is station id %s at %s latitude: %s longitude: %s " % data
print "With " + str(hour_change[379]) + " bicycles coming and going in the hour between " 
      + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S') + 
      " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S')

import matplotlib.pyplot as plt

plt.bar(hour_change.keys(), hour_change.values())
plt.show()
