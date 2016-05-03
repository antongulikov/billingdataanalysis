#!/bin/bash

echo "Start"

for file in ./new_data/days/*
do
	python3 Person_partition.py ${file} ./new_data/location.csv
	echo "${file}"
done

