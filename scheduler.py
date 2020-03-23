from crontab import CronTab
from __init__ import *
import sys

# this uses the python-crontab package NOT crontab.
# https://pypi.org/project/python-crontab/

scrape_period = sys.argv[1] # In minutes (integer)
write = 1 
remove = 1

mycron  = CronTab(user=True)
#users_cron  = CronTab(user='josephbakarji')

if remove:
    mycron.remove_all()
    mycron.write()

if write:
    job = mycron.new(command='python '+ MAINDIR +'scraper.py')
    job.minute.every(scrape_period)
    mycron.write()

print("crontab file content:")
for job in mycron:
    print(job)

# verify job is saved by running: crontab -e

#print(job.is_enabled())
#job.hour.every(4)
#job.day.on(4, 5, 6)

#job.dow.on('SUN')
#job.dow.on('SUN', 'FRI')
#job.month.during('APR', 'NOV')
