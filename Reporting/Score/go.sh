#!/bin/bash

unzip *.zip
php score.php *.csv
php sendreport.php score.csv
rm *.csv
mv *.zip archive