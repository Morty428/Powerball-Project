# Powerball-Project Development With Oracle DBMS

This will be the branch where we will develop different portions of the project.
Right now the project uses SQLite3 that is built into Python. Here we will develop a way for the project to use Oracle's DBMS.

This is also where we will have different Excel converstion files. If we find a better way to convert the speadsheet we will update it to the master branch
The Oracle DBMS used is the Express version 11g and can be downloaded from the Oracle website at:
https://www.oracle.com/technetwork/database/database-technologies/express-edition/downloads/xe-prior-releases-5172097.html

Powerball history is downloaded from the Wisconsin Lottery website at:
https://wilottery.com/lottogames/powerballAllhistory.aspx
An option for Excel or text format can be downloaded. This program uses the Excel spreadsheet

## Planned Updates

For the time being the data plotted is a total from the most recent Powerball drawing to 1992. Future updates will allow a date range selection to have more accurate data selection.

Another planned update is automatically scaping the drawing data to update the database.

## Known Issues

The xls spreadsheet from Wisconsin Lottery will have to be opened and saved as an xls file. When it is exported from the website it is opened as an html format.

The SQL queries are in a refinement stage.  Trying to get variable assignment in the SQL queries is taking some time and research.
