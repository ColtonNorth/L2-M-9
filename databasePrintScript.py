#!/usr/bin/env python3
import sqlite3

#import os
#connect to database file
dbconnect = sqlite3.connect("database.db");

#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

#temperature = 43
#humidity = 50
#pressure = 200
#carbonDioxideLevel = 36.32
#nitrogenDioxideLevel = 12.67
#VOCLevel = 2.6
#Creating a new table and inserting test values
#cursor.execute('''CREATE TABLE vals (temperature REAL, humidity REAL, pressure REAL, carbonDioxide REAL, nitrogenDioxide REAL, voc REAL);''');
#cursor.execute('''INSERT INTO vals VALUES('12', '45.65', '65.2', '54.65', '777', '2.2');''')
#cursor.execute('''INSERT INTO vals VALUES(?, ?, ?, ?, ?, ?);''', (temperature, humidity, pressure, carbonDioxideLevel, nitrogenDioxideLevel, VOCLevel))

dbconnect.commit();

#execute simple select statement
cursor.execute('SELECT * FROM vals');
#print data
print('temp humi press  CO2  NO2   VOC')
for row in cursor:
    print(row['temperature'],row['humidity'],row['pressure'], row['carbonDioxide'], row['nitrogenDioxide'], row['voc']);


#close the connection
dbconnect.close();
