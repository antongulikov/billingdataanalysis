#!/bin/bash


value=(10 20 30 40 60 80 100 120 1440)
top=(10 20 30 40 50 60 70 80 90 100 200)


for i in "${value[@]}"
do
	echo "${i}"
	cd ./new_data/graph_near_petr/g${i}/flow_data/
	rm -r html_result
	mkdir html_result
	cd ../../../../
	for j in "${top[@]}"
	do
		echo "${i} ${j}"
		python3 draw_top_places.py ./new_data/graph_near_petr/g${i}/flow_data/top_vertex_${j}.data ./new_data/graph_near_petr/g${i}/flow_data/new_edges_desc.data ./new_data/graph_near_petr/g${i}/flow_data/html_result/ret_vert${j}.html
		python3 drow_top_pathes.py ./new_data/graph_near_petr/g${i}/flow_data/top_edges_${j}.data ./new_data/graph_near_petr/g${i}/flow_data/new_edges_desc.data ./new_data/graph_near_petr/g${i}/flow_data/html_result/top_edges_${j}.html
	done
done