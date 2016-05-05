#!/bin/bash

echo "Start"


values=(10 20 30 40 60 80 100 120 1440)

for i in "${values[@]}"
do
	cd new_data/graph_near_petr/g${i}
	rm -r flow_data
	mkdir flow_data
	cd ../../../
	python3 top_places.py ./new_data/graph_near_petr/g${i}/g${i}.desc ./new_data/graph_near_petr/g${i}/g${i}.graph ./new_data/graph_near_petr/g${i}/flow_data/top_points.data
	echo $i
	python3 create_marker_place.py ./new_data/graph_near_petr/g${i}/flow_data/top_points.data 
done