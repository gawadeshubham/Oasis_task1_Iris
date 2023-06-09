# -*- coding: utf-8 -*-
"""Copy of Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rk69TcagB0i9p1ZrFny9gdkpUJRqNyKy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pandas_profiling import ProfileReport

df = pd.read_csv('/content/sample_data/Advertising.csv')
df

pf = ProfileReport(df)

pf.to_widgets()

initialReport = pf.to_file('InitialReport.html')

from sklearn.linear_model import LinearRegression

x = df[['TV']]
y = df.Sales
Linear = LinearRegression()

Linear.fit(x,y)

Linear.intercept_

Linear.coef_

Linear.predict([[56]])

budget = [10,23,42,54,64,67,43,78,90,100]

for i in budget:
    print(Linear.predict([[i]]))

Linear.score(x,y)