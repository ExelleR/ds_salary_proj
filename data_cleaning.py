# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:24:45 2020

@author: exeller
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")
df = df[df['Salary Estimate'] != '-1']