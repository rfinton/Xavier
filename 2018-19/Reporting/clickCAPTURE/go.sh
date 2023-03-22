#!/bin/bash

unzip *.zip
sleep 1s
rm config.csv
php clickCAPTURE.php
php sendreport.php
rm *.csv
rm *.xlsx
mv *.zip archive
