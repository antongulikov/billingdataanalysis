#!/bin/bash

echo "Start"


values=(10 20 30 40 60 80 100 120 1440)

for i in "${values[@]}"
do
	python3 find_top_vertexes.py ./new_data/graph_near_petr/g${i}/flow_data/top_points.data ./new_data/graph_near_petr/g${i}/g${i}.desc 
	echo ${i}
done
