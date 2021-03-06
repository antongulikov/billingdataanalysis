#!/bin/bash

echo "Start"


values=(1 2 3 5 10 20 30 40 60 80 100 120 1440)

for i in "${values[@]}"
do
	cd new_data/graph/
	mkdir "g${i}"
	cd ../../
	python3 graph_builder.py ./new_data/graph/g${i}/g${i} ${i}
	echo $i
done

echo "Finish Build"
