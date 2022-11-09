# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:19:27 2022

@author: cse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
age_list=[12,22,36,42,15,89,65,29,6,
         35,81,90,51,53,53,22,31,75,5]
sex_list=['male','female','female','other','male','other','other','male',                                  
'female','female','other','male','female','female','male','female','male','female',
'male']
df_age_sex=pd.DataFrame({'age':age_list,'gender':sex_list})
print(df_age_sex)