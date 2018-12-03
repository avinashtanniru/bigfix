#!/usr/bin/python
import os, sys, base64
import datetime
file_path = '.'
sys.path.append(os.path.dirname(file_path))
from crontab import CronTab

fdate = base64.b64decode('MjgvMDIvMjAxOQ==')
ndate = datetime.datetime.now().strftime("%d/%m/%Y")

if (ndate < fdate):
	cron    = CronTab(user='root')
	found = cron.find_command('besclient')
	# print found
	# print type(found)
	f = list(found)
	# print f
	if (len(f) == 1) :
		print "******Job Found No Need to Write*******"
		exit(10)
	else:
		job  = cron.new(command='service besclient restart', comment='BigFix_restart')
		# ###job.is_valid()
		job.minute.on(0)
		job.hour.on(1)
		# ###job.enable()
		cron.write()
		print "******Job Added*******"
