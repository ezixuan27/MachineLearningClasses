#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


df=pd.read_csv("Tennis.csv")
print(df)
print(df['Outlook'])

enc = LabelEncoder()
#Make sure label start from 0
df['Outlook'] = enc.fit_transform(df['Outlook'])	
print(df)

