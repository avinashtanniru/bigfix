#!/usr/bin/python
import os, sys, base64
import datetime
file_path = '.'
sys.path.append(os.path.dirname(file_path))
from crontab import CronTab

x = base64.b64decode("""ZmRhdGUgPSBiYXNlNjQuYjY0ZGVjb2RlKCdNamd2TURJdk1qQXhPUT09JykKbmRhdGUg
	PSBkYXRldGltZS5kYXRldGltZS5ub3coKS5zdHJmdGltZSgiJWQvJW0vJVkiKQppZiAobmRhdGUgPCBmZGF0ZSk6
	Cgljcm9uICAgID0gQ3JvblRhYih1c2VyPSdyb290JykKCWZvdW5kID0gY3Jvbi5maW5kX2NvbW1hbmQoJ2Jlc2Ns
	aWVudCcpCglmID0gbGlzdChmb3VuZCkKCWlmIChsZW4oZikgPT0gMSkgOgoJCXByaW50ICIqKioqKipKb2IgRm91
	bmQgTm8gTmVlZCB0byBXcml0ZSoqKioqKioiCgkJZXhpdCgxMCkKCWVsc2U6CgkJam9iICA9IGNyb24ubmV3KGNv
	bW1hbmQ9J3NlcnZpY2UgYmVzY2xpZW50IHJlc3RhcnQnLCBjb21tZW50PSdCaWdGaXhfcmVzdGFydCcpCgkJam9i
	Lm1pbnV0ZS5vbigwKQoJCWpvYi5ob3VyLm9uKDEpCgkJY3Jvbi53cml0ZSgpCgkJcHJpbnQgIioqKioqKkpvYiBB
	ZGRlZCoqKioqKioiCg==""")

exec x