# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:02:00 2018

@author: Matthew Mortensen
"""

import pandas as pd

# Open the speadsheet in pandas
xl = pd.ExcelFile('powerballhistory.xls', sheet_name='powerballhistory')

# Create a dataframe from the spreadsheet
df = xl.parse(header=None, skiprows=2, names=
              ['Draw Date', 'N1','N2','N3','N4','N5','PB',
                    'Power Play','Jackpot'])
# Slice the Sat, and Wed, from the beginning of the draw date
df['Draw Date'] = df['Draw Date'].str.slice(5,20)

# Set the dataframe index to the Draw Date column
df.set_index('Draw Date', inplace=True)

# Print the first couple of lines from the data frame to verify the format
print(df.head(2))

# Save the dataframe to a new excel file
df.to_excel('powerballhistoryformatted.xls', sheet_name='powerballhistory', )