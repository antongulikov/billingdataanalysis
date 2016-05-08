#!/bin/bash

values=(10 20 30 40 60 80 100 120 1440)

for i in "${values[@]}"
do
	python3 new_vertex_on_the_path.py ./new_data/graph_near_petr/g${i}/flow_data/top_edges.data ./new_data/graph_near_petr/g${i}/g${i}.desc ./new_data/graph_near_petr/inter_points.data ./new_data/graph_near_petr/g${i}/flow_data/new_edges.data ./new_data/graph_near_petr/g${i}/flow_data/new_edges_desc.data
	echo ${i}
done