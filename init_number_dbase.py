#By Matthew Mortensen
#Code to initialize the SQL table and import data from a speadsheet
import sqlite3
import os
import xlrd
import pandas as pd
DB_File = "Powerball_Numbers.db"
    
def display_Menu():
    print("Menu Commands")
    print("create - Create the Table.")
    print("add - Add data from Excel Spreadsheat.")
    print("select - select a date range to show numbers.")
    print("update - Add a single draw date to the table.")
    print("delete - Delete a draw date from the table.")
    print("PB - number of times powerball picked")
    print("Plot - Plot the data")
    print("quit - Quit Program.")

def create_DB(): #To create a sql table
    conn = sqlite3.connect(DB_File)
    conn.execute('''
                 CREATE TABLE if not exists Powerball
                 (
                  DrawDate       DATETIME  NOT NULL PRIMARY KEY,
                  N1             INTEGER    NOT NULL,
                  N2             INTEGER    NOT NULL,
                  N3             INTEGER    NOT NULL,
                  N4             INTEGER    NOT NULL,
                  N5             INTEGER    NOT NULL,
                  PB             INTEGER    NOT NULL,
                  PowerPlay      TEXT       NOT NULL,
                  Jackpot        TEXT       NOT NULL
                 )
                 ''')
    print("Table was created successfully")
    conn.close()
    
