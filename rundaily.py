
import schedule
import time

def readAndWrite():
	# Add to pickle
	import pandas as pd
	import time

	mainData=pd.read_pickle("data/mainPickle.pkl")

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

	# Dump to file
	comboDF.to_pickle("data/mainPickle.pkl")

	capDF.to_csv("data/cap.csv")
	volDF.to_csv("data/vol.csv")
	capRank.to_csv("data/capRank.csv")
	volRank.to_csv("data/volRank.csv")

if __name__ == "__main__":
	schedule.every().day.at("13:00").do(readAndWrite)

	while True:
		schedule.run_pending()
		time.sleep(60)
