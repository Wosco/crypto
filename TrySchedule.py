import schedule
import time

def job():
	print("It's working?")

schedule.every().day.at("15:00").do(job)

while True:
	schedule.run_pending()
	time.sleep(60)