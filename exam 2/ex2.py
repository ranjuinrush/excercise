# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:34:53 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
path  = r"C:\Users\user\Desktop\Niranjana\exam 2\camera_1.csv"

file = pd.read_csv(path)
df = pd.DataFrame(file)

print(df.columns)

print(df.dtypes)