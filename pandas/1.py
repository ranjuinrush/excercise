# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:58:48 2018

@author: user
"""

import pandas as pd
cereal_df = pd.read_csv(r"C:\Users\user\Desktop\Niranjana\pandas\train.csv")
cereal_df2 = pd.read_csv(r"C:\Users\user\Desktop\Niranjana\pandas\train.csv")

# Are they the same?
print(pd.DataFrame.equals(cereal_df, cereal_df2))
print(cereal_df)
a=cereal_df.columns[0:2]
print(a)
mini=cereal_df['ID'].max()
print(mini)