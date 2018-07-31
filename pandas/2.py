# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:00:05 2018

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import table

raw_data={'Vehilcle':['cars','bikes','vans','buses'],'No of vehicles':[140,70,55,5]}
df = pd.DataFrame(raw_data)
#df['total_vehicles'] = df['cars'] + df['bikes'] + df['buses'] + df['vans']
plt.figure(figsize=(16,8))

ax1 = plt.subplot(121, aspect='equal')
df.plot(kind='pie', y = 'No of vehicles', ax=ax1, autopct='%1.1f%%', 
startangle=90, shadow=False, labels=df['Vehilcle'], legend = False, fontsize=14)


ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, df, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(14)
plt.show()