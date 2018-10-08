# Powerball-Project
A way to practice Python coding and using SQL tables to store and analyze data

Powerball history is downloaded from the Wisconsin Lottery website at:
https://wilottery.com/lottogames/powerballAllhistory.aspx
An option for Excel or text format can be downloaded. This program uses the Excel spreadsheet

Once the program is launched it will show an option menu and to select a menu choice type in the selection with the keyboard. Options are case sensitive. The menu is below.
```
Powerball_Numbers.db file exits
Database connection successfull

Menu Commands
create - Create the Table.
add - Add data from Excel Spreadsheat.
select - select a date range to show numbers.
update - Add a single draw date to the table.
delete - Delete a draw date from the table.
PB - number of times powerball picked
Plot - Plot the data
quit - Quit Program.

Command: 
```

The first thing that is checked is if there is a database file already created. If not you will have to select the create command to create the Powerball_Numbers.db file.

Now we must add the data to the database to do this we choose the add option from the menu.

With the data populated within the database we can start analyzing the data.

For now ploting the data is a simple bar chart. In further updates we can manipulate the data in different ways.

## Planned Updates

For the time being the data plotted is a total from the most recent Powerball drawing to 1992. Future updates will allow a date range selection to have more accurate data selection.

Another planned update is automatically scaping the drawing data to update the database.

## Known Issues

The SQL queries are in a refinement stage.  Trying to get variable assignment in the SQL queries is taking some time and research.
