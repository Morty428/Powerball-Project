# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:23:52 2018

@author: Matthew Mortensen
"""

import cx_Oracle
import xlrd

# Connect to Oracle with username/password
conn = cx_Oracle.connect('python/test')

# Connection test
print(conn.version)

# Create a cursor element to execute SQL statements
cur = conn.cursor()

# DB Drop and Create to have an empty table for testing
cur.execute('''DROP TABLE Powerball''')
cur.execute ('''
                 CREATE TABLE Powerball
                 (
                  DrawDate       DATE  NOT NULL PRIMARY KEY,
                  N1             INTEGER    NOT NULL,
                  N2             INTEGER    NOT NULL,
                  N3             INTEGER    NOT NULL,
                  N4             INTEGER    NOT NULL,
                  N5             INTEGER    NOT NULL,
                  PB             INTEGER    NOT NULL,
                  PowerPlay      VARCHAR(5)       NOT NULL,
                  Jackpot        VARCHAR(25)       NOT NULL)
                 ''')
                 
# Open results spreadsheet to import into database
book = xlrd.open_workbook("powerballhistoryformatted.xls")
sheet = book.sheet_by_name("powerballhistory")

# Query to insert sheet data used a as variable
query = '''INSERT INTO Powerball 
    (DrawDate, N1, N2, N3, N4, N5, PB, PowerPlay, Jackpot)
    VALUES (to_date(:1,'MON DD, YYYY'), :2, :3, :4, :5, :6, :7, :8, :9)
    '''
    
# Use a loop to run through the spreadsheet use the number 1 to skip to row 2 where the data starts   
for row in range(1, sheet.nrows):
    DrawDate     = sheet.cell(row,0).value
    N1           = sheet.cell(row,1).value
    N2           = sheet.cell(row,2).value
    N3           = sheet.cell(row,3).value
    N4           = sheet.cell(row,4).value
    N5           = sheet.cell(row,5).value
    PB           = sheet.cell(row,6).value
    PowerPlay    = sheet.cell(row,7).value
    Jackpot      = sheet.cell(row,8).value
    values = (DrawDate, N1, N2, N3, N4, N5, PB, PowerPlay, Jackpot)
# Add the data from the loop to the table
    cur.execute(query, values)
    
# Close the cursor element
cur.close()

# Commit the added data to the DB
conn.commit()
print("Data import completed")
print()

# Used to show what columns and rows were added to the DB
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("Imported " + columns + " columns and " + rows + " rows to database")

# Close connection to the DBMS
conn.close()
print('Connection closed')