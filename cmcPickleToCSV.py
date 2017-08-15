# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 00:40:02 2017

@author: Wosco Labs
"""
# Take a pickle and dump the 4 CSVs
import pandas as pd
import time

# Read pickle from today's date.  Assume this is run after cmcAddToday
comboDF=pd.read_pickle("mainPickle.pkl")

# Pivot the table for Date on x axis        
capDF=comboDF.pivot_table(index='Date',columns='Name',values='Cap')

# Fill in the gaps
capDF.fillna(0, inplace=True)

# Do same for Volume
volDF=comboDF.pivot_table(index='Date',columns='Name',values='Vol')
volDF.fillna(0,inplace=True)

# Rank cap and volume just because
capRank=capDF.rank(axis=1,method='min',ascending=False)
volRank=volDF.rank(axis=1,method='min',ascending=False)

# Dump to CSV using today's date
capDF.to_csv(time.strftime('%Y%m%d',time.localtime()) + "cap.csv")
volDF.to_csv(time.strftime('%Y%m%d',time.localtime()) + "vol.csv")
capRank.to_csv(time.strftime('%Y%m%d',time.localtime()) + "capRank.csv")
volRank.to_csv(time.strftime('%Y%m%d',time.localtime()) + "volRank.csv")

capDF.to_csv("cap.csv")
volDF.to_csv("vol.csv")
capRank.to_csv("capRank.csv")
volRank.to_csv("volRank.csv")