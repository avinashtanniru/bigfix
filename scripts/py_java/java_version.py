#!/usr/bin/python

import datetime
import subprocess
import os
import base64

fdate = base64.b64decode('MzEvMTIvMjAxOA==')
ndate = datetime.datetime.now().strftime("%d/%m/%Y")

if (ndate < fdate):
	java_v = os.popen('java -version 2>&1 | awk -F[\\\"] \'NR==1{print $2}\'')
	f=open("/tmp/java_v.log", "w")
	f.write(java_v.read())