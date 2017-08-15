# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:45:47 2017

@author: Wosco Labs
"""

# Add to pickle
import pandas as pd
import time

mainData=pd.read_pickle("mainPickle.pkl")

url = "https://coinmarketcap.com/all/views/all/"


# This is just my normal dataframe prep from the big history read code
dfs = pd.read_html(url)
    
df=dfs[0]

# Today's date
df=df.assign(Date=pd.to_datetime('today'))

# Rename some headers
df.rename(columns={df.columns[3]:'Cap',df.columns[5]:'Supply',df.columns[6]:'Vol'},inplace=True)

# Convert market cap to float
df['Cap']=df['Cap'].replace('[\$,]', '', regex=True).replace('?','0').astype(float)

# Convert price to float
df['Price']=df['Price'].replace('[\$,]', '', regex=True).replace('?','0').astype(float)

# Convert supply to float
df['Supply']=df['Supply'].replace('[\$, *]', '', regex=True).replace('?','0').astype(float)

# Convert volume to float
df['Vol']=df['Vol'].replace('[\$, *]', '', regex=True).replace('LowVol','0').replace('?','0').astype(float)

# Add it on top of the big data read in
comboDF=mainData.append(df, ignore_index=True)

print(comboDF)

comboDF.to_pickle(time.strftime('%Y%m%d',time.localtime()) + "pickle.pkl")
comboDF.to_pickle("mainPickle.pkl")