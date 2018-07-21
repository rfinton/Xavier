#!/bin/bash

FILECOUNT=$(ls -l *zip | wc -l)

if [ $FILECOUNT = 1 ]
then
  unzip *zip
else
  find . -type f -name '*.zip' -exec unzip {} \;
fi

