#!/bin/bash

#checking if NAVAll.txt file present in local dir and downloading it if not.
if [ ! -f "NAVAll.txt" ]; then
    curl -o NAVAll.txt https://www.amfiindia.com/spages/NAVAll.txt
fi

#finding scheme name and value column in NAVAll.txt file using awk and printing it in scheme.tsv
awk -F ";" 'NF > 3 {print $4 "\t" $5}' NAVAll.txt > "scheme.tsv"