#Use xlrd to convert spreadsheet to sql    
def add_Data():
    book = xlrd.open_workbook("test.xls")
    sheet = book.sheet_by_name("test")
    conn = sqlite3.connect(DB_File)
    c = conn.cursor()
    query = '''INSERT INTO Powerball 
    (DrawDate, N1, N2, N3, N4, N5, PB, PowerPlay, Jackpot)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    #Use a loop to run through the spreadsheet use the number 1 to skip to row 2 where the data starts   
    for r in range(1, sheet.nrows):
        DrawDate     = sheet.cell(r,0).value
        N1           = sheet.cell(r,1).value
        N2           = sheet.cell(r,2).value
        N3           = sheet.cell(r,3).value
        N4           = sheet.cell(r,4).value
        N5           = sheet.cell(r,5).value
        PB           = sheet.cell(r,6).value
        PowerPlay    = sheet.cell(r,7).value
        Jackpot      = sheet.cell(r,8).value
        values = (DrawDate, N1, N2, N3, N4, N5, PB, PowerPlay, Jackpot)
        #Add the data from the loop to the table
        c.execute(query, values)
    c.close()
    conn.commit()
    conn.close()
    print("Data import completed")
    print()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    print("Imported " + columns + " columns and " + rows + " rows to database")

#Can have a user selected date range to show draw numbers 
def select_Date():
    conn = sqlite3.connect(DB_File)
    date_1 = input("enter in the beginning draw date, yyyy/mm/dd ")
    date_2 = input("enter in the end draw date, yyyy/mm/dd ")
    #query = '''SELECT * FROM Powerball WHERE DrawDate >= ? 
               #AND DrawDate <= ? ORDER BY DrawDate'''
    #cursor = conn.execute(query, (date_1, date_2,))
    query = '''SELECT * FROM Powerball'''
    cursor = conn.execute(query)
    print("{:^15}{:^4}{:^3}{:^3}{:^3}{:^3}{:^3}{:^8}{:^20}".format(
            "DrawDate","N1","N2","N3","N4","N5","PB","PowerPlay","Jackpot"))
    for row in cursor:
       print("{:15}{:^4}{:^3}{:^3}{:^3}{:^3}{:^3}{:^8}{:>20}".format(
               row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    conn.close()
    
#To manually add draws to the table
def update_Data():
    conn = sqlite3.connect(DB_File)
    get_DrawDate = input("Enter in the Draw Date yyyy/mm/dd: ")
    get_N1 = int(input("Enter the 1st number: "))
    get_N2 = int(input("Enter the 2nd number: "))
    get_N3 = int(input("Enter the 3rd number: "))
    get_N4 = int(input("Enter the 4th number: "))
    get_N5 = int(input("Enter the 5th number: "))
    get_PB = int(input("Enter the Powerball number: "))
    get_multi = input("Enter the Power Play multiplier: ex 2x ")
    get_Jackpot = float(input("Enter the Jackpot amount, number only: "))
    #Formating for the last column
    get_Jackpot = "{:.2f}".format(get_Jackpot)
    Jackpot = "$"+ get_Jackpot + " Million"
    query = '''INSERT INTO Powerball 
    (DrawDate, N1, N2, N3, N4, N5, PB, PowerPlay, Jackpot)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    #Adding to the sql database
    conn.execute(query, (get_DrawDate, get_N1, get_N2, get_N3, get_N4, 
                         get_N5, get_PB, get_multi, Jackpot,))
    conn.commit()
    conn.close()
    print(get_DrawDate + " was added to the database successfully.")
    
#Delete a draw date if there was an input mistake
def delete_Data():
    conn = sqlite3.connect(DB_File)
    get_DrawDate = input("Enter the draw date to delete mm/dd/yyyy: ")
    query = '''DELETE FROM Powerball WHERE DrawDate = ?'''
    conn.execute(query, (get_DrawDate,))
    conn.commit()
    conn.close()
    print(get_DrawDate + " was deleted successfully")
    
#Will list the amount of times a powerball was picked
def PB_Picked():
    conn = sqlite3.connect(DB_File)
    query = '''SELECT PB, COUNT(PB)
               FROM Powerball 
               GROUP BY PB
               ORDER BY COUNT(PB) DESC'''
    cursor = conn.execute(query)
    print(list(cursor))
    conn.close()
    
#To plot the regular number selections    
def plot_Data():
    conn = sqlite3.connect(DB_File)
    #convert sql to pandas dataframe
    df_sql = pd.read_sql('''SELECT * FROM Powerball''', con=conn)
    #Create a subset of the dataframe
    numbers_df = df_sql [["N1","N2","N3","N4","N5"]]
    #Count up the number of times a number is picked
    count_df = numbers_df.apply(pd.Series.value_counts)
    #Getting rid of the NaN from the other columns and to get findal number
    total_picked = (count_df.fillna(0)["N1"] + count_df.fillna(0)["N2"] + 
                    count_df.fillna(0)["N3"] + count_df.fillna(0)["N4"] + 
                    count_df.fillna(0)["N5"])
    #using pandas plot to show the number breakdown
    df_plot = total_picked.plot(kind='bar', figsize=(18,10), grid=True,
                      title ="Number of Times a Powerball Number Selected",
                      yticks=(0,25,50,75,100,125,150,175,200,225,250,275,300)
                      )
    df_plot.set_xlabel("Numbers")
    df_plot.set_ylabel("Picked Amount")
    conn.close()

def main():
    try:
        #check to make sure file exists
        if not os.path.isfile("PowerBall_Numbers.db"):
            print()
            print("Error: " + DB_File +" not found")
            print()
            print("Select Create Table")
            print()
        else:
            #to create the file and name it
            print(DB_File +" file exits")
            conn = sqlite3.connect(DB_File)
            print("Database connection successfull")
            print()
        display_Menu()
        #conditions of the menu
        while True:
            command = input("Command: ")
            if command == "create":
                create_DB()
            elif command == "add":
                add_Data()
            elif command == "select":
                select_Date()
            elif command == "update":
                update_Data()
            elif command == "delete":
                delete_Data()
            elif command == "PB":
                PB_Picked()
            elif command == "Plot":
                plot_Data()
                continue
            elif command == "quit":
                break
            else:
                print("Not a valid command input. Please try again. \n")
            display_Menu()
        conn = sqlite3.connect(DB_File)
        conn.close()
        print("Database closed successfully")
    except Exception as e:
        print("Error,", e)
    print("Goodbye")
    
main()