
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

#value = "DELETE FROM emails"
#Creating a new table and inserting test values
#cursor.execute('''CREATE TABLE emails (email TEXT);''');
#cursor.execute('''INSERT INTO emails VALUES('example@gmail.com');''')
#cursor.execute('''INSERT INTO emails VALUES('test@gmail.com');''')
#cursor.execute('''INSERT INTO emails VALUES('coltonsnowboards@gmail.com');''')
#cursor.execute(value)

dbconnect.commit();

#execute simple select statement
cursor.execute('SELECT * FROM vals');
#print data
print('temp humi press  CO2  NO2   VOC')
for row in cursor:
    print(row['temperature'],row['humidity'],row['pressure'], row['carbonDioxide'], row['nitrogenDioxide'], row['voc']);
print('\n')
cursor.execute('SELECT * FROM emails');
#print data
print('Customer emails')
for row in cursor:
    print(row['email']);

#close the connection
dbconnect.close();
