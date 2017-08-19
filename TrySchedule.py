import schedule
import time
import sys

def job():
	print("It's working?")
	sys.stdout.flush()

# schedule.every().day.at("15:00").do(job)

schedule.every(10).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
