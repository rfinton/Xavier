#!/bin/bash

ZIPFILE="$(ls *.zip)"

if [ "$ZIPFILE" = "" ]
	then
		php sendreport.php archive/NoData.csv
	else
		unzip $ZIPFILE
#		sleep 1s
#		php sendreport.php *.csv
#		rm *.csv
#		mv *.zip archive
fi
