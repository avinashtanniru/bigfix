#!/bin/bash  

srcfile="besclient.config"
srcdir="/var/opt/BESClient"
#srcdir="/home/venkatpk/Desktop"

echo "BES Client stopping....."
/etc/init.d/besclient stop

DATE=`date +%Y%m%d`

echo "Taking backup of besclient.config file"
cp "$srcdir/$srcfile" "$srcdir/$srcfile.bak.$DATE"

sed '/__RelaySelect_Automatic/!b;n;cvalue                          = 0' "$srcdir/$srcfile" > "$srcdir/$srcfile.new.$DATE"
mv "$srcdir/$srcfile.new.$DATE"  $srcdir/$srcfile

sed '/__RelayServer1/!b;n;cvalue                          = http:\/\/172.22.0.21:52311\/bfmirror\/downloads\/' "$srcdir/$srcfile" > "$srcdir/$srcfile.new.$DATE"
mv "$srcdir/$srcfile.new.$DATE"  $srcdir/$srcfile


echo "BES Client starting....."
/etc/init.d/besclient start 

echo "Task Completed...$?"

