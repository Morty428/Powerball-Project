# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:02:00 2018

@author: socce
"""

import pandas as pd

#df = pd.read_excel('powerballhistory.xls', sheet_name='powerballhistory',
 #                  index_col='Draw Date', skiprows=1)
'''df = pd.read_excel('powerballhistory.xls', sheet_name='powerballhistory',
                   header=None, index_col=None, skiprows=1, names=
                   ['Draw Date', 'N1','N2','N3','N4','N5','PB',
                    'Power Play','Jackpot']) '''

xl = pd.ExcelFile('powerballhistory.xls', sheet_name='powerballhistory')
df = xl.parse(header=None, skiprows=2, names=['Draw Date', 'N1','N2','N3','N4','N5','PB',
                    'Power Play','Jackpot'])
df.set_index('Draw Date', inplace=True)
df.index = df.index.str.slice(5,20)
df.index = pd.to_datetime(df.index)

#df['test'] = df['Draw Date'].str.slice(5,20)
#df['test'] = pd.to_datetime(df['test'])
#df['test'] = df['test'].astype('datetime64')
                    


print(df.head(2))

df.to_excel('test.xls', sheet_name='test', )